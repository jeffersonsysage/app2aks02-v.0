# from flask import Flask, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # 這行會為所有路由啟用 CORS

# @app.route('/api')
# def hello_world():
#     return jsonify({"msg": "Hello World"})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 这行会为所有路由启用 CORS

@app.route('/api')
def hello_world():
    return jsonify({"msg": "Hello World"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)