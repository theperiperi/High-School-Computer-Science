f=open('06.29.2021 test1.txt')
print(f.name)
print(f.mode)
print(f.readable())
print(f.closed)
f.close()
print(f.closed)