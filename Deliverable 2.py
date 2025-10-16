#LIA deliverable 2
#Names: Eva G Melki, Rabail Saqib, Eva M Sorge
#Description: loading datasets for data analysis and plotting graphs


#Part 1: Load dataset using Pandas

import pandas as pd

data = pd.read_csv('obesity_data.csv')
print(data)

#Accessing individual columns:

age = data['Age']
gender = data['Gender']
height = data['Height']
weight = data['Weight']
BMI = data['BMI']
activity_level = data['PhysicalActivityLevel']
obesity_category = data['ObesityCategory']

#Convert to NumPy arrays:
    
age_array = age.to_numpy()
gender_array = gender.to_numpy()
height_array = height.to_numpy()
weight_array = weight.to_numpy()
BMI_array = BMI.to_numpy()
activity_level_array = activity_level.to_numpy()
obesity_category_array = obesity_category.to_numpy()
#All dataset categories are now saved as NumPy arrays, ready to be used to plot graphs

#Rounding data:

data['Height'] = data['Height'].round(3)
data['Weight'] = data['Weight'].round(3)
data['BMI'] = data['BMI'].round(3)
print(data)
