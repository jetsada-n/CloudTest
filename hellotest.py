from flask import Flask
app = Flask (__name__)

@app.route("/")
def hello():
    return "เจษฎา นิ่มศิริ 6006021621017"

if __name__ == '__main__':

    app.run(host='0.0.0.0',port=80)
