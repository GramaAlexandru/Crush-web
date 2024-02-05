from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yes_choice')
def another_route():
    return render_template('yes_choice.html')  

@app.route('/TEST')
def TEST_route():
    return render_template('TEST.html') 

if __name__ == '__main__':
    app.run(debug=True, port= 3000)