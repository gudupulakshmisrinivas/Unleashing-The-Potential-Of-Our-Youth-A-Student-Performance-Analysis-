from flask import Flask, render_template, request


student = Flask(__name__) # initializng the flask app


@student.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    student.run(debug = False, port = 5000)