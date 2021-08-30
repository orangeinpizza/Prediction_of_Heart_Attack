from flask import Flask, render_template, request
#import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd

df=pd.read_csv('Heart_Data.csv')
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
sc=StandardScaler()
X=sc.fit_transform(X)

#model=tf.keras.models.load_model('ANN_Model.h5')

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/sub",methods=["POST"])
def submit():
    if request.method=='POST':
        n1=request.form['age']
        n2=request.form['anaemia']
        n3=request.form['creatinine_phosphokinase']
        n4=request.form['diabetes']
        n5=request.form['ejection_fraction']
        n6=request.form['high_blood_pressure']
        n7=request.form['platelets']
        n8=request.form['serum_creatinine']
        n9=request.form['serum_sodium']
        n10=request.form['sex']
        n11=request.form['smoking']
        n12=request.form['time']

    #x=model.predict(sc.transform([[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12]]))
    x=0.5
    if x>0.35:
        x=1
    else:
        x=0    
    return render_template('sub.html',n=x)    

if __name__=="__main__":
    app.run(debug=True)
