# x, y = map(float,input().split())
# #that means if the input is 30 and 120. By using map method, input wil get stored as x=30.0, y=120.0
# #where float is datatype of input variables. split() method helps us to separate the input
# x , y = map(float,input().split())
# if( x%5 == 0 and x+0.50<=y):
#      y-= x+0.50
# print(y)     
x, y = map(float, input().split()) # space is a must after ',' and before 'input'
if(x%5==0 and x<y):
    d=y-(x+0.5)
    print("%.2f"%d)
elif(x%5!=0):
    print("%.2f"%y)
else:
    print("%.2f"%y)