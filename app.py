from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'premji'


@app.route("/",methods=['GET'])
def inital():
    return "Welcome prem"

if __name__ == '__main__':
    app.run(debug=True, port=5000)