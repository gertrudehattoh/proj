
import pandas as pd

df = pd.DataFrame({'name' : ['Ama', 'Kojo', 'Qwame', 'Efua', 'Jerry', 'Divine', 'Freedom', 'Mabel'], 'age' : [12,34,45,67,34,34,34,77], 
'height' : [12,34,34,23,34,34,34,56], 'weight' : [234,345,456,456,789,567,879,897]})

print(df)

# adding a new list to my DataFrame 
#declaring list
colour = ['Red','Pink', 'Yellow', 'Indigo', 'Green', 'Blue', 'BLack', 'Brown']

#using 'Colour' as column name
#equating 'colour' = colour
df['Colour'] = colour




#insert a new column as 'other name' at index 1

new_df = df.assign('other name' : ['Adjei', 'Baah', 'Coffie', 'Nyameye', 'Buaba', 'Alovor', 'Agbemafle', 'Atta-Mills'])

print(new_df)