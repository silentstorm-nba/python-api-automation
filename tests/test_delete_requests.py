import logging
import pytest
import allure

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_response(response):
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

@pytest.mark.parametrize("endpoint", [
    "/posts/1", "/comments/1", "/albums/1", "/photos/1", "/todos/1", "/users/1"
])
@allure.feature('DELETE Requests')
@allure.story('Test DELETE requests for various endpoints')
def test_delete_requests(base_url, session, endpoint):
    with allure.step(f"Sending DELETE request to {base_url + endpoint}"):
        response = session.delete(base_url + endpoint)
        log_response(response)
    with allure.step("Asserting the response status code"):
        assert response.status_code == 200
    with allure.step("Asserting the response body is empty"):
        assert response.json() == {}
