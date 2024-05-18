import logging
import pytest
import allure

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_response(response):
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

@pytest.mark.parametrize("endpoint", [
    "/posts", "/comments", "/albums", "/photos", "/todos", "/users"
])
@allure.feature('GET Requests')
@allure.story('Test GET requests for various endpoints')
def test_get_requests(base_url, session, endpoint):
    with allure.step(f"Sending GET request to {base_url + endpoint}"):
        response = session.get(base_url + endpoint)
        log_response(response)
    with allure.step("Asserting the response status code"):
        assert response.status_code == 200
    with allure.step("Asserting the response body is not empty"):
        assert response.json() != []
