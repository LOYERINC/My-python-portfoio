import sqlite3 as s3
regno= None
Surname=None
firstname=None
Sex=None
dob=None
phone=None
email=None
course=None

stud_count=0

conn= s3.connect('C:/lecture/python/DB/Students_Database')--my local DB 
cursor1=conn.cursor()
while True:
 stud_count+= 1
 Surname=input('Surname:')
 firstname=input('firstname:')
 Sex=input('sex:')
 dob=input('DOB:')
 phone=input('phone:')
 email=input('Email"')
 course=input('course:')

 cursor1.execute('insert into students values(?,?,?,?,?,?,?,?)',(regno,Surname,firstname,Sex,dob,phone,email,course))
 conn.commit()

 choice=None
 attempts=0
 while True:
  attempts+=1
  choice= input('\nAny MOre? y/n:')
  if choice.lower().strip()=='n' or choice.lower().strip()=='y':
   break
  else:
   if attempts<3:
    print('\nInvalid option')
   else:
    print('\n You have chosen wrong choices 3 times.\nGoodbye')
    break
   continue
 if attempts>=3:
   break
 if choice.lower().strip() =='n':
  print('\n Goodbye\n')
  break
 elif choice.lower().strip()=='y':
  pass
            
 conn.commit()
 conn.close()
