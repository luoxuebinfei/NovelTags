from typing import Union

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.bin.LoadBookFile import Book

app = FastAPI()

# 设置允许访问的域名
origins = ["*"]  # 也可以设置为"*"，即为所有。

# 设置跨域传参
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"])  # 允许跨域的headers，可以用来鉴别来源等作用。


@app.get("/")
def read_root():
    return Book().read_file()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    from src.killport import killport

    killport("8000")  # 释放被占用的端口

    uvicorn.run(app, host="127.0.0.1", port=8000)
