from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')

@main.route('/test')
def test():
    return render_template('test.html')