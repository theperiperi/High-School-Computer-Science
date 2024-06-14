import pickle
import sys
dict={}
#function to write
def write_in_file():
    file=open('stud2.dat','ab')
    no=int(input('enter number of students:'))
    for i in range(no):
        print('enter details of student',i+1)
        dict['roll']=int(input('enter roll number:'))
        dict['name']=input('enter name:')
        dict['marks']=int(input('enter marks:'))
        pickle.dump(dict,file) #dump to write in student file
    file.close()
#function to display
def display():
    #read from file and display
    file=open('stud2.dat','rb')
    try:
        while True:
            stud=pickle.load(file)
            print(stud)
        except EOFError:
            pass
        file.close()

#main program
        while True:
            print('MENU \n 1-write in a file \n 2-display')


#not yet done
