print('learning to move the file object')
fileobject=open('testfile.txt','r+')
#open in read or write mode
#rb+ means read or write for binary files
str=fileobject.read()
print('initial pos of file is:',fileobject.tell())
fileobject.seek(0)
print('now the file object is at the beginning of the file',fileobject.tell())
fileobject.seek(5)
print('we are moving to 10th byte of brogram')
print('the position of the file object is at',fileobject.tell())
str=fileobject.read()
print(str)

f=open('demofile.txt','r')
f.seek(4)
print(f.readline())
