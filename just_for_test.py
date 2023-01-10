a=str((1,2))
b=str((11,33))
print(a,b)
a= a.split(',')
print(a[0][a[0].index('(')+1:], a[1][:a[1].index(')')])

