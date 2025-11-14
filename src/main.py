from typing import List

import uvicorn
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel


class Item(BaseModel):
    text: str


# Команда для запуска: uvicorn main:app --host 127.0.0.1 --port 8001
app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.post("/text/")
def get_text(item: Item):
    return {"Text": item.text}


@app.post("/file/")
async def get_file(files: List[UploadFile]):
    list_files_data = []
    for file in files:
        contents = await file.read()
        list_files_data += [{"filename": file.filename, "content": contents}]
        await file.close()
    return {"files": list_files_data}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8006)
