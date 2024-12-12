"""
Custom HTML test runner for detailed test reports.
"""
import unittest
from datetime import datetime
import os
from jinja2 import Template

class CustomTestResult(unittest.TestResult):
    """Custom TestResult class that tracks successful tests."""
    
    def __init__(self):
        super().__init__()
        self.successes = []
        
    def addSuccess(self, test):
        """Record successful tests."""
        super().addSuccess(test)
        self.successes.append(test)

class HTMLTestRunner:
    """Custom test runner that generates detailed HTML reports."""
    
    def __init__(self, output_dir="test_reports"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
    def run(self, test_suite):
        """Run the test suite and generate HTML report."""
        result = CustomTestResult()
        start_time = datetime.now()
        test_suite.run(result)
        end_time = datetime.now()
        
        # Generate report data
        report_data = {
            'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration': str(end_time - start_time),
            'total_tests': result.testsRun,
            'failures': len(result.failures),
            'errors': len(result.errors),
            'success_rate': f"{((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.2f}%",
            'test_cases': []
        }
        
        # Process test results
        for test, err in result.failures + result.errors:
            status = 'FAIL' if (test, err) in result.failures else 'ERROR'
            report_data['test_cases'].append(self._create_test_case_data(test, status, err))
            
        for test in result.successes:
            report_data['test_cases'].append(self._create_test_case_data(test, 'PASS'))
            
        # Generate HTML report
        self._generate_html_report(report_data)
        return result
        
    def _create_test_case_data(self, test, status, error=None):
        """Create test case data dictionary."""
        doc = test._testMethodDoc or ""
        
        # Extract sections from docstring
        sections = self._parse_docstring(doc)
        
        return {
            'name': test.id(),
            'description': sections.get('description', "No description"),
            'status': status,
            'error': error,
            'specification': sections.get('specification', "No specification provided"),
            'criteria': sections.get('criteria', "No criteria specified")
        }
        
    def _parse_docstring(self, doc):
        """Parse docstring into sections."""
        sections = {}
        
        # Get description (first paragraph)
        parts = doc.strip().split('\n\n', 1)
        if parts:
            sections['description'] = parts[0].strip()
        
        # Find specification
        spec_start = doc.find('Specification:')
        if spec_start != -1:
            spec_end = doc.find('\n\n', spec_start)
            if spec_end == -1:
                spec_end = len(doc)
            spec_text = doc[spec_start:spec_end].split('\n', 1)
            if len(spec_text) > 1:
                sections['specification'] = spec_text[1].strip()
        
        # Find criteria
        criteria_start = doc.find('Criteria:')
        if criteria_start != -1:
            criteria_end = doc.find('\n\n', criteria_start)
            if criteria_end == -1:
                criteria_end = len(doc)
            criteria_text = doc[criteria_start:criteria_end].split('\n', 1)
            if len(criteria_text) > 1:
                sections['criteria'] = criteria_text[1].strip()
        
        return sections
        
    def _generate_html_report(self, data):
        """Generate HTML report using template."""
        template = Template('''
<!DOCTYPE html>
<html>
<head>
    <title>Test Report</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 20px;
            line-height: 1.6;
        }
        .header { 
            background: #f8f9fa; 
            padding: 20px; 
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .summary { 
            margin: 20px 0;
            padding: 15px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .test-case { 
            border: 1px solid #ddd; 
            margin: 15px 0; 
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .PASS { 
            background-color: #d4edda;
            border-left: 5px solid #28a745;
        }
        .FAIL { 
            background-color: #f8d7da;
            border-left: 5px solid #dc3545;
        }
        .ERROR { 
            background-color: #fff3cd;
            border-left: 5px solid #ffc107;
        }
        .details { 
            margin-top: 15px;
            padding: 10px;
            background: rgba(0,0,0,0.05);
            border-radius: 3px;
        }
        .criteria { 
            font-style: italic;
            color: #666;
        }
        h1, h2, h3 { 
            color: #333;
            margin-top: 0;
        }
        pre {
            background: #f8f9fa;
            padding: 10px;
            border-radius: 3px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Test Execution Report</h1>
        <p><strong>Start Time:</strong> {{ start_time }}</p>
        <p><strong>Duration:</strong> {{ duration }}</p>
    </div>
    
    <div class="summary">
        <h2>Summary</h2>
        <p><strong>Total Tests:</strong> {{ total_tests }}</p>
        <p><strong>Success Rate:</strong> {{ success_rate }}</p>
        <p><strong>Failures:</strong> {{ failures }}</p>
        <p><strong>Errors:</strong> {{ errors }}</p>
    </div>
    
    <div class="test-cases">
        <h2>Test Cases</h2>
        {% for test in test_cases %}
        <div class="test-case {{ test.status }}">
            <h3>{{ test.name }}</h3>
            <p><strong>Description:</strong> {{ test.description }}</p>
            <p><strong>Specification:</strong> {{ test.specification }}</p>
            <p><strong>Pass/Fail Criteria:</strong> {{ test.criteria }}</p>
            <p><strong>Status:</strong> {{ test.status }}</p>
            {% if test.error %}
            <div class="details">
                <p><strong>Error Details:</strong></p>
                <pre>{{ test.error }}</pre>
            </div>
            {% endif %}
        </div>
        {% endfor %}
    </div>
</body>
</html>
        ''')
        
        report_path = os.path.join(self.output_dir, f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(report_path, 'w') as f:
            f.write(template.render(**data))