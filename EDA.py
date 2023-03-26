#import pandas as pd
#(n%2)==0
#if (n+1)%2 != 0:
 # print('weird')
  #[n for n in range (3,5) if (n%2)==0]
#print('not weird')
#elif:
 # print('nice') 
  
#matrix= [[1, 4, 9], [1, 8, 27], [1, 16, 81]]
#matrix[3][0]
#print(matrix)  

#dog = ['Freddie', 9, True, 1.1, 2001, ['bone', 'little ball']]
#dog[5][0]
#print(dog[5][0])
#print([5][1])

test = [{'Arizona': 'Phoenix', 'California': 'Sacramento', 'Hawaii': 'Honolulu'},
1000,
2000,
3000,
['hat', 't-shirt', 'jeans', {'socks1': 'red', 'socks2': 'blue'}]]
print(test[2])
print(test[0])
print(test[4])
print(test[0]['Arizona'])
print(test[4][2])
print(test[4][3]['socks2'])

n = input('type a number' )

if n%2==1:
  print('Weird')
if n in range(2,5) and n%2==0:
  print('Not Weird')
if n in range(5,21) and n%2==0:
  print('weird')
if n>20 and n%2==0:
  print('Not Weird')



