from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import sqlite3
from tkinter import messagebox,ttk
import os
from datetime import*
import time
from math import *

class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Perfomance Analysis System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #_icons
        self.logo_dash=ImageTk.PhotoImage(file="images./logo_p.png")
        #_title
        title=Label(self.root,text="Student Perfomance Analysis System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)


        btn_couse=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=150,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_student).place(x=210,y=5,width=150,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=400,y=5,width=150,height=40)
        btn_view=Button(M_Frame,text="Result View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=590,y=5,width=150,height=40)
        btn_logout=Button(M_Frame,text="Logout",command=self.logout,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=780,y=5,width=150,height=40)
        btn_exit=Button(M_Frame,text="Exit",command=self.exit_,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=970,y=5,width=150,height=40)
        btn_mocktest=Button(M_Frame,text="Mock Test",command=self.mocktest,font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2").place(x=1160,y=5,width=150,height=40)
        #window content____
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #update Details____
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)


        ################ clock 
        self.lbl=Label(self.root, text = "\nC.L.O.C.K",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)
        self.working()

       #footer____
        footer=Label(self.root,bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
#FUNCTION________________________________________________
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB", (400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        #====For Clock Image
        bg=Image.open("images/c.png")
        bg=bg.resize((300,300), Image.LANCZOS)     # 22
        clock.paste(bg,(50,50))
        
        
        #====Hour Line Image====
        origin=200, 200
        draw.line((origin, 200+50*sin(radians (hr)), 200-50*cos(radians(hr))), fill="#DF005E", width=4)
        #Min Line Image====
        draw.line((origin, 200+80*sin(radians(min_)),200-80*cos(radians(min_))), fill="white", width=3)
        #====Sec Line Image====
        draw.line((origin, 200+100*sin(radians(sec_)),200-100*cos(radians(sec_))), fill="yellow", width=4)
        
        draw.ellipse((195,195, 210, 210), fill="#1AD5D5") 
        clock.save("images/clock_new.png")

    def working(self):
        h = datetime.now().time().hour 
        m = datetime.now().time().minute 
        h = datetime.now().time().second 
        s = datetime.now().time().second
        
        hr=(h/12)*360                 #47
        min_=(m/60)*360
        sec_=(s/60)*360
        
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk. PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
        
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

        
        
    
    
    def update_details(self):
        con = sqlite3.connect(database= 'rms.db') 
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            course = cur.fetchall()
            self.lbl_course.config(text=f'Total Courses\n[{str(len(course))}]')

            cur.execute("SELECT * FROM student")
            student = cur.fetchall()
            self.lbl_student.config(text=f'Total Students\n[{str(len(student))}]')

            cur.execute("SELECT * FROM result")
            result = cur.fetchall()
            self.lbl_result.config(text=f'Total Results\n[{str(len(result))}]')

            self.lbl_course.after(200,self.update_details)
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit",parent=self.root)
        if op==True:
            self.root.destroy()
            
    def mocktest(self):
        op=messagebox.askyesno("Confirm","Start Mock Test",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python mocktest.py")
            

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
    
















    
    
    
