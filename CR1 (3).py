n = int(input())

r1=n/3-n//3
r2=n/5-n//5
r3=n/7-n//7
m1=r1==0
m2=r2==0
m3=r3==0
print(f'Is {n} a multiple of 3? {m1}')
print(f'Is {n} a multiple of 5? {m2}')
print(f'Is {n} a multiple of 7? {m3}')