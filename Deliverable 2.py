#LIA deliverable 2
#Names: Eva G Melki, Rabail Saqib, Eva M Sorge
#Description: loading datasets for data analysis and plotting graphs


#Part 1: Load dataset using Pandas

import pandas as pd

data = pd.read_csv('obesity_data.csv')

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

#Part 2: Filtering Data

#Filtering Data to keep dataset at 500 items (or indexes):
    
filtered_data = []
filtered_index= []

for i in range(len(data)):
    if i <= 500:
        filtered_index.append(i)
      
filtered_data=data.iloc[filtered_index]
print(filtered_data)

#Creating separate tables for males and females

filtered_females = []
filtered_males = []

for i, row in filtered_data.iterrows():
    if row["Gender"] == "Male":
        filtered_males.append(i)
    else:
        filtered_females.append(i)
        
filtered_males=data.iloc[filtered_males]
filtered_females=data.iloc[filtered_females]

print(filtered_males)        
print(filtered_females)


# part 3 : Manipulating your data

#Description: # This part will remove any data that looks unrealistic
# We will calculate BMI = weight / (height * height) and values between 10 and 60 (normal human range )

filtered_weight = []
filtered_height = []
filtered_BMI = []
filtered_age = []
filtered_gender = []
filtered_activity = []
filtered_obesity = []

for i in range(len(BMI_array)) :
    if 10 <= BMI_array[i] <= 60:
        
        filtered_weight.append(weight_array[i])
        filtered_height.append(height_array[i])
        filtered_BMI.append(BMI_array[i])
        filtered_age.append(age_array[i])
        filtered_gender.append(gender_array[i])
        filtered_activity.append(activity_level_array[i])
        filtered_obesity.append(obesity_category_array[i])
        
# converting them back to numpy arrays

import numpy as np

weight_array = np.array(filtered_weight)
height_array = np.array(filtered_height)
BMI_array = np.array(filtered_BMI)
age_array = np.array(filtered_age)
gender_array = np.array(filtered_gender)
activity_level_array = np.array(filtered_activity)
obesity_category_array = np.array(filtered_obesity)
print("Filtered dataset ( realistic BMI values only ):")  
print(BMI_array)     
        