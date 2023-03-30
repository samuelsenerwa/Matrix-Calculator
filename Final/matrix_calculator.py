from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np

def Second_Window():
    # ----Functions To check for invalid input :----  
    def checkInput(textBox,row,col):
        if textBox.compare("end-1c", "==", "1.0"):
            messagebox.showerror("Matrix Empty", "Please Enter the Matrix") 
            return(1)
        return(0)
            
    def checkEmpty(entry1,entry2):
        if len(entry1.get()) == 0: 
            messagebox.showerror("Empty", "Please enter number of Rows")
            return(1)
        elif len(entry2.get()) == 0:    
            messagebox.showerror("Empty", "Please enter number of Columns")
            return(1)
        elif (entry1.get()).isdigit() == False or (entry2.get()).isdigit() == False:
            messagebox.showerror("Invalid Input", "Please enter a valid input")
            return(1)
        return(0)
        

    # ----Show widgets and text box in frame 2:----
    def showFrame(choice):
        clearFrame(f2)
        clearFrame(f3)  
        c = choice.get()
        if c == ' Single':                  
            Label(f2,text="Number of Rows",font=("Times",13)).place(relx=0.32,rely=0.15,relwidth=0.17)
            e1 = Entry(f2,font=("Times",12))
            e1.place(relx=0.5,rely=0.15,relwidth=0.04)
            Label(f2,text="Number of Columns",font=("Times",13)).place(relx=0.32,rely=0.2,relwidth=0.17)
            e2 = Entry(f2,font=("Times",12))
            e2.place(relx=0.5,rely=0.2,relwidth=0.04)        
            Button(f2,text="Continue",fg ='blue', command=lambda: showMatrix1(e1,e2,input1)).place(relx=0.4,rely=0.25,relwidth=0.07)
            input1 = Text(f2,font=("Times",14))
            input1.configure(insertbackground="white")
            input1.place(relx=0.3,rely=0.3,relwidth=0.3,relheight=0.3)   
            Button(f2,text="Clear",fg="#green",command=lambda: delete(input1)).place(relx=0.4,rely=0.62,relwidth=0.07,relheight=0.05)
        elif c == ' Double':             
            Label(f2,text="Matrix A",font=("Times",17)).place(relx=0.15,rely=0.14,relwidth=0.17)
            Label(f2,text="Number of Rows",font=("Times",13)).place(relx=0.06,rely=0.2,relwidth=0.17)
            e1 = Entry(f2,font=("Times",12))
            e1.place(relx=0.24,rely=0.2,relwidth=0.04)
            Label(f2,text="Number of Columns",font=("Times",13)).place(relx=0.06,rely=0.24,relwidth=0.17)
            e2 = Entry(f2,font=("Times",12))
            e2.place(relx=0.24,rely=0.24,relwidth=0.04)
            Label(f2,text="Matrix B",font=("Times",17)).place(relx=0.65,rely=0.14,relwidth=0.17)
            Label(f2,text="Number of Rows",font=("Times",13)).place(relx=0.56,rely=0.2,relwidth=0.17)
            e3 = Entry(f2,font=("Times",12))
            e3.place(relx=0.74,rely=0.2,relwidth=0.04)
            Label(f2,text="Number of Columns",font=("Times",13)).place(relx=0.56,rely=0.24,relwidth=0.17)
            e4 = Entry(f2,font=("Helvetica",12))
            e4.place(relx=0.74,rely=0.24,relwidth=0.04)
            Button(f2,text="Continue",fg='blue', command=lambda: showMatrix2(e1,e2,e3,e4,input1,input2)).place(relx=0.45,rely=0.28,relwidth=0.07)
            input1 = Text(f2,font=("Times",14))  
            input1.configure(insertbackground="white")
            input2 = Text(f2,font=("Times",14)) 
            input1.configure(insertbackground="white")
            input2.configure(insertbackground="white")
            input1.place(relx=0.1,rely=0.35,relwidth=0.3,relheight=0.3)     
            input2.place(relx=0.55,rely=0.35,relwidth=0.3,relheight=0.3) 
            Button(f2,text="Clear",fg='green',command=lambda: delete(input1)).place(relx=0.2,rely=0.68,relwidth=0.1,relheight=0.04)
            Button(f2,text="Clear",fg="green",command=lambda: delete(input2)).place(relx=0.65,rely=0.68,relwidth=0.1,relheight=0.04)
                    
    # ----Clearing contents of text box:----       
    def delete(textBox):
        textBox.delete(1.0,END)

    # ----Clearing contents of Frame:---- 
    def clearFrame(frame):
        for w in frame.winfo_children():
            print(w)
            w.place_forget()
        if frame == f2:
            Label(f2,text="Input Matrix",font=("Times",17),borderwidth = 3,
             relief="sunken").place(relx=0.36,rely=0.04,relwidth=0.18,relheight=0.08)
        elif frame == f3:
            Label(f3,text="Output Matrix",font=("Times",17),borderwidth = 3,
             relief="sunken").place(relx=0.12,rely=0.04,relwidth=0.12,relheight=0.08)
        
    # ----Creating a 2-D array from String:-----      
    def findArray(r,c,input1):
        main_list = []
        i = float(r)    
        lst1 = list(input1.get(1.0,i+1.0).splitlines())    
        print(lst1);
        if len(lst1) != r:
            messagebox.showerror("Invalid Input", "Please enter a valid input!")
            return
        for i in range(0,r):
            lst1[i] = lst1[i].rstrip()        
            try:
                lst2 = list(map(int, lst1[i].split(" ")))
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid input!")
                return
            except TypeError:
                messagebox.showerror("Invalid Input", "Please enter a valid input!")
                return
            else:
                if len(lst2)!=c :
                    messagebox.showerror("Invalid Input", "Please enter a valid input!")
                    return
                main_list.append(lst2)
        arr = np.array(main_list)    
        return(arr)    

    # -----Displaying output in frame3 in text box:----
    def showResult(row,col,res):
        clearFrame(f3)    
        output1 = Text(f3,font=("Times",14))
        output1.place(relx=0.08,rely=0.3,relwidth=0.20,relheight=0.30)   
        t = "\n"
        for i in range(0,row):
            for j in range(0,col):            
                s = str(res[i][j])         
                s = s + " "
                output1.insert(INSERT,s)
                if j == col-1:
                    output1.insert(INSERT,t)   
        output1.config(state="disabled")
            
    # -----Functions on Single MATRIX:----  
    def calTrans(row,col,input1):
        test = checkInput(input1,row,col)
        if test:
            return     
        input_arr = findArray(row,col,input1)
        res = input_arr.transpose()
        showResult(col,row,res)
        
    def calDet(row,col,input1):
        if row != col:
            messagebox.showerror("Invalid Input", "Cannot calculate Determinant of non-square matrix!") 
            return
        test = checkInput(input1,row,col)
        if test:
            return     
        input_arr = findArray(row,col,input1)
        d = np.linalg.det(input_arr)
        d = int(np.round_(d))
        clearFrame(f3)
        Label(f3,text="Determinant of Matrix Entered: ",font=("Times",14)).place(relx=0.1,rely=0.4,relheight=0.08)
        Label(f3,text=str(d),font=("Times",14)).place(relx=0.18,rely=0.5,relheight=0.09,relwidth=0.04)



    def calInverse(row,col,input1):
        test = checkInput(input1,row,col)
        if test:
            return 
        if row != col:
            messagebox.showerror("Invalid Input", "Cannot calculate Inverse of non-square matrix!") 
            return
        input_arr = findArray(row,col,input1)
        d = int(np.linalg.det(input_arr))
        if d == 0:
            messagebox.showerror("Invalid Input", "Cannot calculate Inverse of singular matrix(Determinent=0)!")
            return
        res = np.linalg.inv(input_arr)
        res = np.round_(res,decimals=6)
        showResult(row,col,res)
        

    # -----Functions on Double MATRIX:----  
    def matrixAdd(row1,col1,row2,col2,input1,input2):
        if row1 != row2 or col1 != col2:
            messagebox.showerror("Invalid Input", "No. of rows and columns of two matrix should be equal for Addition")
            return 
        if checkInput(input1,row1,col1):
            return   
        elif checkInput(input2,row2,col2):
            return
        input_arr1 = findArray(row1,col1,input1)
        input_arr2 = findArray(row1,col1,input2)
        res = np.add(input_arr1,input_arr2)
        showResult(row1,col1,res)

    def matrixSub(row1,col1,row2,col2,input1,input2):
        if row1 != row2 or col1 != col2:
            messagebox.showerror("Invalid Input", "No. of rows and columns of two matrix should be equal for Substraction")
            return    
        if checkInput(input1,row1,col1):
            return   
        elif checkInput(input2,row2,col2):
            return
        input_arr1 = findArray(row1,col1,input1)
        input_arr2 = findArray(row1,col1,input2)
        res = np.subtract(input_arr1,input_arr2)
        showResult(row1,col1,res)
        
    def matrixMul(row1,col1,row2,col2,input1,input2):
        if col1 != row2:
            messagebox.showerror("Invalid Input", "No. of columns of matrix1 should be equal to number of rows of matrix2 for Multiplication")
            return 
        if checkInput(input1,row1,col1):
            return   
        elif checkInput(input2,row2,col2):
            return  
        input_arr1 = findArray(row1,col1,input1)
        input_arr2 = findArray(row2,col2,input2)
        res = np.dot(input_arr1,input_arr2)
        showResult(row1,col2,res)   
       
    # ----Frame 2 Buttons and Text Box:----
    def showMatrix1(e1,e2,input1):    
        if checkEmpty(e1,e2):
            return
        row = int(e1.get())
        col = int(e2.get())         
        Button(f2,text="Transpose",fg="blue",font=("italic",15),highlightthickness=10,highlightbackground="blue",command=lambda: calTrans(row,col,input1)).place(relx=0.28,rely=0.7,relwidth=0.15,relheight=0.1)
        Button(f2,text="Inverse",fg="blue", font=("italic",15),command=lambda: calInverse(row,col,input1)).place(relx=0.46,rely=0.7,relwidth=0.15,relheight=0.1)
        Button(f2,text="Determinant",fg="blue",font=("italic",15),command=lambda: calDet(row,col,input1)).place(relx=0.36 ,rely=0.82,relwidth=0.15,relheight=0.1)    
        
    def showMatrix2(e1,e2,e3,e4,input1,input2):
        if checkEmpty(e1,e2):
            return
        elif checkEmpty(e3,e4):
            return
        row1 = int(e1.get())
        col1 = int(e2.get())
        row2 = int(e3.get())
        col2 = int(e4.get())        
        Button(f2,text="Addition[A+B]",fg="blue",font=("italic",12),command=lambda: matrixAdd(row1,col1,row2,col2,input1,input2)).place(relx=0.28,rely=0.73,relwidth=0.18,relheight=0.08)
        Button(f2,text="Substraction[A-B]",fg="blue",font=("italic",12), command=lambda: matrixSub(row1,col1,row2,col2,input1,input2)).place(relx=0.49,rely=0.73,relwidth=0.18,relheight=0.08)
        Button(f2,text="Multiplication[A*B]",fg="blue",font=("italic",12), command=lambda: matrixMul(row1,col1,row2,col2,input1,input2)).place(relx=0.28 ,rely=0.84,relwidth=0.18,relheight=0.08)
        Button(f2,text="Substraction[B-A]",fg="blue",font=("italic",12),command = lambda: matrixSub(row2,col2,row1,col1,input2,input1)).place(relx=0.49 ,rely=0.84,relwidth=0.18,relheight=0.08)
        

      #Function for displaying explanation
    def open_frame():
        new_window = Toplevel(root)
        new_window.title("Matrix Explanation")
        frame = Frame(new_window)
        frame.pack()
        
        text = Label(frame, text="Explanation for matrix calculations:\n\n"
                     "A matrix, in a mathematical context, is a rectangular array of numbers, symbols, or expressions that are arranged in rows and columns. Matrices are often used in scientific fields such as physics, computer graphics, probability theory, statistics, calculus, numerical analysis, and more.\n"
                     "The dimensions of a matrix, A, are typically denoted as m × n. This means that A has m rows and n columns. When referring to a specific value in a matrix, called an element, a variable with two subscripts is often used to denote each element based on its position in the matrix. For example, given ai,j, where i = 1 and j = 3, a1,3 is the value of the element in the first row and the third column of the given matrix.\n"
                     "Matrix operations such as addition, multiplication, subtraction, etc., are similar to what most people are likely accustomed to seeing in basic arithmetic and algebra, but do differ in some ways, and are subject to certain constraints. Below are descriptions of the matrix operations that this calculator can perform.\n\n"

                     "Matrix addition\n\n"
                     "Matrix addition can only be performed on matrices of the same size. This means that you can only add matrices if both matrices are m × n. For example, you can add two or more 3 × 3, 1 × 2, or 5 × 4 matrices. You cannot add a 2 × 3 and a 3 × 2 matrix, a 4 × 4 and a 3 × 3, etc. The number of rows and columns of all the matrices being added must exactly match.\n"
                     "If the matrices are the same size, matrix addition is performed by adding the corresponding elements in the matrices. For example, given two matrices, A and B, with elements ai,j, and bi,j, the matrices are added by adding each element, then placing the result in a new matrix, C, in the corresponding position in the matrix:\n"
                     "a1,1 + b1,1 = 1 + 5 = 6 = c1,1\n"
                     "a1,2 + b1,2 = 2 + 6 = 8 = c1,2\n"
                     "a2,1 + b2,1 = 3 + 7 = 10 = c2,1\n"
                     "a2,2 + b2,2 = 4 + 8 = 12 = c2,2\n\n"

                     "Transpose of a matrix\n\n"
                     "The transpose of a matrix, typically indicated with a T as an exponent, is an operation that flips a matrix over its diagonal.\n"
                      " This results in switching the row and column indices of a matrix, meaning that aij in matrix A, becomes aji in AT. If necessary, refer above for a description of the notation used.\n\n"

                      "Determinant of a matrix\n\n"
                      "The determinant of a matrix is a value that can be computed from the elements of a square matrix. It is used in linear algebra, calculus, and other mathematical contexts. For example, the determinant can be used to compute the inverse of a matrix or to solve a system of linear equations.\n"
                      "There are a number of methods and formulas for calculating the determinant of a matrix. The Leibniz formula and the Laplace formula are two commonly used formulas.\n\n"

                      "Inverse of a matrix\n\n"
                      "The inverse of a matrix A is denoted as A-1, where A-1 is the inverse of A if the following is true:\n"
                      "A×A-1 = A-1×A = I, where I is the identity matrix\n\n"

                      "Determinant of a matrix\n"
                      "The determinant of a matrix is a value that can be computed from the elements of a square matrix. It is used in linear algebra, calculus, and other mathematical contexts. For example, the determinant can be used to compute the inverse of a matrix or to solve a system of linear equations.\n"
                      "There are a number of methods and formulas for calculating the determinant of a matrix. The Leibniz formula and the Laplace formula are two commonly used formulas.\n\n"
                      
                      "Matrix subtraction\n"
                      "Matrix subtraction is performed in much the same way as matrix addition, described above, with the exception that the values are subtracted rather than added. If necessary, refer to the information and examples above for a description of notation used in the example below. Like matrix addition, the matrices being subtracted must be the same size.\n"
                      "If the matrices are the same size, then matrix subtraction is performed by subtracting the elements in the corresponding rows and columns:\n\n"
                      
                      "a1,1 - b1,1 = 1 - 5 = -4 = c1,1\n"
                      "a1,2 - b1,2 = 2 - 6 = -4 = c1,2\n"
                      "a2,1 - b2,1 = 3 - 7 = -4 = c2,1\n"
                      "a2,2 - b2,2 = 4 - 8 = -4 = c2,2\n\n"


                      , font=('Times', 12)
                     
                     )
        text.configure(wraplength=600, justify='left', anchor='nw')
        text.pack()


    # /*/*/*/ Main Root for our Program /*/*/*/ 
    root = Tk()
    root.state('zoomed')
    root.title("Matrix Calculator")
    root.minsize(1350, 650)

    # ----Frame 1: Contains Option----
    f1 = Frame(root)
    f1.place(relwidth=1,relheight=0.3)
    Label(f1,text="Matrix Calculator",font=("Times",20),borderwidth = 3,
             relief="sunken").place(relx=0.38,relwidth=0.25,relheight=0.2)
    n = StringVar()
    choice = ttk.Combobox(f1, width = 27,textvariable = n)
    choice['values'] = (' Single', ' Double')
    choice.place(relx=0.46,rely=0.24,relwidth=0.1)
    choice.current(0)
    Button(f1,text="Select",fg ='blue', command=lambda: showFrame(choice)).place(relx=0.5,rely=0.34)

    # ----Frame 2: Contains Input Matrix----
    f2 = Frame(root, highlightbackground="blue",highlightthickness=1)
    f2.place(rely=0.15,relwidth=0.65,relheight=0.9)
    Label(f2,text="Input Matrix",font=("Times",17),borderwidth = 3,
             relief="sunken").place(relx=0.36,rely=0.04,relwidth=0.18,relheight=0.08)
    Label(f2,text="Number of Rows",font=("Times",13)).place(relx=0.32,rely=0.15,relwidth=0.17)
    e1 = Entry(f2,font=("Times",12), bd = 1, relief ='sunken')
    e1.place(relx=0.5,rely=0.15,relwidth=0.04)
    Label(f2,text="Number of Columns",font=("Times",13)).place(relx=0.32,rely=0.2,relwidth=0.17)
    e2 = Entry(f2,font=("Times",12), bd = 1, relief ='sunken')
    e2.place(relx=0.5,rely=0.2,relwidth=0.04)
    Button(f2,text="Continue",fg ='blue',bd = 1, relief='raised',command=lambda: showMatrix1(e1,e2,input1)).place(relx=0.4,rely=0.25,relwidth=0.07)
    input1 = Text(f2,font=("Times",14)) 
    input1.configure(insertbackground="white")
    input1.place(relx=0.3,rely=0.3,relwidth=0.3,relheight=0.3)
    Button(f2,text="Clear",fg ='green', bd = 1, relief ='raised', command=lambda: delete(input1)).place(relx=0.4,rely=0.62,relwidth=0.07,relheight=0.05)

    # ----Frame 3: Contains Output Matrix----
    f3 = Frame(root,highlightbackground="blue",highlightthickness=1)
    f3.place(relx=0.65,rely=0.15,relwidth=1,relheight=0.9)
    Label(f3,text="Output Matrix",font=("Times",17),borderwidth = 3,
             relief="sunken").place(relx=0.12,rely=0.04,relwidth=0.12,relheight=0.08)

    # Create the button
    button = Button(f3, text="Open Matrix Calculations", command=open_frame)
    button.place(relx = 0.12, rely = 0.85)

    root.mainloop()

def access_control() ->None:
    database = {'samuel senerwa':1234}

    logname = str(name.get())
    logname = logname.lower()

    logpassword = int(word.get())

    if logname in database and logpassword ==(database[logname]):
        alert.configure(text='logged in successfully !', fg ='green')
        access.configure(state='normal')
        guest.configure(state='disabled')

    elif logname in database and logpassword != (database[logname]):
        alert.configure(text='incorrect password ! retry', fg ='red')
        access.configure(state='disabled')
        name.configure(fg='black')
        word.configure(fg ='red')
        
    else:
        alert.configure(text='Invalid username and password!', fg ='red')
        name.configure(fg ='red')
        word.configure(fg ='red')
        
def LogCancel() ->None:
    Answer = askquestion(title='MATRIX CALCULATOR', message ='Cancel Log In ?')
    if Answer =='yes':
        self.destroy()
        
def guest_control() ->None:
     access.configure(state='normal')
     logIn.configure(state='disabled')

      # Function Help
def assist_help():
    new_window = Toplevel(self)
    new_window.title("Help")
    
    text = Label(new_window,text =  "Help\n\n"
                                    "1. Login first to get access to the system\n"
                                    "2. Make sure you use numerical numbers while inoutting matrices so as to avoid errors\n"
                                     "3. If you don't have an account login as a guest\n\n", font=('Times', 16))
    text.configure(wraplength=600, justify='left', anchor='nw')
    text.pack()
            


self = Tk()
self.title('MATRIX CALCULATOR')
self.minsize(1366, 768)

label = Label(self, text='Matrix Calculator', font=('Times', 16,'bold'), fg = 'green')
label.pack(side = 'top', anchor ='center')

log = Label(self, text='Log In Here', font=('Times', 14,'bold'), fg ='green')
log.place(relx = 0.15, rely = 0.1)

username = Label(self, text='username', font =('Times', 12), fg ='green')
username.place(relx = 0.15, rely = 0.15)

name = Entry(self, font=('Times', 12), width = 38, bd = 1, relief = 'sunken')
name.place(relx = 0.15, rely = 0.2, height = 35)

password = Label(self, text ='password', font =('Times', 12), fg ='green')
password.place(relx =0.15, rely = 0.25)

word = Entry(self, show ='*', font=('Times', 12), width = 38, bd = 1, relief ='sunken')
word.place(relx = 0.15, rely = 0.30, height = 35)

cancel = Button(self, text='cancel', font=('Times', 12), bd = 1, relief ='raised', width = 8, height = 2, fg ='white', bg ='red', command =LogCancel)
cancel.place(relx = 0.15, rely = 0.38)

logIn = Button(self, command =  access_control, text='log in', font=('Times', 12), bd = 1, relief ='raised', width = 8, height = 2, fg ='white', bg ='blue')
logIn.place(relx = 0.31, rely =0.38)

alert = Label(self, font=('Times', 12))
alert.place(relx = 0.15, rely = 0.55)
#guest account log in
note = Label(self, text='have no account ? log in as guest . . .', fg ='green', font=('Times', 12))
note.place(relx = 0.60, rely =0.1)

guest = Button(self, command = guest_control, text='guest', font=('Times', 12), width = 10, bd = 1, height = 2, relief ='raised', bg ='white', fg='green')
guest.place(relx = 0.67, rely = 0.20)

assist = Button(self, command = assist_help, text='help', font=('Times', 12), width = 10, bd = 1, height = 2, relief ='raised', bg ='white', fg='black')
assist.place(relx = 0.67, rely = 0.30)

clue = Label(self, text='after log In, click to access the calculator.', font=('Times', 12), fg ='green')
clue.place(relx = 0.60, rely = 0.55)

access = Button(self,text ='matrix calculator', font=('Times', 12), bd = 0, width = 20, height = 2, relief ='raised', fg ='white', bg ='blue', command = Second_Window, state='disabled' )
access.place(relx = 0.64, rely = 0.60)

self.mainloop()



