import requests

# response = requests.get(' http://127.0.0.1:8001/1')

doc_text = {'text': 'wow'}
response = requests.post(url='http://127.0.0.1:8006/text', json=doc_text)
print(response.content, response)
