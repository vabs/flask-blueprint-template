from flask import Flask, jsonify, abort
from jinja2 import TemplateNotFound
from simple_page import simple_page

__author__ = 'vaibhav'

app = Flask(__name__)
app.register_blueprint(simple_page)
app.debug = True


@app.route('/')
def home_page():
    try:
        return jsonify({'status': 'ok'})
    except TemplateNotFound:
        abort(404)


# app's default 404 error handler
@app.errorhandler(404)
def error_404(e):
    print e
    print 'from app'
    return jsonify({'status': 404})


# app's default 500 error handler
@app.errorhandler(500)
def error_500(e):
    print e
    return jsonify({'status': 500})


if __name__ == "__main__":
    app.run()