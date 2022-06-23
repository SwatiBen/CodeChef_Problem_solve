#In ChefLand, human brain speed is measured in bits per second (bps). 
# Chef has a threshold limit of X bits per second above which his calculations are prone to errors. 
# If Chef is currently working at Y bits per second, is he prone to errors?
#If Chef is prone to errors print YES, otherwise print NO.

#Input Format
# The only line of input contains two space separated integers X and Y — the threshold limit and the rate at which 
# Chef is currently working at.

X,Y=map(int,input().split())
if(Y>X):
    print("YES")
else:
    print("NO")