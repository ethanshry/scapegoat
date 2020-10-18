from bottle import route, run, template
@route('/')
def index():
    return "Hello, Index"

@route('/fancy')
def index():
    return "Fancy Route~~~ :p"

@route('/app/info')
def app_info():
    with open('./src/env.txt', 'r') as env:
        tmp = '<h1> Scapegoat App Info </h1>'
        for line in env.readlines():
            tmp = f'{tmp} <h5>{line}</h5>'
        return tmp

run(host='0.0.0.0', port=9000)
