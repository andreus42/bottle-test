from bottle import route, run
from bottle import template

@route('/hello')
def hello():
    return "Hello, world!"

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/goodbye')
def goodbye(name='Stranger'):
	return template ("Goodbye, cruel world!\nI'm leaving you today, {{name}}.", name=name)

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()

@route('/static/<path:path>')
def callback(path):
    return static_file(path, ...)

run(host='localhost', port=8080, debug=True)
