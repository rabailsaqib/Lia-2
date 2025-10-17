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

#Part 4: Plotting your data 

import matplotlib.pyplot as plt
import pandas as pd

# 1 )plot of any type containing data from more than 1 array using different colors and line styles.
# This graph compares BMI and Weight against Age using different colors and line styles
sorted_data = data.sort_values(by="Age")
plt.plot(sorted_data["Age"], sorted_data["BMI"], color="pink", linestyle="-", label="BMI vs Age")
plt.plot(sorted_data["Age"], sorted_data["Weight"], color="black", linestyle="--", label="Weight vs Age")
plt.title("Comparison: BMI and Weight by Age")
plt.xlabel("Age")
plt.ylabel("Value")
plt.legend()
plt.show()

# 2 )1 plot of any type using grid ( scatter plot )
# / Scatter plot of Weight vs BMI to show distribution of BMI at different weights
plt.scatter(filtered_data["Weight"], filtered_data["BMI"], color="green")
plt.title("BMI vs Weight (with grid)")
plt.xlabel("Weight (kg)")
plt.ylabel("BMI")
plt.grid(True) 
plt.show()

# 3 )1 plot of any type containing 2 subplots side by side (counts as 1)
# (Histogram of Height and Weight distributions in the dataset)

#Histogram of Weight distribution in the dataset
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(height_array, color='purple')
plt.title( "Height Distribution" )
plt.xlabel("Height")
plt.ylabel( "Count")
# ( Histogram of Weight distribution in the dataset)
plt.subplot(1,2,2)
plt.hist(weight_array, color='yellow')
plt.title("Weight Distribution")
plt.xlabel("Weight")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#4 )1 scatter plot (withought the grid) / Weight vs BMI
plt.scatter(weight_array, BMI_array, color='red')
plt.title("BMI vs Weight")
plt.xlabel("Weight")
plt.ylabel("BMI")
plt.show()

#5 )1 bar plot
#Count of people in each Physical Activity Level category
activity_counts = data['PhysicalActivityLevel'].value_counts()
plt.bar(activity_counts.index, activity_counts.values, color='lightblue')
plt.title("Count of physical activity Level ")
plt.xlabel("Activity Level")
plt.ylabel("Amount Of People")
plt.xticks(rotation=45)
plt.show()

#6 )1 histogram
# This histogram shows the frequency of BMI values
plt.hist(data["BMI"], bins=20, color="#DB7093")
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()


#7 )1 pie chart
# Gender distribution for the pie chart
gender_counts = data["Gender"].value_counts()
labels = gender_counts.index
y = gender_counts.values
colors = ["blue", "red"]

plt.title("Gender Distribution in Dataset")
plt.pie(y, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
plt.show()

