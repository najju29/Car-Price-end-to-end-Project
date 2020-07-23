from flask import Flask, request, render_template, redirect, url_for, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('maruti_model.pkl', 'rb'))
model1= pickle.load(open('tata_model.pkl', 'rb'))
model2= pickle.load(open('hyundai_model.pkl', 'rb'))
model3= pickle.load(open('Toyota_model.pkl', 'rb'))
model4= pickle.load(open('mahindra_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('index.html')

@app.route('/view1')
def view1():
    return render_template('about.html')


@app.route('/predict', methods=['POST', 'DELETE', 'GET'])
def predict():
    return render_template('Maruthi.html')

@app.route('/predictT', methods=['POST', 'DELETE'])
def predictT():
    return render_template('Tata.html')

@app.route('/predictH', methods=['POST', 'DELETE'])
def predictH():
    return render_template('Hyundai.html')

@app.route('/predictToy', methods=['POST', 'DELETE'])
def predictToy():
    return render_template('Toyato.html')

@app.route('/predictM', methods=['POST', 'DELETE'])
def predictM():
    return render_template('Mahindra.html')



@app.route('/predict1', methods=['POST', 'DELETE', 'GET'])
def predict1():
    year = request.form['year']
    km_driven = request.form['km_driven']
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    Model_Name = request.form['Model_Name']

    int_features = [year, km_driven, fuel, seller_type, transmission, owner, Model_Name]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('Maruthi.html', predict_text='The Estimated Price of your Car is {}'.format(output))

@app.route('/predict2', methods=['POST', 'DELETE', 'GET'])
def predict2():
    year=request.form['year']
    km_driven = request.form['km_driven']
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    Model_Name = request.form['Model_Name']

    int_features1 = [year, km_driven, fuel, seller_type, transmission, owner, Model_Name]
    final_features1 = [np.array(int_features1)]
    prediction1 = model1.predict(final_features1)

    output1 = round(prediction1[0], 2)
    return render_template('Tata.html', predict_text1='The Estimated Price of your car is {}'.format(output1))


@app.route('/predict3', methods=['POST', 'DELETE', 'GET'])
def predict3():
    year=request.form['year']
    km_driven = request.form['km_driven']
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    Model_Name = request.form['Model_Name']

    int_features1 = [year, km_driven, fuel, seller_type, transmission, owner, Model_Name]
    final_features1 = [np.array(int_features1)]
    prediction1 = model2.predict(final_features1)

    output1 = round(prediction1[0], 2)
    return render_template('Hyundai.html', predict_text1='The Estimated Price of your car is {}'.format(output1))

@app.route('/predict4', methods=['POST', 'DELETE', 'GET'])
def predict4():
    year=request.form['year']
    km_driven = request.form['km_driven']
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    Model_Name = request.form['Model_Name']

    int_features1 = [year, km_driven, fuel, seller_type, transmission, owner, Model_Name]
    final_features1 = [np.array(int_features1)]
    prediction1 = model3.predict(final_features1)

    output1 = round(prediction1[0], 2)
    return render_template('Toyato.html', predict_text1='The Estimated Price of your car is {}'.format(output1))


@app.route('/predict5', methods=['POST', 'DELETE', 'GET'])
def predict5():
    year=request.form['year']
    km_driven = request.form['km_driven']
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    Model_Name = request.form['Model_Name']

    int_features1 = [year, km_driven, fuel, seller_type, transmission, owner, Model_Name]
    final_features1 = [np.array(int_features1)]
    prediction1 = model4.predict(final_features1)

    output1 = round(prediction1[0], 2)
    return render_template('Mahindra.html', predict_text1='The Estimated Price of your car is {}'.format(output1))



if __name__ == '__main__':
    app.run(debug=True)
