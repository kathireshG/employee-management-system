from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkcalendar import *
#from datetime import date
#import datetime

#--------------INTIAL_SETUP--------------------


root=Tk()
root.title('EMPLOYEE MANAGEMENT')
root.geometry('5000x5000')
root.state('zoomed')
root.config(bg='yellow')

mainbg=PhotoImage(file='icons/texture/bg2.png')
mainlabel=Label(root,image=mainbg).place(relwidth=1,relheight=1)

radiovar=IntVar()

#--------------Database_Setup------------------


mycon=sqlite3.connect('Employee database.db')
#cursor: Cursor=mycon.cursor()
cursor=mycon.cursor()
cursor.execute("create table if not exists details (empid int(10) primary key ,name varchar(20),age int(10),gender varchar(20), DOB varchar(20),salary int(10),nationality varchar(10));")
mycon.commit()

#------------BUTTON_FUNCTIONS------------------

def adddata():
    global display_Frame,a,Logoimage,imageLabel,SubmitImage,temp,submitimage,today
    def submit():
        global display_Frame,pictureLabel,pictureimagelabel,a
        check=True
        
        a=cursor.execute('select * from details;')
        try:
            for i in a:
                if int(EmpidEntry.get())==i[0] and check==True:
                    messagebox.showinfo("Data Error", "EMPLOYEE ID already exists !!!")
                    check=False
                    break
                else:
                    check=True
        except:
            messagebox.showinfo("Numeric Error", "Invalid Value for EMPLOYEE ID")
            check=False
            
        try:
            if check==True and int(EmpidEntry.get())<0:
                check=False
                messagebox.showinfo("Numeric Error", "Invalid Numeric Value for EMPLOYEE ID")
            elif check==True and (len(EmpidEntry.get())<5 or len(EmpidEntry.get())>5):
                check=False
                messagebox.showinfo('Error','EMPLOYEE ID CAN CONTAIN ONLY 5 DIGITS')
            else:
                pass
        except:
            messagebox.showinfo("Numeric Error", "Invalid Numeric Value for EMPLOYEE ID")
            check=False

        try:
            if check==True and int(AgeEntry.get())<0:
                check=False
                messagebox.showinfo("Numeric Error", "Invalid Numeric Value for AGE")
            else:
                pass
        except:
            messagebox.showinfo("Numeric Error", "Invalid Numeric Value for AGE")
            check=False

        try:
            if check==True and int(SalaryEntry.get())<0:
                check=False
                messagebox.showinfo("Numeric Error", "Invalid Numeric Value for SALARY")
            else:
                pass
        except:
            messagebox.showinfo("Numeric Error", "Invalid Numeric Value for SALARY")
            check=False

        if check==True and (NameEntry.get()=='' or GenderCombo.get()=='' or CalEntry.get()=='' or NationalityEntry.get()==''):
            messagebox.showinfo("Empty Fields",'Empty Field(s) !!!')
            check=False
        else:
            pass

        if check==True:
            a=(int(EmpidEntry.get()),NameEntry.get(),int(AgeEntry.get()),GenderCombo.get(),CalEntry.get(),int(SalaryEntry.get()),NationalityEntry.get())
            display_Frame.destroy()
            display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
            display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
            temp='insert into details (empid,name,age,gender,DOB,salary,nationality) values ('+str(a[0])+','+"'"+a[1].upper()+"'"+','+str(a[2])+','+"'"+a[3]+"'"+','+"'"+a[4]+"'"+','+str(a[5])+','+"'"+a[6].upper()+"'"+');'
            cursor.execute(temp)
            mycon.commit()
            pictureimagelabel=PhotoImage(file='icons/empdetails are added1.png')
            pictureLabel=Label(display_Frame,bg='cadetblue3',image=pictureimagelabel)
            pictureLabel.place(relwidth=0.6,relheight=0.2,x=205,y=200)
        else:
            pass

                             
    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,font=("arial",25,'bold'),labelanchor=N,bg='cadetblue3',text='EMPLOYEE DETAILS',bd=10,relief=RIDGE)
    details_Frame.place(x=50,y=20,relwidth=0.55,relheight=0.9)

    Logoimage=PhotoImage(file='icons/adddetails.png')
    imageLabel=Label(display_Frame,bd=0,bg='cadetblue3',image=Logoimage)
    imageLabel.place(x=750,y=95,relwidth=0.3,relheight=0.5)

    submitimage=PhotoImage(file='icons/submit.png')
    
    SubmitButton=Button(display_Frame,command=submit,bg='cadetblue3',bd=0,image=submitimage)
    SubmitButton.place(x=850,y=370)
    
    emptyLabel=Label(details_Frame,bg='cadetblue3',width=32,pady=10)
    emptyLabel.grid(padx=10)
    EmpidLabel=Label(details_Frame,font=("arial",15),text='EMPLOYEE ID NUMBER',anchor=W,width=20,bg='cadetblue3',pady=15)
    EmpidLabel.grid(padx=10)
    EmpidEg=Label(details_Frame,text='(Eg 12345):',font=("arial",15),bg='cadetblue3')
    EmpidEg.place(x=250,y=52)
    NameLabel=Label(details_Frame,font=("arial",15),text='NAME:',anchor=W,width=20,bg='cadetblue3',pady=5)
    NameLabel.grid(pady=10,padx=10)
    AgeLabel=Label(details_Frame,font=("arial",15),text='AGE:',anchor=W,width=20,bg='cadetblue3',pady=5)
    AgeLabel.grid(pady=10,padx=10)
    GenderLabel=Label(details_Frame,font=("arial",15),text='GENDER:',anchor=W,width=20,bg='cadetblue3',pady=5)
    GenderLabel.grid(pady=10,padx=10)
    CalLabel=Label(details_Frame,font=("arial",15),text='DOB (DD/MM/YYYY):',anchor=W,width=20,bg='cadetblue3',pady=5)
    CalLabel.grid(pady=10,padx=10)
    SalaryLabel=Label(details_Frame,font=("arial",15),text='SALARY:',anchor=W,width=20,bg='cadetblue3',pady=5)
    SalaryLabel.grid(pady=10,padx=10)
    NationalityLabel=Label(details_Frame,font=("arial",15),text='NATIONALITY:',anchor=W,width=20,bg='cadetblue3',pady=5)
    NationalityLabel.grid(pady=10,padx=10)

    EmpidEntry=Entry(details_Frame,font=("arial",15,'bold'))
    EmpidEntry.grid(padx=120,row=1,column=1)
    NameEntry=Entry(details_Frame,font=("arial",15,'bold'))
    NameEntry.grid(row=2,column=1)
    AgeEntry=Entry(details_Frame,font=("arial",15,'bold'))
    AgeEntry.grid(row=3,column=1)

    GenderCombo=ttk.Combobox(details_Frame, font=('arial', 15, 'bold'),state='readonly', width=18)
    GenderCombo['value']=('','MALE', 'FEMALE')
    GenderCombo.current(0)
    GenderCombo.grid(row=4,column=1)
    #today=datetime.date(1995, 12, 31)
    CalEntry=DateEntry(details_Frame,font=("arial",14,'bold'),width=18,date_pattern='dd/mm/y')#maxdate=today,
    CalEntry.grid(row=5,column=1)
    CalEntry.delete(0,'end')
    CalEntry.config(state='readonly')
    
    SalaryEntry=Entry(details_Frame,font=("arial",15,'bold'))
    SalaryEntry.grid(row=6,column=1)
    NationalityEntry=Entry(details_Frame,font=("arial",15,'bold'))
    NationalityEntry.grid(row=7,column=1)


def displaydata():
    global display_Frame
    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,text='EMPLOYEE DETAILS',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)
    scroll_y=Scrollbar(details_Frame,orient=VERTICAL)
    tv = ttk.Treeview(details_Frame,columns = (1,2,3,4,5,6,7), height=10,show = 'headings',yscrollcommand=scroll_y.set) 
    scroll_y.place(y=20,x=980,relheight=0.9)
    scroll_y.config(command=tv.yview)
    tv.place(y=20,relwidth=0.982,relheight=0.9)
    tv.column(1,width=60, anchor = 'center')
    tv.column(3,width=60, anchor = 'center')
    tv.column(4,width=100, anchor = 'center')
    tv.column(5,width=100, anchor = 'center')
    tv.column(6,width=100, anchor = 'center')
    tv.column(7,width=150, anchor = 'center')
    tv.heading(1 , text = 'EMPID')
    tv.heading(2 , text = 'NAME' )
    tv.heading(3 , text = 'AGE' )
    tv.heading(4 , text = 'GENDER' )
    tv.heading(5 , text = 'DOB' )
    tv.heading(6 , text = 'SALARY' )
    tv.heading(7 , text = 'NATIONALITY')
    temp='select * from details order by name;'
    a=cursor.execute(temp)
    #tv.insert('','end' , values ="")
    for i in a:
        tv.insert('','end' , values =i)

def sortdata():
    global display_Frame,tv,scroll_y,sortimage,tv

    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,text='SORT',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)


    scroll_y=Scrollbar(details_Frame,orient=VERTICAL)
    tv = ttk.Treeview(details_Frame, columns = (1,2,3,4,5,6,7), show = 'headings',yscrollcommand=scroll_y.set) 
    scroll_y.place(x=980,y=100,relheight=0.75)
    scroll_y.config(command=tv.yview)
    #ttk.Style().configure(Treeview,bg='yellow')
    tv.place(relwidth=0.98,relheight=0.75,y=100)
    tv.column(1,width=60, anchor = 'center')
    tv.column(3,width=60, anchor = 'center')
    tv.column(4,width=100, anchor = 'center')
    tv.column(5,width=100, anchor = 'center')
    tv.column(6,width=100, anchor = 'center')
    tv.column(7,width=150, anchor = 'center')
    tv.heading(1 , text = 'EMPID')
    tv.heading(2 , text = 'NAME')
    tv.heading(3 , text = 'AGE')
    tv.heading(4 , text = 'GENDER')
    tv.heading(5 , text = 'DOB')
    tv.heading(6 , text = 'SALARY')
    tv.heading(7 , text = 'NATIONALITY')
    a=cursor.execute('select * from details order by name;')
    #tv.tag_configure(1,bg='red')
    #ttk.Style().configure("tv", background="#383838",foreground="white")
    #ttk.Style().configure("tv.Heading",background = "blue",foreground="Black")
    for i in a:
        tv.insert('','end' , values =i)


    def sortButton():
        if sortCombo.get()=='':
             messagebox.showinfo("ERROR","BLANK FIELD")
        else:
            
            global tv,scroll_y
            
            tv.destroy()
            scroll_y.destroy()
            scroll_y=Scrollbar(details_Frame,orient=VERTICAL)
            tv = ttk.Treeview(details_Frame, columns = (1,2,3,4,5,6,7), show = 'headings',yscrollcommand=scroll_y.set) 
            scroll_y.place(x=980,y=100,relheight=0.75)
            scroll_y.config(command=tv.yview)

            tv.place(relwidth=0.98,relheight=0.75,y=100)
            tv.column(1,width=60, anchor = 'center')
            tv.column(3,width=60, anchor = 'center')
            tv.column(4,width=100, anchor = 'center')
            tv.column(5,width=100, anchor = 'center')
            tv.column(6,width=100, anchor = 'center')
            tv.column(7,width=150, anchor = 'center')
            tv.heading(1 , text = 'EMPID')
            tv.heading(2 , text = 'NAME')
            tv.heading(3 , text = 'AGE')
            tv.heading(4 , text = 'GENDER')
            tv.heading(5 , text = 'DOB')
            tv.heading(6 , text = 'SALARY')
            tv.heading(7 , text = 'NATIONALITY')
            if sortCombo.get()=='NAME':
                temp='select * from details order by name;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            elif sortCombo.get()=='NATIONALITY':
                temp='select * from details order by nationality;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            elif sortCombo.get()=='SALARY':
                temp='select * from details order by salary;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            elif sortCombo.get()=='AGE':
                temp='select * from details order by age;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            elif sortCombo.get()=='EMPLOYEE ID':
                temp='select * from details order by empid;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            elif sortCombo.get()=='GENDER':
                temp='select * from details order by gender;'
                a=cursor.execute(temp)
                for i in a:
                    tv.insert('','end' , values =i)

            else:
                pass

    sortlabel=Label(details_Frame,font=("arial",15),text='Sort According to:',bg='cadetblue3').place(x=200,y=35)

    sortCombo=ttk.Combobox(details_Frame, font=('arial', 15, 'bold'),state='readonly', width=20)
    sortCombo['value']=('','NAME','EMPLOYEE ID','AGE','SALARY','NATIONALITY','GENDER')
    sortCombo.current(0)
    sortCombo.place(x=400,y=35)

    sortimage=PhotoImage(file='icons/sort1.png')

    sortButton=Button(details_Frame,command=sortButton,image=sortimage,bd=2,bg='cadetblue3',relief=SOLID)
    sortButton.place(x=680,y=29)

def searchdata():
    global display_Frame,radiovar
    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

    def next1():
        global display_Frame
        evalue=e.get()
        if e.get()=='':
            messagebox.showinfo("ERROR","BLANK FIELD")
            pass
        else:
            display_Frame.destroy()
            display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
            display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
            details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
            details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)
        
            results=Label(details_Frame,text='RESULTS:',bg='cadetblue3',font=("arial",20,'bold','underline'))
            results.place(x=430,y=17)

            scroll_y=Scrollbar(details_Frame,orient=VERTICAL)
            tv = ttk.Treeview(details_Frame, columns = (1,2,3,4,5,6,7), show = 'headings',yscrollcommand=scroll_y.set) 
            scroll_y.place(x=980,y=100,relheight=0.75)
            scroll_y.config(command=tv.yview)

            tv.place(relwidth=0.98,relheight=0.75,y=100)
            tv.column(1,width=60, anchor = 'center')
            tv.column(3,width=60, anchor = 'center')
            tv.column(4,width=100, anchor = 'center')
            tv.column(5,width=100, anchor = 'center')
            tv.column(6,width=100, anchor = 'center')
            tv.column(7,width=150, anchor = 'center')
            tv.heading(1 , text = 'EMPID')
            tv.heading(2 , text = 'NAME')
            tv.heading(3 , text = 'AGE')
            tv.heading(4 , text = 'GENDER')
            tv.heading(5 , text = 'DOB')
            tv.heading(6 , text = 'SALARY')
            tv.heading(7 , text = 'NATIONALITY')

            def searchdataback():
                if radiovar.get()==1:
                    namesearch()
                elif radiovar.get()==2:
                    empsearch()
                elif radiovar.get()==3:
                    agesearch()
                elif radiovar.get()==4:
                    salarysearch()
                elif radiovar.get()==5:
                    gendersearch()
                elif radiovar.get()==6:
                    nationalitysearch()
                elif radiovar.get()==7:
                    dobsearch()
                    
            back=Button(details_Frame,bg='cadetblue3',command=searchdataback,image=backimage,bd=0)
            back.place(y=4,x=20)

            if radiovar.get()==1:
                temp='select * from details where name = "'+evalue.upper()+'" ;'
                cursor.execute(temp)
                a=cursor.fetchall()
                if a==[]:
                    messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                    namesearch()
                else:
                    for i in a:
                        tv.insert('','end' , values =i)

            elif radiovar.get()==2:
                try:
                    temp='select * from details where empid = '+str(evalue)+';'
                    cursor.execute(temp)
                    a=cursor.fetchall()
                    if a==[]:
                        messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                        empsearch()
                    else:
                        for i in a:
                            tv.insert('','end' , values =i)
                except:
                    messagebox.showinfo("ERROR","DATA ERROR")
                    empsearch()

            elif radiovar.get()==3:
                try:
                    temp='select * from details where age = '+str(evalue)+';'
                    cursor.execute(temp)
                    a=cursor.fetchall()
                    if a==[]:
                        messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                        agesearch()
                    else:
                        for i in a:
                            tv.insert('','end' , values =i)
                except:
                    messagebox.showinfo("ERROR","DATA ERROR")
                    agesearch()
                    
            elif radiovar.get()==4:
                try:
                    temp='select * from details where salary = '+str(evalue)+';'
                    cursor.execute(temp)
                    a=cursor.fetchall()
                    if a==[]:
                        messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                        salarysearch()
                    else:
                        for i in a:
                            tv.insert('','end' , values =i)
                except:
                    messagebox.showinfo("ERROR","DATA ERROR")
                    salarysearch()
                    
            elif radiovar.get()==5:
                temp='select * from details where gender = "'+evalue+'";'
                cursor.execute(temp)
                a=cursor.fetchall()
                if a==[]:
                    messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                    gendersearch()
                else:
                    for i in a:
                        tv.insert('','end' , values =i)

            elif radiovar.get()==6:
                temp='select * from details where nationality = "'+evalue.upper()+'";'
                cursor.execute(temp)
                a=cursor.fetchall()
                if a==[]:
                    messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                    nationalitysearch()
                else:
                    for i in a:
                        tv.insert('','end' , values =i)

            elif radiovar.get()==7:
                temp='select * from details where DOB = "'+evalue+'";'
                cursor.execute(temp)
                a=cursor.fetchall()
                if a==[]:
                    messagebox.showinfo("RESULTS","NO RESULTS FOUND")
                    dobsearch()
                else:
                    for i in a:
                        tv.insert('','end' , values =i)
       
    def namesearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER NAME (FULL NAME):' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)

        backimage=PhotoImage(file='icons/back.png')
        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)

    def nationalitysearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER NATIONALITY:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)
        backimage=PhotoImage(file='icons/back.png')

        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)

    def salarysearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER SALARY:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)
        backimage=PhotoImage(file='icons/back.png')

        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)

    def empsearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER EMPLOYEE ID:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)
        backimage=PhotoImage(file='icons/back.png')

        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)

    def salarysearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER SALARY:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)
        backimage=PhotoImage(file='icons/back.png')

        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)

    def agesearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER AGE:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e.place(x=550,y=120)
        backimage=PhotoImage(file='icons/back.png')

        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=250,x=600)


    def gendersearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER GENDER:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        lab.place(x=90,y=120)

        e=ttk.Combobox(details_Frame, font=('arial', 20, 'bold'),state='readonly', width=20)
        e['value']=('','MALE', 'FEMALE')
        e.current(0)
        e.place(x=550,y=120)

        backimage=PhotoImage(file='icons/back.png')
        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=200,x=600)

    def dobsearch():
        global display_Frame,e,backimage,nextimage
        display_Frame.destroy()
        display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
        display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
    
        details_Frame=LabelFrame(display_Frame,text='SEARCH',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
        details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

        lab = Label(details_Frame, text = 'ENTER DATE OF BIRTH (DD/MM/YYYY):' , bg = 'cadetblue3', font=("arial",20))
        lab.place(x=60,y=120)

        e = DateEntry(details_Frame,font=("arial",20),width = 20,bg='#FFDFA4',date_pattern='dd/mm/y')
        e.place(x=610,y=120)
        e.delete(0, "end")
        e.config(state='readonly')

        backimage=PhotoImage(file='icons/back.png')
        back=Button(details_Frame,command=searchdata,image=backimage,bd=0,bg='cadetblue3')
        back.place(y=4,x=20)
        
        nextimage=PhotoImage(file='icons/next.png')
        next=Button(details_Frame,command=next1,image=nextimage,bd=0,bg='cadetblue3')
        next.place(y=200,x=600)

    search=Label(details_Frame,text='SEARCH BY:',font=("arial",20,'bold','underline'),bg='cadetblue3').place(x=420,y=50)
    r1 = Radiobutton(details_Frame , command=namesearch,text = '1. NAME' , height ='2', bg = 'cadetblue3',font=("arial",20)  , value = 1 ,variable=radiovar)
    r1.place(x=120,y=130)
    r2 = Radiobutton(details_Frame ,command=empsearch,text = '2. EMPLOYEE ID' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 2   ,variable=radiovar)
    r2.place(x=290,y=130)
    r3 = Radiobutton(details_Frame ,command=agesearch,text = '3. AGE' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 3 ,variable=radiovar)
    r3.place(x=560,y=130)
    r4 = Radiobutton(details_Frame ,command=salarysearch,text = '4. SALARY' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 4  ,variable=radiovar)
    r4.place(x=700,y=130)
    r5 = Radiobutton(details_Frame , command=gendersearch,text = '6. GENDER', height ='2',bg = 'cadetblue3',font=("arial",20), value = 5 ,variable=radiovar)
    r5.place(x=565,y=210)
    r6 = Radiobutton(details_Frame , command=nationalitysearch,text = '7. NATIONALITY', height ='2',bg = 'cadetblue3',font=("arial",20), value = 6 ,variable=radiovar)
    r6.place(x=400,y=285)
    r7 = Radiobutton(details_Frame , command=dobsearch,text = '5. DATE OF BIRTH', height ='2',bg = 'cadetblue3',font=("arial",20), value = 7 ,variable=radiovar)
    r7.place(x=270,y=210)

def deletedata():
    global display_Frame,delete1image
    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,text='DELETE',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

    lab = Label(details_Frame, text = 'ENTER EMPLOYEE ID:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
    lab.place(x=90,y=120)

    deleteEntry = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
    deleteEntry.place(x=550,y=120)

    def deleteButton():
        global deleteimagelabel,backimage
        a=cursor.execute('select * from details;')

        if deleteEntry.get()=='':
            messagebox.showinfo("ERROR","BLANK FIELD")

        else:
            del_val=messagebox.askquestion('Delete ?','Are You Sure?')
            cursor.execute('select * from details where empid='+str(deleteEntry.get())+' ;')
            tempdelete=cursor.fetchall()
            if del_val=='yes':
                if tempdelete==[]:
                    messagebox.showinfo("ERROR","EMPLOYEE ID NOT FOUND")
                
                else:
                    temp='delete from details where empid = '+str(deleteEntry.get())+' ;'
                    cursor.execute(temp)
                    mycon.commit()

                    details_Frame=LabelFrame(display_Frame,text='DELETE',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
                    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

                    deleteimagelabel=PhotoImage(file='icons/empdetails are deleted.png')
                    deleteLabel=Label(details_Frame,bg='cadetblue3',image=deleteimagelabel)
                    deleteLabel.place(relwidth=0.6,relheight=0.2,x=205,y=150)

                    backimage=PhotoImage(file='icons/back.png')
                    back=Button(details_Frame,command=deletedata,image=backimage,bd=0,bg='cadetblue3')
                    back.place(y=4,x=20)
            else:
                pass

    delete1image=PhotoImage(file='icons/delete1.png')
    delete1Button=Button(display_Frame,command=deleteButton,bd=0,bg='cadetblue3',image=delete1image)
    delete1Button.place(y=270,x=700)


def modifyfinal():
    global display_Frame,e1value
    modify_val=messagebox.askokcancel('Confirmation','Employee Details will be changed')
    if modify_val==True:
        e1value=e1.get()
        cursor.execute('select * from details;')
        a=cursor.fetchall()
        empid_check_modify=True
        for i in a:
            if str(i[0])==e1value:
                empid_check_modify=False
            else:
                pass

        if empid_check_modify==False:
            messagebox.showinfo("ERROR","EMPLOYEE ID ALREADY EXISTS ")
            modifyradiodata()
            
        elif e1value=='':
            messagebox.showinfo("ERROR","BLANK FIELD")
            modifyradiodata()

        elif radiovar.get()==2 and len(e1value)!=5 :
            messagebox.showinfo('Error','EMPLOYEE ID CAN CONTAIN ONLY 5 DIGITS')
            
        else:
            display_Frame.destroy()
            display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
            display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
                        
            details_Frame=LabelFrame(display_Frame,text='MODIFY',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
            details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

            final_modify_check=False

            try:
                if radiovar.get()==1:
                    temp='UPDATE details set name='+'"'+e1value.upper()+'"'+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==2:
                    temp='UPDATE details set empid='+str(e1value)+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==3:
                    temp='UPDATE details set age='+str(e1value)+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==4:
                    temp='UPDATE details set salary='+str(e1value)+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==5:
                    temp='UPDATE details set gender='+'"'+e1value.upper()+'"'+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==6:
                    temp='UPDATE details set nationality='+'"'+e1value.upper()+'"'+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True
                    
                elif radiovar.get()==7:
                    temp='UPDATE details set DOB='+'"'+e1value.upper()+'"'+' WHERE empid = '+str(tempvalue)+';'
                    cursor.execute(temp)
                    mycon.commit()
                    messagebox.showinfo('Successful','EMPLOYEE DETAILS HAVE BEEN CHANGED')
                    final_modify_check=True

                if final_modify_check==True:
                    modifyfinallabel=Label(details_Frame,text='NEW DETAILS:',font=("arial",20,'bold'),bg='cadetblue3')
                    modifyfinallabel.place(x=410,y=30)

                    scroll_y=Scrollbar(details_Frame,orient=VERTICAL)
                    tv = ttk.Treeview(details_Frame, columns = (1,2,3,4,5,6,7), show = 'headings',yscrollcommand=scroll_y.set) 
                    scroll_y.place(x=980,y=100,relheight=0.75)
                    scroll_y.config(command=tv.yview)

                    tv.place(relwidth=0.98,relheight=0.75,y=100)
                    tv.column(1,width=60, anchor = 'center')
                    tv.column(3,width=60, anchor = 'center')
                    tv.column(4,width=100, anchor = 'center')
                    tv.column(5,width=100, anchor = 'center')
                    tv.column(6,width=100, anchor = 'center')
                    tv.column(7,width=150, anchor = 'center')
                    tv.heading(1 , text = 'EMPID')
                    tv.heading(2 , text = 'NAME')
                    tv.heading(3 , text = 'AGE')
                    tv.heading(4 , text = 'GENDER')
                    tv.heading(5 , text = 'DOB')
                    tv.heading(6 , text = 'SALARY')
                    tv.heading(7 , text = 'NATIONALITY')

                    modifyback_button=Button(details_Frame,command=modifydata,image=backimage,bd=0)
                    modifyback_button.place(y=4,x=20)
                    
                    if radiovar.get()==2:
                        temp='select * from details where empid = '+str(e1value)+' ;'
                        cursor.execute(temp)
                        a=cursor.fetchall()
                        for i in a:
                            tv.insert('','end' , values =i)
                        
                    else:
                        temp='select * from details where empid = '+tempvalue+' ;'
                        cursor.execute(temp)
                        a=cursor.fetchall()
                        for i in a:
                            tv.insert('','end' , values =i)

            except:
                messagebox.showinfo('Error','Data Error')
                modifyradiodata()
    else:
        pass
                
def modifyradiodata():
    global display_Frame,backimage,nextimage,e1,details_Frame,next1image

    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)
                
    details_Frame=LabelFrame(display_Frame,text='MODIFY',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

    Ex_details_Frame=LabelFrame(details_Frame,text='EXISTING DETAILS',bd=2,font=("arial",17,'bold'),relief=SOLID,bg='cadetblue3',labelanchor=N)
    Ex_details_Frame.place(relwidth=0.76,relheight=0.25,x=120,y=25)

    if radiovar.get()==1:
        cursor.execute('select name from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing Name:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=150,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=420,y=20)

        modifydatalabel = Label(details_Frame, text = 'ENTER NEW NAME:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e1.place(x=550,y=180)

        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)

    elif radiovar.get()==2:
        cursor.execute('select empid from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing EMPLOYEE ID:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=150,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=450,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW EMPLOYEE ID:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e1.place(x=550,y=180)

        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)
        
    elif radiovar.get()==3:
        cursor.execute('select age from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing Age:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=240,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=450,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW AGE:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e1.place(x=550,y=180)
        
        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)
        
    elif radiovar.get()==4:
        cursor.execute('select salary from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing Salary:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=200,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=450,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW SALARY:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e1.place(x=550,y=180)
        
        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)
        
    elif radiovar.get()==5:
        cursor.execute('select gender from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing Gender:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=200,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=460,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW GENDER:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1=ttk.Combobox(details_Frame, font=('arial', 20, 'bold'),state='readonly', width=20)
        e1['value']=('','MALE', 'FEMALE')
        e1.current(0)
        e1.place(x=550,y=180)
        
        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)
        
    elif radiovar.get()==6:
        cursor.execute('select nationality from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing Nationality:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=150,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=400,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW NATIONALITY:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
        e1.place(x=550,y=180)
        
        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)

    elif radiovar.get()==7:
        cursor.execute('select DOB from details where empid = '+str(tempvalue)+';')
        a=cursor.fetchall()

        Exist=Label(Ex_details_Frame,text='Existing DOB:',bg='cadetblue3',font=("arial",14,'bold'))
        Exist.place(x=200,y=20)

        Exist_Label1=Label(Ex_details_Frame,text=a[0][0],bg='cadetblue3',fg='black',font=("arial",14,'bold'))
        Exist_Label1.place(x=420,y=20)
        
        modifydatalabel = Label(details_Frame, text = 'ENTER NEW DOB:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
        modifydatalabel.place(x=90,y=180)

        e1= DateEntry(details_Frame,font=("arial",20),width = 20,bg='#FFDFA4',date_pattern='dd/mm/y')
        e1.place(x=550,y=180)
        e1.delete(0, "end")
        e1.config(state='readonly')
        
        next1image=PhotoImage(file='icons/modify1.png')

        modifynext=Button(details_Frame,command=modifyfinal,image=next1image,bd=0,bg='cadetblue3')
        modifynext.place(y=260,x=600)
        
    else:
        pass
    
def modifynext():
    global display_Frame,backimage,tempvalue,details_Frame
    if modifyEntry.get()=='':
        messagebox.showinfo("ERROR","BLANK FIELD")
        pass
        
    else:
        a=cursor.execute('select * from details;')
        cursor.execute('select * from details where empid='+str(modifyEntry.get())+' ;')
        tempmodify=cursor.fetchall()
        if tempmodify==[]:
            messagebox.showinfo("ERROR","EMPLOYEE ID NOT FOUND")
        else:
            tempvalue=str(modifyEntry.get())

            display_Frame.destroy()
            display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
            display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

            details_Frame=LabelFrame(display_Frame,text='MODIFY',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
            details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

            modify_2_label=Label(details_Frame,text='SELECT PARAMETER:',font=("arial",20,'bold','underline'),bg='cadetblue3')
            modify_2_label.place(x=340,y=50)

            backimage=PhotoImage(file='icons/back.png')

            modifyback_button=Button(details_Frame,command=modifydata,image=backimage,bd=0)
            modifyback_button.place(y=4,x=20)
            
            r1 = Radiobutton(details_Frame,command=modifyradiodata, text = '1. NAME' , height ='2', bg = 'cadetblue3',font=("arial",20)  , value = 1 ,variable=radiovar)
            r1.place(x=120,y=130)
                
            r2 = Radiobutton(details_Frame ,command=modifyradiodata,text = '2. EMPLOYEE ID' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 2   ,variable=radiovar)
            r2.place(x=290,y=130)
                
            r3 = Radiobutton(details_Frame ,command=modifyradiodata,text = '3. AGE' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 3 ,variable=radiovar)
            r3.place(x=560,y=130)
                
            r4 = Radiobutton(details_Frame ,command=modifyradiodata,text = '4. SALARY' ,height ='2',bg = 'cadetblue3',font=("arial",20), value = 4  ,variable=radiovar)
            r4.place(x=700,y=130)
                
            r5 = Radiobutton(details_Frame ,command=modifyradiodata,text = '6. GENDER', height ='2',bg = 'cadetblue3',font=("arial",20), value = 5 ,variable=radiovar)
            r5.place(x=565,y=210)
                
            r6 = Radiobutton(details_Frame,command=modifyradiodata,text = '7. NATIONALITY', height ='2',bg = 'cadetblue3',font=("arial",20), value = 6 ,variable=radiovar)
            r6.place(x=400,y=285)
                
            r7 = Radiobutton(details_Frame,command=modifyradiodata,text = '5. DATE OF BIRTH', height ='2',bg = 'cadetblue3',font=("arial",20), value = 7 ,variable=radiovar)
            r7.place(x=270,y=210)


def modifydata():
    global display_Frame,nextimage,modifyEntry,details_Frame
    display_Frame.destroy()
    display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
    display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

    details_Frame=LabelFrame(display_Frame,text='MODIFY',padx=5,pady=5,bd=10,font=("arial",25,'bold'),bg='cadetblue3',labelanchor=N)
    details_Frame.place(relwidth=0.9,relheight=0.9,x=60,y=25)

    modifylabel = Label(details_Frame, text = 'ENTER EMPLOYEE ID:' , bg = 'cadetblue3',width = '25' , font=("arial",20))
    modifylabel.place(x=90,y=120)

    modifyEntry = Entry(details_Frame,font=("arial",20), width = 20,bg='#FFDFA4')
    modifyEntry.place(x=550,y=120)

    nextimage=PhotoImage(file='icons/next.png')

    modifynext1=Button(details_Frame,command=modifynext,image=nextimage,bd=0,bg='cadetblue3')
    modifynext1.place(y=200,x=600)

#--------------FRAMES ---------------------------

frame=Frame(root,bd=15,relief='ridge',bg='gray44')
frame.place(relx=0,rely=0,relwidth=0.15,relheight=1)

bgimage=PhotoImage(file='icons/texture/texture2.png')
framebg=Label(frame,image=bgimage).place(relwidth=1,relheight=1)


artframe=Frame(root,bg='blue')
artframe.place(relx=0.15,relwidth=1,relheight=0.15)
artcanvas=Canvas(artframe)
artcanvas.pack(fill=BOTH,expand=YES)
empart=PhotoImage(file='icons/wordart.png')
artcanvas.create_image(0,0,image=empart,anchor=NW)
 
display_Frame=Frame(root,bg='cadetblue3',bd=12,relief=SOLID)
display_Frame.place(relx=0.19,rely=0.22,relwidth=0.76,relheight=0.71)

first_slide_pici=PhotoImage(file='icons/first.png')
first_slide_pic=Label(display_Frame,image=first_slide_pici,bd=0).place(x=150,y=60)


#----------------MENU BUTTONS----------------------

menuimage=PhotoImage(file='icons/MENU.png')

menu=Label(frame,image=menuimage,font=("arial",20,'bold'),fg='white',bg='gray44').pack(fill=X,pady=10)
Photo1=PhotoImage(file='icons/display1.png')
Photo1image=Photo1.subsample(3,3)
display=Button(frame,command=displaydata,text='DISPLAY',image=Photo1image,bd=10,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=10)
display.pack(fill=X,pady=8)


Photo2=PhotoImage(file='icons/add.png')
Photo2image=Photo2.subsample(3,3)
add=Button(frame,command=adddata,text='ADD DATA',image=Photo2image,bd=10,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=10)
add.pack(fill=X,pady=8)

Photo3=PhotoImage(file='icons/search.png')
Photo3image=Photo3.subsample(3,3)
search=Button(frame,command=searchdata,image=Photo3image,text='SEARCH',bd=10,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=10)
search.pack(fill=X,pady=8)

Photo4=PhotoImage(file='icons/sort.png')
Photo4image=Photo4.subsample(3,3)
sort=Button(frame,text='SORT',command=sortdata,bd=10,image=Photo4image,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=10)
sort.pack(fill=X,pady=8)

Photo5=PhotoImage(file='icons/modify.png')
Photo5image=Photo5.subsample(3,3)
modify=Button(frame,command=modifydata,text='MODIFY',bd=10,image=Photo5image,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=10)
modify.pack(fill=X,pady=8)

Photo6=PhotoImage(file='icons/delete.png')
Photo6image=Photo6.subsample(3,3)
delete=Button(frame,command=deletedata,image=Photo6image,text='DELETE',bd=10,bg='lightgreen',relief='ridge',compound=LEFT,font=("arial",15,'bold'),padx=10,pady=6)
delete.pack(fill=X,pady=8)

Photo7=PhotoImage(file='icons/exit.png')
Photo7image=Photo7.subsample(3,3)
exit1=Button(frame,image=Photo7,bd=10,bg='lightgreen',relief='ridge',compound=LEFT,command=exit,font=("arial",15,'bold'),padx=10,pady=10)
exit1.pack(fill=X,pady=8)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",font=('arial',12))
style.configure("Treeview.Heading", font=('calibri',19))
#('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

try:
    root.iconbitmap('icons/main icon1.ico')
except:
    pass

#------------------------------------------------
root.mainloop()


