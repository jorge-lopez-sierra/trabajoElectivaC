import pandas as pd
import numpy as np
import sklearn
import joblib
form flask import Flask,render_template,request
app=Flask(_name_)

@app.route(´/´)
def index():
    return render_template('index.html')

@app.route('/prediccion',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        try:
            var_1=float(request.form['var_1'])
            var_2=float(request.form['var_2'])

            pred_args=[var_1,var_2]
            pred_arr=np.array(pred_args)
            preds=pred_arr.reshape(1,-1)
            modelo=open(´./Modelo.pkl','rb')
            prediccion_modelo=modelo_clas.predict(preds)
            prediccion_modelo=round(float(prediccion_modelo),2)
            if prediccion_modelo == 1.0:
                prediccion_modelo = "Aprueba"
            else:
                prediccion_modelo = "No aprueba"
            except ValueError:
                return "Por favor entra nombre validos"
            return render_template('prediccion.html',prediccion=prediccion_modelo)
if _name_=='__main__':
    app.run(debug=True)
