# Step 1: Importing libraries 
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures

# Step 2: Defining the columns and reading the DataFrame 
df = pd.read_csv('2023/kum-cebulova-dolina.csv')
print (df)

exit()

# Step 3: Seperating the data into features and labels
X = df[['datum']]
y = df['vhodi']

# Step 4: Generating polynomial features 
Z = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X)
# Dividing the dataset into test and train data
X_train, X_test, y_train, y_test = train_test_split(Z, y, test_size=0.3, random_state=10)

# Step 5: Selecting the linear regression method from the scikit-learn library
model = LinearRegression().fit(X_train, y_train)

# Step 6: Validation
# Evaluating the trained model on training data
y_prediction = model.predict(X_train)
print("MAE on train data= " , metrics.mean_absolute_error(y_train, y_prediction))
# Evaluating our trained model on test data
y_prediction = model.predict(X_test)
print("MAE on test data = " , metrics.mean_absolute_error(y_test, y_prediction))