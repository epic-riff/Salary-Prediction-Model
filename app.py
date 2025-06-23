from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('expredmodel.pickle', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predection', methods=['GET', 'POST'])
def predection():
    if request.method == 'POST':
        pred = [[float(request.form.get('exp'))]]
        predection = model.predict(pred)
        predection = round(predection[0], 2)
        return render_template('index.html', predection='$'+str(predection))
    return render_template('index.html', predection="Form Failed, Please Try Again")
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
    