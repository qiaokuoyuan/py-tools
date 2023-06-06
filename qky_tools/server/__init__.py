import flask
from flask_cors import CORS

app = flask.Flask(__name__)


@app.route('/')
def g():
    return {
        'code': 200,
        'data': {
            'data': [{'name': '张三', 'age': i} for i in range(1, 10)],
            'pageNum': 1,
            'pageSize': 10,
            'total': 20

        }

    }


CORS(app, supports_credentials=True)
app.run("0.0.0.0", port=10086)
