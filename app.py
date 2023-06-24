from flask import Flask,request
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))


@app.route('/home', methods = ['GET','POST'])    #creating API
def welcome():
    data = request.form
    if request.method == 'POST':
        joke = data['joke']    #request.form.get(variable name from html)

    Result = model.predict(joke)
    if Result[0] == 0:
        return 'This is not funny'
    else:
        return 'This is very funny'

@app.route('/login')    #creating API
def login():
    return 'This is a login page'

@app.route('/feed')    #creating API
def feed():
    return 'Display feed'

if __name__ == '__main__':
    app.run(debug=True)