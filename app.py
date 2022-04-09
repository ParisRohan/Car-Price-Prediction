from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('carprice_xgb.pkl', 'rb'))
print("Model Loaded")
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():     
    
    if request.method == 'POST':
        
        #Car average mileage
        mileage_number = int(request.form['mileage_number'])
        
        #Total km driven by the vehicle
        km_driven = int(request.form['km_driven'])
#        Kms_Driven2=np.log(Kms_Driven)
 
        #Torque
        torque = int(request.form['torque'])       
            
        #seats
        seats = int(request.form['seats'])  
        
        #engine_op_number
        engine_op_number = int(request.form['engine_op_number'])  
        
        #max_power_number
        max_power_number = int(request.form['max_power_number'])  
        
        #Year in which the vehicle was bought
        year = int(request.form['year'])
        Car_age = 2022 - year
                
        #Vehicle owner
        owner=request.form['owner']
        if(owner=='Fourth & Above Owner'):
            owner=2
        elif(owner=='Third Owner'):
            owner=3
        elif(owner=='Second Owner'):
            owner=4
        elif(owner=='First Owner'):
            owner=5
        else:
            owner=0

        #Fuel type
        fuel=request.form['fuel']
        if (fuel=='Diesel'):
            fuel_Diesel=1
            fuel_Petrol=0
            fuel_LPG=0
        elif(fuel=='Petrol'):
            fuel_Diesel=0
            fuel_Petrol=1
            fuel_LPG=0
        elif(fuel=='LPG'):
            fuel_Diesel=0
            fuel_Petrol=0
            fuel_LPG=1
        else:         
            fuel_Diesel=0
            fuel_Petrol=0
            fuel_LPG=0

        #Seller type
        seller_type=request.form['seller_type']
        if(seller_type=='Individual'):
            seller_type_Individual=1
            seller_type_Trustmark_Dealer=0
           
        elif(seller_type=='Trustmark_Dealer'):
            seller_type_Individual=0
            seller_type_Trustmark_Dealer=1
           
        else:
            seller_type_Individual=0
            seller_type_Trustmark_Dealer=0
            
         
        #Engine transmission
        transmission_Manual=request.form['transmission_Manual']
        if(transmission_Manual=='Manual'):
            transmission_Manual=1
        else:
            transmission_Manual=0
        
        #Feature Transformation
        torque_log=np.log(torque)
        engine_op_number_sqaure=engine_op_number**(1/2)
        max_power_number_sqaure=max_power_number**(1/2)
        km_driven_sqaure=km_driven**(1/2)
        Car_age_log=np.log(Car_age)
        
        model_input=[mileage_number, km_driven_sqaure, torque_log, seats, engine_op_number_sqaure, max_power_number_sqaure,
                       Car_age_log, owner, fuel_Diesel, fuel_LPG, fuel_Petrol, seller_type_Individual,seller_type_Trustmark_Dealer, transmission_Manual]
            
        np_array=np.asarray(model_input)
        model_input=np_array.reshape(1,-1)
        
        prediction=model.predict(model_input)
    
        #output=round(prediction[0],2)
        output=np.exp(prediction)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at Rs. {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

