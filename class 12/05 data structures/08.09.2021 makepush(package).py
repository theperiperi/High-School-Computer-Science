package=[]

def makepush(package):
    a=int(input('enter package title'))
    package.append(a)
    
def makepop(package):
    if(package==[]):
        print('stack is empty')
    else:
        print('deleted element is',package.pop())

makepush(package)
makepop(package)
