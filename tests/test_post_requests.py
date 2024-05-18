import logging
import pytest
import allure

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

sample_post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

def log_response(response):
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

@pytest.mark.parametrize("endpoint, data", [
    ("/posts", sample_post_data),
    ("/comments", {"postId": 1, "name": "test", "email": "test@test.com", "body": "test body"}),
    ("/albums", {"title": "test", "userId": 1}),
    ("/photos", {"albumId": 1, "title": "test", "url": "http://test.com", "thumbnailUrl": "http://test.com"}),
    ("/todos", {"title": "test", "completed": False, "userId": 1}),
    ("/users", {"name": "test", "username": "test", "email": "test@test.com"})
])
@allure.feature('POST Requests')
@allure.story('Test POST requests for various endpoints')
def test_post_requests(base_url, session, endpoint, data):
    with allure.step(f"Sending POST request to {base_url + endpoint} with data {data}"):
        response = session.post(base_url + endpoint, json=data)
        log_response(response)
    with allure.step("Asserting the response status code"):
        assert response.status_code == 201
    with allure.step("Asserting the response body contains the sent data"):
        response_data = response.json()
        for key in data:
            assert response_data[key] == data[key]
