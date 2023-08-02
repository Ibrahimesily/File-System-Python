#******************************** Write Function *********************************************************************************************
def Write_Student():
    with open('studentpy.txt' , 'a') as file :
        c = 'y'
        while c == 'y':
            name = input('Enter The Student Name : ')
            id = input('Enter The Student ID : ')  
            age = input('Enter The Student Age : ')
            Academic_Year = input('Enter The Student Academic Year : ')
            phone_Number = input('Enter The Student Phone Number : ')
            Gender = input('Enter The Student Gender : ')
            Recedent = input('Enter The Student Recedent : ')
            file.write(  name + '\t' + id + '\t' + age + '\t' + Academic_Year + '\t' + phone_Number + '\t' + Gender + '\t' + Recedent + '\n' )
            print('----------------------------------------------------------------------------- ')
            c = input('Do You Want To Enter Another Record ( y / n ) ? : ')
            print('----------------------------------------------------------------------------- ')
        print('File Saved Successfully')
        print('----------------------------------------------------------------------------- ')
    
#********************************* Read Function *********************************************************************************************
def Read_Student() :
    with open('studentpy.txt' , 'r') as file :
        print('Name\tID\tAge\tYear\tphone Number\tGender\tRecedent')
        print('----------------------------------------------------------------------------- ')
        for line in file :
            print(line , end='')
        print('\n')     

#********************************* Search Function *******************************************************************************************
def Search_Student() :
    name = input('Enter The Name Of The Student To Search For : ')
    with open('studentpy.txt' , 'r') as file :
        flag = False
        for line in file :
            fields = line.split('\t')
            if fields[0] == name :
                flag = True
                print('Name\t ID\tAge\tAcademic Year\tphone Number\tGender\t  Recedent')
                print('----------------------------------------------------------------------------- ')
                print(line , end='')
                print('----------------------------------------------------------------------------- ')
        if not flag :
            print('Student Not Found')
            print('----------------------------------------------------------------------------- ')
            
#********************************* Delete Function ********************************************************************************************
def Delete_Student() :
    import os
    file     = open('studentpy.txt' , 'r')
    tempfile = open('tempstudentpy.txt' , 'w')
    name     = input('Enter The Name Of The Student To Delete : ')
    flag     = False
    for line in file :
        st = line.split('\t')
        if st[0] == name :
            flag = True
        else :
            tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('studentpy.txt')
    os.rename('tempstudentpy.txt' , 'studentpy.txt' )
    
    if not flag :
        print('Student Not Found')
        print('----------------------------------------------------------------------------- ')        
    else :
        print('Student Deleted Successfully')
        print('----------------------------------------------------------------------------- ')

 #********************************* Update Function ********************************************************************************************
def Update_Student() :
    import os
    file     = open('studentpy.txt' , 'r')
    tempfile = open('tempstudentpy.txt' , 'w')
    name     = input('Enter The Name Of The Student To Update : ')
    flag     = False
    for line in file :
        st = line.split('\t')
        
        if st[0] == name :
            flag = True
            age            = input('Enter The New Age for The Student : ')
            academic_year  = input('Enter The New Academic Year for The Student : ')
            recedent       = input('Enter The New Recedent for The Student : ')
            line           = st[0] + '\t' + st[1] + '\t' + age + '\t' + academic_year + '\t' + st[4] + '\t' + st[5] + '\t' + recedent + '\n'  
        tempfile.write(line)
        
    file.close()
    tempfile.close()
    os.remove('studentpy.txt')
    os.rename('tempstudentpy.txt' , 'studentpy.txt' )
    
    if not flag :
        print('Student Not Found')
        print('----------------------------------------------------------------------------- ')        
    else :
        print('Student Deleted Successfully')
        print('----------------------------------------------------------------------------- ')    
    
 #********************************* Home Function ********************************************************************************************
def Home():
    ch = 'y'
    while ch == 'y':
        print('1 - Add New Student .')
        print('2 - Read All Students .')
        print('3 - Search For a Student .')
        print('4 - Delete a Student .')
        print('5 - Update Student Records .')
        print('----------------------------------------------------------------------------- ')
        ch = input('Please Enter Your Choise : ')
        print('----------------------------------------------------------------------------- ')
        if ch == '1' :
            Write_Student()
        elif ch == '2' :
            Read_Student()
        elif ch == '3' :
            Search_Student()
        elif ch == '4' :
            Delete_Student()
        elif ch == '5' :
            Update_Student()
        print('----------------------------------------------------------------------------- ')    
        ch = input('Do You Want To Perform Another Operation (y/n) : ')
        print('----------------------------------------------------------------------------- ')
Home()    

 #*******************************************************************************************************************************************    
