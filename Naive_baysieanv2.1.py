'''Name: NAMAN MADHARIA
'''

#giving sample input

weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Weather: ",weather_encoded)
print ("Temp:",temp_encoded)
print ("Play:",label)

'''output
Weather: [2 2 0 1 1 1 0 2 2 1 2 0 0 1]
2 -> Sunny
0 -> Overcast
1 -> Rainy

Temp: [1 1 1 2 0 0 0 2 0 2 2 2 1 2]
1 -> Hot
2 -> Mild
0 -> Cool

Play: [0 0 1 1 1 0 1 0 1 1 1 1 1 0]
0 -> No
1 -> Yes
'''


#Combinig weather and temp into single listof tuples
features=list(zip(weather_encoded,temp_encoded))
print(features)
#[(2, 1), (2, 1), (0, 1), (1, 2), (1, 0), (1, 0), (0, 0), (2, 2), (2, 0), (1, 2), (2, 2), (0, 2), (0, 1), (1, 2)]
#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label)

#Predict Output
weather_input=int(input("enter weather: \n 2 for Sunny\n0 for Overcast\n1 -> Rainy\n"))
temp_input=int(input("enter temperature: \n1 for Hot\n2 for Mild\n0 for Cool\n"))
predicted= model.predict([[weather_input,temp_input]]) 
#print("Predicted Value:", predicted)
if (predicted==1):
	print("Yes the children will play")
else:
	print("No the children will not play")


