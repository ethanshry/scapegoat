from bottle import route, run, template

def makeHtml(text):
    result = f"""
        <body>
        <h1>{text}<h2>
        </body>
        <style>
        h1 {{
            font-family: Arial;
            text-align: center;
            width: 100%;
            text-transform: capitalize;
        }}
        body {{
            background-color: pink;
            display: flex;
            height: 100vh;
            flex-direction: row;
            align-items: center;
        }}
        </style>
    """
    return result


@route('/')
def index():
    print("Standard")
    return makeHtml("Hello from python")

@route('/other')
def index():
    print("other route")
    return makeHtml("this is the other route :)")

@route('/app/info')
def app_info():
    print("Seeking app info...")
    with open('./src/env.txt', 'r') as env:
        tmp = '<h1> Scapegoat App Info </h1>'
        for line in env.readlines():
            print("line")
            tmp = f'{tmp} <h5>{line}</h5>'
        return makeHtml(tmp)

run(host='0.0.0.0', port=9000)
