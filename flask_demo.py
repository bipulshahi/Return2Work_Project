from flask import Flask

app = Flask(__name__)

@app.route('/')
def myName():
    return 'Bipul Kumar'

@app.route('/myEmail')
def myEmail():
    return 'bipul@hello.com'

app.run()
