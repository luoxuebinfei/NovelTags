# 读取书籍配置文件
import json
import os


class Book:
    def __init__(self):
        self.file_path = r"src\userdata\Book.json"
        self.check_file_existence()

    # 查看文件是否存在,不存在则创建
    def check_file_existence(self):
        file_dir = os.path.dirname(self.file_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        if not os.path.exists(self.file_path):
            print(f"The file {self.file_path} does not exist.")
            with open(self.file_path, "w") as f:
                data = []
                json.dump(data, f)

    # 读取文件内容
    def read_file(self):
        with open(self.file_path, "r", encoding='utf-8') as f:
            data = json.load(f)
            # print(os.getcwd())
            # print(os.path.join(os.getcwd(), self.file_path))
        return data


if __name__ == '__main__':
    a = Book()
    print(a.read_file())
