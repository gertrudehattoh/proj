import pandas as pd

new = 'the students are studying for their exams'
new1 = new.split()

print(new1)

df = pd.DataFrame(new1)
print(df)





#the data set of students at KNUST
data = {'name' : ['Kofi', 'Ama', 'Qwame', 'Maame'],
'course': ['biological sciences', 'Physics', 'Chemistry', 'maths'], 'age' : [21, 20, 19, 20] }

print(data)

#select all the columns
my_data = pd.DataFrame(data,)

print(my_data)  





data = {'car' :['Ford', 'Volvo'], 'speed' : [234,567]}
data1 = pd.DataFrame(data)

print(data1)

#declare list that is to be converted into a dataframe
address = ['Ayeduase', 'Kotei']

#adding the address variable to the DataFrame 
# using address as the column name
data1['Address'] = address

print(data1)

#inserting a new column at a position of choice
data2 = data1.insert(2,'Distance',[34,34],True)

print(data2)









