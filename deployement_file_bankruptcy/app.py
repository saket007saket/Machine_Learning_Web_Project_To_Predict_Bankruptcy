import numpy as np
from flask import Flask, request, jsonify, render_template
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.tree import DecisionTreeClassifier
import pickle
model1=pickle.load(open('finalized_model5.pkl','rb'))
model2=pickle.load(open('finalized_model4.pkl','rb'))
model3=pickle.load(open('finalized_model3.pkl','rb'))
model4=pickle.load(open('finalized_model2.pkl','rb'))
model5=pickle.load(open('finalized_model1.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict1',methods=['GET','POST'])
def predict1():
    if request.method=='POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])
        #prediction=np.sum(final_features)
        #final_features[final_features<=0]=1
        #final_features=[np.log(final_features)]
        prediction = model1.predict(final_features)
        if(prediction==1):
            prediction='Yes'
        else:
            prediction='No'
        return render_template('index1.html', prediction_text='Is company prone to bankrupt? : {}'.format(prediction))
    return render_template('index1.html')

@app.route('/predict2',methods=['GET','POST'])
def predict2():
    if request.method=='POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])
        #prediction=np.sum(final_features)
        #final_features[final_features<=0]=1
        #final_features=[np.log(final_features)]
        prediction = model2.predict(final_features)
        if(prediction==1):
            prediction='Yes'
        else:
            prediction='No'
        return render_template('index2.html', prediction_text='Is company prone to bankrupt? : {}'.format(prediction))
    return render_template('index2.html')

@app.route('/predict3',methods=['GET','POST'])
def predict3():
    if request.method=='POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])
        #prediction=np.sum(final_features)
        #final_features[final_features<=0]=1
        #final_features=[np.log(final_features)]
        prediction = model3.predict(final_features)
        if(prediction==1):
            prediction='Yes'
        else:
            prediction='No'
        return render_template('index3.html', prediction_text='Is company prone to bankrupt? : {}'.format(prediction))
    return render_template('index3.html')

@app.route('/predict4',methods=['GET','POST'])
def predict4():
    if request.method=='POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])
        #prediction=np.sum(final_features)
        #final_features[final_features<=0]=1
        #final_features=[np.log(final_features)]
        prediction = model4.predict(final_features)
        if(prediction==1):
            prediction='Yes'
        else:
            prediction='No'
        return render_template('index4.html', prediction_text='Is company prone to bankrupt? : {}'.format(prediction))
    return render_template('index4.html')

@app.route('/predict5',methods=['GET','POST'])
def predict5():
    if request.method=='POST':
        int_features = [float(x) for x in request.form.values()]
        final_features = np.array([int_features])
        #prediction=np.sum(final_features)
        #final_features[final_features<=0]=1--------
        #final_features=[np.log(final_features)]   !------->these two lines of codes we will use if we require transformation
        prediction = model5.predict(final_features)
        if(prediction==1):
            prediction='Yes'
        else:
            prediction='No'
        return render_template('index5.html', prediction_text='Is company prone to bankrupt? : {}'.format(prediction))
    return render_template('index5.html')

if __name__ == "__main__":
    app.run(debug=True)
