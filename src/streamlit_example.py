import requests
import streamlit as st


HOST_API = 'http://127.0.0.1'
PORT_API = '8006'


def send_file_to_api(data: list):
    """Функция для передачи файла в api"""
    files = [(f'files', data[i]) for i in range(len(data))]
    response = requests.post(url=f'{HOST_API}:{PORT_API}/file/', files=files)
    return response.status_code, response.content


st.title('Тестируем fastapi вместе с streamlit')


uploaded_file = st.file_uploader("Выберите файл", accept_multiple_files=True, type=["txt", "docx"])

button_send_file_result = st.button('Отправить файл на обработку')

if button_send_file_result and uploaded_file:
    files_data = [(file.name, file.getvalue(), "text/plain") for file in uploaded_file]

    st.write('**Input data:**')
    st.write(files_data)

    result = send_file_to_api(files_data)

    st.write('**Result test:**')
    st.write(result)
