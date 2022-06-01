# x, y = map(float,input().split())
# #that means if the input is 30 and 120. By using map method, input wil get stored as x=30.0, y=120.0
# #where float is datatype of input variables. split() method helps us to separate the input
x , y = map(float,input().split())
if( x%5 == 0 and x+0.50<=y):
     y-= x+0.50
print(y)     