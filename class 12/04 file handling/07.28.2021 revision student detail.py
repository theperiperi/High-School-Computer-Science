#student details revision
import pickle
#function definition
def write_details():
    lst=[]
    while True:
        r=int(input("Enter roll "))
        n=input("Enter name ")
        p=float(input("Enter per "))
        d=str(r)+' '+n+' '+str(p)
        lst.append(d)
        ch=input("Like to add more student records (y/n) ")
        if(ch=='y' or ch=='Y'):
            continue
        else:
            break
    fp=open("rstudentrevision.csv","wb")
    pickle.dump(lst,fp)
    print("Names written in the file")
    fp.close()
write_details()
