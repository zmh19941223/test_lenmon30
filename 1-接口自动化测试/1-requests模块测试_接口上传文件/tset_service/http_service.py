"""
============================
author:MuSen
time:2019/6/21
E-mail:3247119728@qq.com
============================
"""
import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from flask import send_from_directory
import datetime

app = Flask(__name__)

# 文件上传的路径
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/upload', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template("upload_page.html")
    else:
        # 获取请求的参数
        name = request.form.get('nickname')
        sex = request.form.get("sex")
        age = request.form.get("age")
        # 获取上传的图片
        avatar = request.files.get('pic')
        if all([name, sex, age, avatar]):
            # 保存文件
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            msg = "文件上传成功,文件保存的地址为：http://127.0.0.1:5000/images/{}".format(filename)
            data = {
                "code": 1,
                "data": {
                    "name": name,
                    "sex": sex,
                    "age": age,
                    "filename": filename,
                    "datetime": datetime.datetime.now()
                },
                "msg": msg
            }
        else:
            # 返回内容：
            data = {
                "code": 1,
                "data": None,
                "msg": "参数不能为空！"
            }

        return jsonify(data)


@app.route('/images/<filename>', methods=['GET', 'POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run(debug=True)
