from flask import Flask
x=Flask(__name__)
@x.route('/ism')
def display():
    return "welcome to ISM"
if __name__=='__main__':
    x.run(debug=True)