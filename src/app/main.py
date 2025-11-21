from typing import List

import requests
import uvicorn
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel


class Item(BaseModel):
    text: str


# Команда для запуска: uvicorn main:app --host 127.0.0.1 --port 8001
app = FastAPI()


def get_data_from_gigachat(text):
    response = requests.post(f'https://api.example.com/{text}')
    response.raise_for_status()
    return response.json()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.post("/gigachat/{text}")
def get_result_model(text: str):
    result = get_data_from_gigachat(text)
    return {'result_model': result}


@app.post("/text/")
def get_text(item: Item):
    return {"text": 'start_' + item.text + '_end'}


@app.post("/file/")
async def get_file(files: List[UploadFile]):
    list_files_data = []
    for file in files:
        contents = await file.read()
        list_files_data += [{"filename": file.filename, "content": contents}]
        await file.close()
    return {"files": list_files_data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8006)
