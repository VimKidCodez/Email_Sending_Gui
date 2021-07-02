# Author: S D Sriram
# Designation: Student Studing in 7th Grade
# I will be uploading files  weekly

from tkinter import *
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# You don't have to import anything
#gui
root= Tk()
root.geometry('500x680')
root.title("Free Email Service ")
root.iconbitmap('email.ico')
root.resizable(0, 0)

Label_0=Label(root, text="Send an email for free", width=20, fg="brown", font=("bold",20))
Label_0.place(x=90,y=33)

Label_1=Label(root, text=" Email Account:", width=20,fg="green", font=("bold",10))
Label_1.place(x=40,y=110)

Rmail=StringVar()
Rpswrd=StringVar()
Rsender=StringVar()
Rsubject=StringVar()


emailE=Entry(root, width=40, textvariable=Rmail)
emailE.place(x=200, y=110)

Label_2=Label(root, text="Your Password:", width=20,fg="red", font=("bold",10))
Label_2.place(x=40,y=160)


passwordE=Entry(root, width=40, show="*", textvariable=Rpswrd)
passwordE.place(x=200, y=160)

compose=Label(root, text=" Send an Email", width=20, font=("bold",15))
compose.place(x=180,y=210)

Label_3=Label(root, text="Sent To Email:", width=20, font=("bold",10))
Label_3.place(x=40,y=260)


senderE=Entry(root, width=40, textvariable=Rsender)
senderE.place(x=200, y=260)

Label_4=Label(root, text="Subject:", width=20, font=("bold",10))
Label_4.place(x=40,y=310)


subjectE=Entry(root, width=40, textvariable=Rsubject)
subjectE.place(x=200, y=310)


Label_5=Label(root, text="Message:", width=20, font=("bold",10))
Label_5.place(x=40,y=360)


msgbodyE=Text(root, width=30, height=10)
msgbodyE.place(x=200, y=360)






# when you click the send.png this thing will happen
def sendemail():

    

    try:
        mymsg=MIMEMultipart()
        mymsg['From']=str(Rmail.get())
        mymsg['To']= str(Rsender.get())
        mymsg['Subject']= str(Rsubject.get())

        mymsg.attach(MIMEText(msgbodyE.get(1.0,'end'), 'plain'))

        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(Rmail.get()), str(Rpswrd.get()))
        text=mymsg.as_string()
        server.sendmail(str(Rmail.get()), str(Rsender.get()), text)

        Label_6=Label(root, text="Done!", width=20,fg='green', font=("bold",15))
        Label_6.place(x=140,y=550)

        server.quit()
    except:
        Label_6=Label(root, text="something went wrong!", width=20,fg='red', font=("bold",15))
        Label_6.place(x=140,y=550)

sendimage = PhotoImage(file='send.png')
send_image = Button(root,image = sendimage, fg="white", command=sendemail).place(x=250, y=550)
# ----------------------
root.mainloop()

