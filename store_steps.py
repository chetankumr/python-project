def thing():
    print('hello')
    print('fun')
thing()
thing()
print('zip')
thing()
print(exit)

def greet():
    print('Good morning, my name is chetan')
    print('how are you?')
greet()

greet()
thing()
print('how are you?')
print('from where are you?')
print('how can i help you?')
count=0
for number in (10,15,30):
    count= count+1
print(count)
total=0
for number in (5,10,15):
    total=total+number
print(total)
largest = None
for number in (5,10,30,60,80):
    if largest is None or number> largest:
        largest= number
print(largest)

smallest= None
for number in (1,2,5,6,78,89,-9):
    if smallest is None or number<smallest:
        smallest= number
print (smallest)

total=0
count=0
for number in (5,10,15,20):
    total=total+number
    count=count+1

average= total/count
print(total)
print(count)
print(average)

for number in(5,10,15,20,56,78,89,100):
    if number >= 100:
       print(number)
    
for number in (1,2,3,4,5,6,7,8,9,10) :
    if number %2 ==0 and number>6:
        print (number)   
found = False
for number in (10,15,20,45,):
    if number >30:
        found= False
print(found)
raining = True
if raining:
    print("plan canel")
else:
    print("game on")
found=False
print('Before',found)
for value in (9,41,56,3,74,15):
    if value==3:
        found= True
    print(found, value)
print('after',found)