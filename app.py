from flask import  Flask, render_template,request
import pickle



from sklearn.linear_model import LinearRegression

with open('D:\SUSHMITHA\Dataframes_csvFiles\reg_pickle','rb') as f:
    mp=pickle.load(f)

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',method=['POST'])
def predict():
    if request.method=='POST':
        cylinders=request.form('cylinders')
        displacement=request.form('displacement')
        horsepower=request.form('horsepower')
        weight=request.form('weight')
        modelyear=request.form('modelyear')
        origin=request.form('origin')

        data=[[float(cylinders),float(displacement),float(horsepower),float(weight),float(modelyear),float(origin)]]
        lr=pickel.load(open('D:\SUSHMITHA\Dataframes_csvFiles\reg_pickle','rb'))
        prediction=lr.predict(data)

    return render_template('index.html',prediction=prediction)   



if __name__=='__main__':
    app.run(debug=True)