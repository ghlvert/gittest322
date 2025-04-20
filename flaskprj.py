from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>hw</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)