from flask import Flask

from minizincweb import solver_bp

application = app = Flask(__name__)

app.register_blueprint(solver_bp)

@app.route('/')
def main():
    return {
        'status': 'OKs',
    }


if __name__ == '__main__':
    import logging

    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')


