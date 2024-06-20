from flask import Flask,render_template

app = Flask(__name__)

# 创建了网址/show/info 和函数index 的对应关系
@app.route("/show/info")
def index():
    # 默认去templates文件夹找文件
    return render_template("index.html")
@app.route("/get/news")
def getnews():
    # 默认去templates文件夹找文件
    return render_template("getnews.html")

if __name__ == '__main__':
    app.run(host="",port="8000")