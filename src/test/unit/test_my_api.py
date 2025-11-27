from fastapi.testclient import TestClient
from app.main import app

import pytest
from unittest.mock import patch, Mock

client = TestClient(app)


@pytest.mark.parametrize("input_data, expected_result", [
    ({'text': 'test_1'}, {'text': 'start_test_1_end'}),
])
def test_get_text(input_data, expected_result):
    response = client.post(url='/text/', json=input_data)
    assert response.status_code == 200
    assert response.json() == expected_result


def test_get_result_model(test_get_result_model_data: tuple[str, dict, dict]):

    input_data, response_gigachat, expected_result = test_get_result_model_data

    with patch('requests.post') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = response_gigachat
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем нашу функцию
        response = client.post(url=f'/gigachat/{input_data}')
        content = response.json()

        # Проверяем результат
        assert content == expected_result

        # Проверяем, что requests.post был вызван с правильными аргументами
        mock_get.assert_called_once_with('https://api.example.com/hello')
