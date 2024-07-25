from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np



# loading saved model
model=pickle.load(open("decision_tree_model.pkl","rb"))

app=Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')




@app.route("/prediction",methods=['GET','POST'])
def pred():
    pred={1.0:"None",2.0:"Sleep_apnea",0.0:"Insomnia"}
    if request.method == 'POST':
        gender = request.form.get('Gender')
        if gender == "Male":
            gender = 1
        else:
            gender = 0
        odict = {"Software Engineer":9,"Doctor":1,"Sales Representative":6,"Teacher":10,"Nurse":5,"Engineer":2,"Accountant":0,"Scientist":8,"Lawyer":3,"Salesperson":7,"Manager":4}
        bdict= {"Overweight":3,"Normal":0,"NormalWeight":1,"Obese":2}
        data = pd.DataFrame({
            'Gender':gender,
            'Age':request.form.get('Age'),
            'Occupation':odict[request.form.get('Occupation')],
            'Sleep Duration':request.form.get('Sleep_Duration'),
            'Quality of Sleep':request.form.get('Quality_of_Sleep'),
            'Physical Activity Level':request.form.get('physical_activity'),
            'Stress Level':request.form.get('Stress_level'),
            'BMI Category':bdict[request.form.get('BMI_Category')],
            'Heart Rate':request.form.get('Heart_Rate'),
            'Daily Steps':request.form.get('Daily_Steps'),
            'systolic_bp':request.form.get('Systolic_bp'),
            'diastolic_bp':request.form.get('Diastolic_bp'),
        },index=[0])
        prediction = model.predict(data)
        print(type(prediction[0]))
        print(prediction[0])
        return render_template('pred_form.html',prediction = pred[prediction[0]])

    return render_template('pred_form.html')






if __name__== '__main__':
    app.run()

