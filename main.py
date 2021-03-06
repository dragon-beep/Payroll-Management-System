import mysql.connector as con
obj=con.connect(host='localhost',user='root',password='',database='project')
cur=obj.cursor()
#creating tables
def create():
    t1="create table payroll(empid char(5) primary key,firstname char(20),lastname char(20),gender char(5),date_of_birth date, date_of_joining date,address char(35),basic_salary float,designation char(30))"
    cur.execute(t1)
#inserting data into tables
def insert():
    fn=input('enter firstname')
    ln=input('enter lastname')
    ge=input('enter gender(F/M)')
    d1=input('enter date of birth in YYYY:MM:DD format')
    d2=input('enter date of joining in YYYY:MM:DD format')
    add=input('enter address')
    bsal=float(input('enter salary per annum'))
    desig=input('enter designation (i.e. from manager, clerk, general manager, president)')
    t="select * from payroll"
    cur.execute(t)
    p=cur.fetchall()
    a='00'+str(cur.rowcount+1)
    i="E"
    a=i+a
    t1="insert into payroll values('{}','{}','{}','{}','{}','{}','{}',{},'{}')".format(a,fn,ln,ge,d1,d2,add, bsal,desig)
    cur.execute(t1)
    obj.commit()
    print('record entered successfuly')#display records for given name
def search_by_name():
    fn=input('enter firstname of employee')
    ln=input('enter last name of employee')
    t="select * from payroll where firstname='{}' and lastname='{}'".format(fn,ln)
    cur.execute(t)
    data=cur.fetchall()
    if data==None:
        print('no data')
    else:
        print("empid","firstname","lastname","gender","date of birth","date of joining","address","basic_salary","designation")
        for x in data:
            print(x)
#displaying all employees
def displayemp():
    t="select * from payroll"
    cur.execute(t)
    data=cur.fetchall()
    if data==None:
        print('empty database')
    else:
        print("empid","firstname","lastname","gender","date of birth","date of joining","address","basic_ salary","designation")
        for x in data:
            print(x)
#modifying records
def modify():
    def modifyname():#modifying name of record
        eid=input('enter empid for which name is to be updated')
        fn=input('enter new firstname')
        ln=input('enter new lastname')
        t="update payroll set firstname='{}',lastname='{}' where empid='{}'".format(fn,ln,eid)
        cur.execute(t)
        print('updated table\n')
        t1="select * from payroll where empid='{}'".format(eid)
        cur.execute(t1)
        data=cur.fetchall()
        print("empid","firstname","lastname","gender","date of birth","date of joining","addrpythoness","basic_ salary","designation")
        for x in data:
            print(x)
        obj.commit()
    def modifyaddress():#modifying address of record
        eid=input('enter empid for which address is to be updated')
        add=input('enter new address')
        t="update payroll set address='{}' where empid='{}'".format(add,eid)
        cur.execute(t)
        print('updated table\n')
        t1="select * from payroll where address='{}'".format(add)
        cur.execute(t1)
        data=cur.fetchall()
        print("empid","firstname","lastname","gender","date of birth","date of joining","address","basic_ salary","designation")
        for x in data:
            print(x)
        obj.commit()
    def modify_basic_salary():#modifying basic salary of record
        eid=input('enter empid for which salary is to be updated')
        bsal=int(input('enter new basic salary'))
        t="update payroll set basic_ salary={} where empid='{}'".format( bsal,eid)
        cur.execute(t)
        print('updated table\n')
        t1="select * from payroll where empid='{}'".format(eid)
        cur.execute(t1)
        data=cur.fetchall()
        print("empid","firstname","lastname","gender","date of birth","date of joining","address","basic_ salary","designation")
        for x in data:
            print(x)
        obj.commit()
    def modify_desig():#modifying designation of record
        eid=input('enter empid for which designation is to be updated')
        desig=input('enter new designation')
        t="update payroll set designation='{}' where empid='{}'".format(desig,eid)
        cur.execute(t)
        print('updated table\n')
        t1="select * from payroll where empid='{}'".format(eid)
        cur.execute(t1)
        data=cur.fetchall()
        print("empid","firstname","lastname","gender","date of birth","date of joining","address","basic_ salary","designation")
        for x in data:
            print(x)
        obj.commit()
    while True:
        i=int(input('enter 1 to modify name; enter 2 to modify address; enter 3 to modify basic salary; enter 4 to modify designation'))
        if i==1:
            modifyname()
        elif i==2:
            modifyaddress()
        elif i==3:
            modify_basic_salary()
        elif i==4:
            modify_desig()
        else:
            break
#calculation of   salary
def   salarycalc():
    eid=input('enter empid')
    t1="select designation from payroll where empid='{}'".format(eid)
    cur.execute(t1)
    p=cur.fetchall()
    desig=p[0][0]
    t2="select basic_salary from payroll where empid='{}'".format(eid)
    cur.execute(t2)
    p1=cur.fetchall()
    bsal=p1[0][0]
    t3="select gender from payroll where empid='{}'".format(eid)
    cur.execute(t3)
    p2=cur.fetchall()
    gender=p2[0][0]
    if gender=='F':
        preg=input('is the employee pregnant? enter yes or no')
    if desig=='clerk':
        salary=0
        if gender=='F' and preg=='no':
            bonus=26000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>40:
                salary= bsal-((leaves-40)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
        elif gender=='F' and preg=='yes':
            bonus=26000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>100:
                salary= bsal-((leaves-100)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
        else:
            bonus=25000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>30:
                salary= bsal-((leaves-30)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
    elif desig=='manager':
        salary=0
        if gender=='F' and preg=='no':
            bonus=51000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>40:
                salary= bsal-((leaves-40)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
        elif gender=='F' and preg=='yes':
            bonus=51000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>100:
                salary= bsal-((leaves-100)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
        else:
            bonus=50000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>30:
                salary= bsal-((leaves-30)*( bsal/365))
                salary=  salary+bonus
            else:
                salary= bsal+bonus
    elif desig=='general manager':
        salary=0
        if gender=='F' and preg=="no":
            bonus=62000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>40:
                salary= bsal-((leaves-40)*( bsal/365))
                salary= salary+bonus
            else:
                salary= bsal+bonus
        elif gender=='F' and preg=='yes':
            bonus=51000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>100:
                salary= bsal-((leaves-100)*( bsal/365))
                salary= salary+bonus
            else:
                salary= bsal+bonus
        else:
            bonus=60000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>30:
                salary= bsal-((leaves-30)*( bsal/365))
                salary= salary+bonus
            else:
                salary= bsal+bonus
    elif desig=='president':
        salary=0
        if gender=='F' and preg=="no":
            bonus=72000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>40:
                salary= bsal-((leaves-40)*( bsal/365))
                salary= salary+bonus
            else:
                salary= bsal+bonus
        elif gender=='F' and preg=='yes':
            bonus=70000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>100:
                salary=bsal-((leaves-100)*(bsal/365))
                salary= salary+bonus
            else:
                salary=bsal+bonus
        else:
            bonus=70000
            leaves=int(input('enter no. of leaves taken'))
            if leaves>30:
                salary=bsal-((leaves-30)*(bsal/365))
                salary=salary+bonus            
    print("your salary is Rs.'{}'".format(salary))
    return(salary)
#tax
def tax():
    sal=salarycalc()
    tax=0.3*sal
    salary=sal-tax
    print("employee's final salary  after taxes is :",  salary)
#deleting
def delete():
    while True:
        inp=int(input('press 1 to delete record, press any other number to exit'))
        if inp==1:
            eid=input('enter employee ID to be deleted')
            qry="delete from payroll where empid='{}'".format(eid)
            cur.execute(qry)
            obj.commit()
            print('deleted')
        else:
            break
while True:
    inp=int(input('''Main Menu:\n[1]  Create table\n[2]   Insert into table\n[3]  Search by employee name\n[4]  Display all records\n[5]  Modify data\n[6]  Salary calculator\n[7]  Salary after tax\n[8]  Delete\n[9] Exit'''))
    print()
    if inp==1:
        create()
    elif inp==2:
        insert()
    elif inp==3:
        search_by_name()
    elif inp==4:
        displayemp()
    elif inp==5:
        modify()
    elif inp==6:
          salarycalc()
    elif inp==7:
        tax()
    elif inp==8:
        delete()
    else:
   	    break