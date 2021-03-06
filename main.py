from flask import Flask, render_template, request
import pickle
import numpy as np

file = 'diabetes-prediction-model.pkl'
classifier = pickle.load(open(file, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction', methods = ['POST'])
def prediction():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])

    data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
    my_prediction = classifier.predict(data)

    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run(debug=True)