import logging
import pytest
import allure

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

sample_put_data = {
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1
}

def log_response(response):
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response Body: {response.json()}")

@pytest.mark.parametrize("endpoint, data", [
    ("/posts/1", sample_put_data),
    ("/comments/1", {"id": 1, "postId": 1, "name": "test", "email": "test@test.com", "body": "test body"}),
    ("/albums/1", {"id": 1, "title": "test", "userId": 1}),
    ("/photos/1", {"id": 1, "albumId": 1, "title": "test", "url": "http://test.com", "thumbnailUrl": "http://test.com"}),
    ("/todos/1", {"id": 1, "title": "test", "completed": False, "userId": 1}),
    ("/users/1", {"id": 1, "name": "test", "username": "test", "email": "test@test.com"})
])
@allure.feature('PUT Requests')
@allure.story('Test PUT requests for various endpoints')
def test_put_requests(base_url, session, endpoint, data):
    with allure.step(f"Sending PUT request to {base_url + endpoint} with data {data}"):
        response = session.put(base_url + endpoint, json=data)
        log_response(response)
    with allure.step("Asserting the response status code"):
        assert response.status_code == 200
    with allure.step("Asserting the response body contains the updated data"):
        response_data = response.json()
        for key in data:
            assert response_data[key] == data[key]
