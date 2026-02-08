# for loop
data=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
'''
for x in data:
    if x%2==0:
        print(x)'''

'''for data in range(1,11):
    print(data)'''

'''for index, value in enumerate(data):
    if value%2==0:
        print(index, value)'''

for index, value in enumerate(range(1,11), start=1):
    data=[]
    if value%2==0:

        print(index, value)