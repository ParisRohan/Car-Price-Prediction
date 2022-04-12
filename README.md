# Car-Price-Prediction
A supervised ML project on predicting the selling price of used vehicles by using the cardekho.com Kaggle dataset. The model is trained using XGBoost regressor algorithm.
The app is deployed using Heroku.

# Website link: https://rohan-car-price-prediction.herokuapp.com/

# Tech Stack:
* Front-End: HTML, CSS
* Back-End: Flask
* IDE: Jupyter notebook, Spyder

# How to run the app
1. Create a virtual environment using following command:
   * **_conda create -n <your environment name> python=3.7_**
2. Activate the created environment
   * **_activate <your environment name>_**
3. Navigate to the directory where you wish to install the packages 
4. Install the required packages using
   * **_pip install -r requirements.txt_**
5. Run the app using
   * **_python app.py_**
 
# Screenshots 
![image](https://user-images.githubusercontent.com/49038495/163014441-8e8e0482-9d6d-4561-8a29-dc3cc340741f.png)
![image](https://user-images.githubusercontent.com/49038495/163014684-154a0e55-46df-4848-8b34-e287170c6e0a.png)

**Prediction output:**
![image](https://user-images.githubusercontent.com/49038495/163014998-cf96ffa0-52da-4cd0-a49f-4a778530b03d.png)

# Workflow

## 1. Data Collection
  The dataset can be found from following Kaggle site-
  https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho
  
## 2. Data Preprocessing
  * Split the categorical features to obtain desired numerical features like mileage_number, engine_op_number, max_power_number, torque
  * Impute mean value of feature for missing numerical features
  * Impute mode value of feature for missing categorical features
  * Handle outliers using Interquartile range (IQR) and boxplots
  * Transform features to get the features in normal distribution curve using following Feature Transformation techniques and Probability distribution graph-
    ** log transformation, Reciprocal transformation, Square root transformation, Exponential transformation
  * Perform Ordinal encoding on 'owner' feature and One hot encoding on remaining categorical features
  
## 3. Model Building
  * Build a model after experimenting with different algrithms and evaluate their performance using different metrics
  
## 4. Deployment
  The model is deployed using Flask and Heroku
  Please refer to the following blog on how to deploy a model using Heroku:-
  https://parisrohan.medium.com/how-to-deploy-an-application-using-heroku-94a2fbeac08c
  
  
  
 
