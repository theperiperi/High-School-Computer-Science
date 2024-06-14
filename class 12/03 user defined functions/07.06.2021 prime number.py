#check whether prime or not
n=int(input('enter integer'))
def prime():
    i=2
    if i<n:
        if n%i==0:
            print('composite')
        if n%i!=0:
            i+=1
            if n==i:
                print('prime')
prime()
#small problem
