import logging
import os
import pytest
from datetime import datetime
from config import BASE_URL
import requests

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure logging to file with timestamp in the filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_filename = f"logs/api_tests_{timestamp}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

@pytest.fixture(scope="session")
def session():
    return requests.Session()

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def logger_fixture():
    return logger
