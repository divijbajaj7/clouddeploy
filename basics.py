from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return "<p>Hello, World! My name is Divij</p>"
    #return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)


# this is new code 


