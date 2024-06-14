#sections and streams

data=0
s=[]
c='y'

while c=='y':
    option=input('push or pop or stop')

    if option=='push':
        def push(data):
            a=input('stream')
            b=input('sections')
            data=a+' '+b
            s.append(data)
        push(data)
        l=len(s)
        for i in range(0,l):
            print('now the queue is',s[i])

    if option=='pop':
        def pop(data):
            if s==[]:
                print('queue is empty')
            else:
                print('the deleted element is',s.pop(l-1))
        pop(data)
        l=len(s)
        for i in range(0,l):
            print('now the queue is',s[i])
