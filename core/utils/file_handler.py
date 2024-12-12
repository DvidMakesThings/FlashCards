"""
File system operations for data persistence.
"""
import os
import json
from typing import List, Dict, Any

def ensure_storage_dir(storage_path: str) -> None:
    """
    Ensures the storage directory exists.
    
    Args:
        storage_path (str): Path to the storage directory
    """
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

def load_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        List[Dict[str, Any]]: The loaded data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json_file(file_path: str, data: List[Dict[str, Any]]) -> bool:
    """
    Saves data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        data: The data to save
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception:
        return False