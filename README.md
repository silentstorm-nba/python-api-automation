# Python API Automation

This project contains automated tests for various API endpoints using Python, Pytest, and Allure for reporting. The tests include GET, POST, PUT, PATCH, and DELETE requests.

## Project Structure

```
api_test_project/
│
├── config.py
├── conftest.py
├── requirements.txt
├── .gitignore
│
├── logs/
│   └── api_tests_YYYYMMDD_HHMMSS.log
│
├── tests/
│   ├── __init__.py
│   ├── test_get_requests.py
│   ├── test_post_requests.py
│   ├── test_put_requests.py
│   ├── test_patch_requests.py
│   └── test_delete_requests.py
│
└── allure-results/
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/silentstorm-nba/python-api-automation.git
cd python-api-automation
```

### 2. Create and Activate a Virtual Environment

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Tests and Generate Allure Results

```bash
pytest --alluredir=allure-results
```

### 5. Generate and Open Allure Report

#### Install Allure Command-Line Tool

- **macOS**:
  ```bash
  brew install allure
  ```

- **Windows/Linux**:
  Download the binary from the [Allure installation page](https://docs.qameta.io/allure/#_installing_a_commandline).

#### Generate and Serve the Allure Report

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Logging

Logs are saved in the `logs` directory with a timestamped filename (e.g., `api_tests_YYYYMMDD_HHMMSS.log`).

## Acknowledgements

Special thanks to [jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com/) for providing a free and easy-to-use API for testing and prototyping.