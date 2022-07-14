INPUT = int(input())
n=1000-INPUT
count = 0

coin_types = [500, 100, 50, 10,5,1]

for i in coin_types:
    count+=n//i
    n=n%i

print(count)