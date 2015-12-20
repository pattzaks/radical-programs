import flask
import sys

app = flask.Flask (__name__)

@app.route('/v1/akshay')
def func_name_any():
    return 'v1/akshay on 9001' 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
