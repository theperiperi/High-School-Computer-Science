#file_object.seek(offset[reference_point])
#offset is the number of bytes by which the file object is to be moved
#reference point indicates the starting position of the file object,
#that is with reference to which position, the offset has to be counted.

#0 indicates beginning of file
#1 indicates current of file

#by default value of reference point is 0

#position source specified is the byte position from the beginning of the file
#to the current position of the file object

# Program to write and read employee records in a binary file
import pickle
print("WORKING WITH BINARY FILES")
bfile=open("empfile.dat","ab")
recno=1
print ("Enter Records of Employees")
print()
#taking data from user and dumping in the file as list object
while True:
    print("RECORD No.", recno)
    eno=int(input("\tEmployee number : "))
    ename=input("\tEmployee Name : ")
    ebasic=int(input("\tBasic Salary : "))
    allow=int(input("\tAllowances : "))
    totsal=ebasic+allow
    print("\tTOTAL SALARY : ", to


#fileObject.seek(5,0)
#This function returns an integer that specifies the
#current position of the file object in the file. The position
#so specified is the byte position from the beginning of
#the file till the current position of the file object. The
#syntax of using tell() is:
#file_object.tell()
