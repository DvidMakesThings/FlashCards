# Build APK Workflow for FlashCards

This repository contains a GitHub Actions workflow to automate building an Android APK for the FlashCards project. This workflow ensures dependencies are properly configured, the environment is set up correctly, and the APK is built and uploaded to the repository.

## Overview

The workflow is triggered on every push to the master branch. It sets up a build environment, installs necessary dependencies, and executes the build process using Buildozer, a Python-based tool for building Android APKs. The final APK is automatically pushed back to the repository.

## Workflow Details

The workflow is defined in `.github/workflows/build.yml` and consists of the following key steps:

### Trigger

The workflow is triggered by any push to the master branch:

```yaml
on:
    push:
        branches:
            - master
```

### Steps Explanation

**Step 1: Checkout Repository**

The `actions/checkout` action is used to pull the latest code from the repository.

```yaml
- name: Checkout Repository
    uses: actions/checkout@v3
```

**Step 2: Update System**

Ensures the system's package manager has the latest package metadata.

```yaml
- name: Update System
    run: sudo apt update
```

**Step 3: Install Required Packages**

Installs the essential dependencies for Python, Java, and Buildozer. Key packages include:

- Python 3.9 and related development libraries.
- Java 17 as the required JDK version for Gradle and Buildozer.
- System tools like autoconf, libtool, pkg-config, and others.

```yaml
- name: Install Required Packages
    run: |
        sudo apt install -y git zip unzip openjdk-17-jdk python3.9 python3.9-venv python3.9-dev \
            autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
            cmake libffi-dev libssl-dev
```

**Step 4: Set Java 17 as Default**

Configures Java 17 as the default version for the build environment.

```yaml
- name: Set Java 17 as Default
    run: |
        sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-17-openjdk-amd64/bin/java 1
        sudo update-alternatives --set java /usr/lib/jvm/java-17-openjdk-amd64/bin/java
        sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-17-openjdk-amd64/bin/javac 1
        sudo update-alternatives --set javac /usr/lib/jvm/java-17-openjdk-amd64/bin/javac
        export JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
        echo "export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64" >> ~/.bashrc
```

**Step 5: Set Up Virtual Environment**

Creates a Python virtual environment to isolate dependencies.

```yaml
- name: Set Up Virtual Environment
    run: |
        python3.9 -m venv venv
        source venv/bin/activate
        python -m pip install --upgrade pip
```

**Step 6: Install Python Packages**

Installs Buildozer, pyjnius, and other required Python packages in the virtual environment.

```yaml
- name: Install Required Python Packages in `venv`
    run: |
        source venv/bin/activate
        pip install Cython==0.29.33 pyjnius virtualenv buildozer
        pip install --force-reinstall Cython==0.29.33
```

**Step 7: Set Environment Variables**

Sets environment variables for Buildozer and Python.

```yaml
- name: Set Environment Variables
    run: |
        source venv/bin/activate
        export PATH=$PATH:~/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
        export PYTHONPATH=$HOME/.local/lib/python3.9/site-packages:/usr/local/lib/python3.9/dist-packages:$PYTHONPATH
```

**Step 8: Clone FlashCards Repository**

Clones the FlashCards repository to prepare for building the APK.

```yaml
- name: Clone FlashCards Repository
    run: git clone https://github.com/DvidMakesThings/FlashCards.git ~/FlashCards
```

**Step 9: Force Cythonize pyjnius**

Addresses potential compatibility issues with pyjnius by manually rebuilding it.

```yaml
- name: Force Cythonize pyjnius Manually
    run: |
        source venv/bin/activate
        git clone https://github.com/kivy/pyjnius.git ~/pyjnius
        cd ~/pyjnius
        python setup.py build_ext --inplace
        pip install .
```

**Step 10: Verify Python Packages**

Confirms that the required Python packages are installed correctly.

```yaml
- name: Verify Python Packages Installation
    run: |
        source venv/bin/activate
        pip show Cython
        pip show pyjnius
        pip show virtualenv
        pip show buildozer
```

**Step 11: Build APK**

Uses Buildozer to build the APK. The `JAVA_HOME` variable ensures the correct JDK version is used.

```yaml
- name: Build APK
    env:
        JAVA_HOME: /usr/lib/jvm/java-17-openjdk-amd64
    run: |
        source venv/bin/activate
        cd ~/FlashCards
        yes | buildozer -v android debug
```

**Step 12: Upload APK**

The APK is pushed back to the repository in the bin directory. The workflow uses a secret token (PUSH) to authenticate the commit.

```yaml
- name: Upload APK to Repository
    env:
        PUSH: ${{ secrets.PUSH }}
    run: |
        source venv/bin/activate
        cd ~/FlashCards
        mkdir -p bin
        mv bin/*.apk ./bin/ || echo "No APK found to upload"
        git config --global user.name "github-actions[bot]"
        git config --global user.email "github-actions[bot]@users.noreply.github.com"
        git add .
        git commit -m "APK autobuilder [skip ci]"
        git push https://DvidMakesThings:${{ secrets.PUSH }}@github.com/DvidMakesThings/FlashCards.git master
```

## Programs and Tools Used

- **GitHub Actions** - For automating the workflow.
- **Buildozer** - To build the Android APK.
- **Python 3.9** - For the project's runtime environment.
- **Java 17** - Required for the Android Gradle Plugin.
- **Cython and pyjnius** - Python dependencies used in the project.
- **Gradle** - Build system for Android projects.

## File Structure

The workflow is designed to adapt to a variety of project structures. A typical setup might include:

```plaintext
.
├── .github/
│   └── workflows/
│       └── build.yml         # Workflow file for GitHub Actions
├── main.py                   # Main program entry point
├── app.kv                    # Kivy layout/UI file
├── core/                     # Core logic (Flashcard, Manager, Algorithm)
├── gui/                      # GUI components and handlers
├── storage/                  # Data storage (e.g., JSON or SQLite)
├── unittest/                 # Unit tests and reports
├── LICENSE                   # License file
└── README.md                 # This README file
```

While the workflow assumes a structure like this, modifications can be made to suit your specific project.

## Secrets Required

The following GitHub secrets must be configured for the workflow to run successfully:

- **PUSH**: Personal access token for pushing the APK back to the repository.

## License

This project is licensed under the GPL-3.0 License. See the LICENSE file for details.

## Contact

For any questions or feedback, please contact:

- **Email**: s.dvid@hotmail.com
- **GitHub**: [DvidMakesThings](https://github.com/DvidMakesThings)
