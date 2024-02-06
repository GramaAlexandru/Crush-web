from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_route():
    return render_template('main.html')

@app.route('/întrebare')
def home():
    return render_template('index.html')

@app.route('/da')
def another_route():
    return render_template('yes_choice.html')  
 

if __name__ == '__main__':
    app.run(debug=True, port= 5000)