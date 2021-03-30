from bottle import route, run, template
@route('/')
def index():
    print("Standard")
    return "Hello, Index"

@route('/fancy')
def index():
    print("FANCAY")
    return "Fancy Route~~~ :)"

@route('/app/info')
def app_info():
    print("Seeking app info....")
    with open('./src/env.txt', 'r') as env:
        tmp = '<h1> Scapegoat App Info </h1>'
        for line in env.readlines():
            print("line")
            tmp = f'{tmp} <h5>{line}</h5>'
        return tmp

run(host='0.0.0.0', port=9000)
