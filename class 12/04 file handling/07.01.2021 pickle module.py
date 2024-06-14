#pickle module
#program to write list sequence in a binary file
def foperation():
    import pickle
    list1=[10,20,30,40,100]
    f=open('07.01.2021.dat','wb')
    #.dat:data file, 'wb':write mode,binary file
    pickle.dump(list1,f)#writing contents to binary file
    print('file added to the binary file')
    f.close()
foperation()
