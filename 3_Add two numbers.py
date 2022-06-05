#Shivam is the youngest programmer in the world, he is just 12 years old.
#  Shivam is learning programming and today he is writing his first program.
#The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

T = int(input())
for tc in range (T):
    a,b=map(int, input().split())
    ans = a+b
    print(a+b)