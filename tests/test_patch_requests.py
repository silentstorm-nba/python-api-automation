import logging
import pytest
import allure

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

sample_patch_data = {
    "title": "foo"
}

def log_response(response):
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

@pytest.mark.parametrize("endpoint, data", [
    ("/posts/1", sample_patch_data),
    ("/comments/1", {"body": "updated body"}),
    ("/albums/1", {"title": "updated title"}),
    ("/photos/1", {"title": "updated title"}),
    ("/todos/1", {"completed": True}),
    ("/users/1", {"username": "updated_test"})
])
@allure.feature('PATCH Requests')
@allure.story('Test PATCH requests for various endpoints')
def test_patch_requests(base_url, session, endpoint, data):
    with allure.step(f"Sending PATCH request to {base_url + endpoint} with data {data}"):
        response = session.patch(base_url + endpoint, json=data)
        log_response(response)
    with allure.step("Asserting the response status code"):
        assert response.status_code == 200
    with allure.step("Asserting the response body contains the updated data"):
        response_data = response.json()
        for key in data:
            assert response_data[key] == data[key]
