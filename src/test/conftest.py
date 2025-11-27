import pytest


@pytest.fixture(scope='function')
def test_get_result_model_data() -> tuple[str, dict, dict]:
    input_data = 'hello'
    response_gigachat = {
        'name': 'gigachat',
        'result': 'Hello i am gigachat. Who are you????',
    }

    result_data = {
        'result_model': {
            'name': 'gigachat',
            'result': 'Hello i am gigachat. Who are you????',
        }
    }
    return input_data, response_gigachat, result_data
