x = 5
if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else:
    print('Large')
print('all done')
print('10/2')
try:
    print(10/2)
except:
    print("Error")
try:
    print(10/0)
except:
    print("Error")
try:
    x = int("100")
    print(x)
except:
    print("Error")
try:
    x= int("hello")
    print(x)
except:
    print('inavlid')
name = input("enter your age")
try:
    age = int(name)
    print("next year you will be ", age+1)
except:
    print('please enter a valid age')
print("all done")
astr = "hello bob"
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr= -1
print('second',istr)

pip install streamlit


