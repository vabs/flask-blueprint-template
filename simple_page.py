from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound

# registering a blueprint
# using standard templates folder
# using custom static folder
simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates', url_prefix='/simple', static_folder='static_page')

#loading page from '/simple'
@simple_page.route('/')
def show():
    try:
        return render_template('pages.html')
    except TemplateNotFound:
        abort(404)


# loading a page on a suburl
# used for loading js from custom static folder ( static_page )
@simple_page.route('/test')
def show_test():
    try:
        return render_template('pages_test.html')
    except TemplateNotFound:
        abort(404)


# method trying to load the page which does not exists
# used for showing the blueprint error handling for 404
@simple_page.route('/load')
def show_error():
    try:
        return render_template('not_found.html')
    except TemplateNotFound:
        abort(404)


@simple_page.errorhandler(404)
def simple_page_404(e):
    print e
    print 'from simple_page blueprint'
    return jsonify({'status': '404 from simple_page blueprint'})

