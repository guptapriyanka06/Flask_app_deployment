from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    return "<h>This is flask application</h>"

if __name__=="__main__":
    app.run()



