x, y = map(float, input().split())

if(x%5==0 and x<y):
    d=y-(x+0.5)
    print("%.2f"%d)
    
elif(x%5!=0):
    print("%.2f"%y)
    
else:
    print("%.2f"%y)
