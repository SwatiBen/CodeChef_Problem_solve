x, y = map(float, input().split()) # space is a must after ',' and before 'input'
if(x%5==0 and x<y):
    d=y-(x+0.5)
    print("%.2f"%d)
elif(x%5!=0):
    print("%.2f"%y)
else:
    print("%.2f"%y)
