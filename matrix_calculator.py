from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np


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
        Label(f2,text="Number of Rows",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.32,rely=0.15,relwidth=0.17)
        e1 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e1.place(relx=0.5,rely=0.15,relwidth=0.04)
        Label(f2,text="Number of Columns",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.32,rely=0.2,relwidth=0.17)
        e2 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e2.place(relx=0.5,rely=0.2,relwidth=0.04)        
        Button(f2,text="Continue",bg="#1DA1F2",command=lambda: showMatrix1(e1,e2,input1)).place(relx=0.4,rely=0.25,relwidth=0.07)
        input1 = Text(f2,bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold"))
        input1.configure(insertbackground="#ffffff")
        input1.place(relx=0.3,rely=0.3,relwidth=0.3,relheight=0.3)   
        Button(f2,text="Clear",bg="#1DA1F2",command=lambda: delete(input1)).place(relx=0.4,rely=0.62,relwidth=0.07,relheight=0.05)
    elif c == ' Double':             
        Label(f2,text="Matrix A",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold")).place(relx=0.15,rely=0.14,relwidth=0.17)
        Label(f2,text="Number of Rows",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.06,rely=0.2,relwidth=0.17)
        e1 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e1.place(relx=0.24,rely=0.2,relwidth=0.04)
        Label(f2,text="Number of Columns",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.06,rely=0.24,relwidth=0.17)
        e2 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e2.place(relx=0.24,rely=0.24,relwidth=0.04)
        Label(f2,text="Matrix B",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold")).place(relx=0.65,rely=0.14,relwidth=0.17)
        Label(f2,text="Number of Rows",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.56,rely=0.2,relwidth=0.17)
        e3 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e3.place(relx=0.74,rely=0.2,relwidth=0.04)
        Label(f2,text="Number of Columns",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.56,rely=0.24,relwidth=0.17)
        e4 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
        e4.place(relx=0.74,rely=0.24,relwidth=0.04)
        Button(f2,text="Continue",bg="#1DA1F2",command=lambda: showMatrix2(e1,e2,e3,e4,input1,input2)).place(relx=0.45,rely=0.28,relwidth=0.07)
        input1 = Text(f2,bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold"))  
        input1.configure(insertbackground="#ffffff")
        input2 = Text(f2,bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold")) 
        input1.configure(insertbackground="#ffffff")
        input2.configure(insertbackground="#ffffff",border=10)
        input1.place(relx=0.1,rely=0.35,relwidth=0.3,relheight=0.3)     
        input2.place(relx=0.55,rely=0.35,relwidth=0.3,relheight=0.3) 
        Button(f2,text="Clear",bg="#1DA1F2",command=lambda: delete(input1)).place(relx=0.2,rely=0.68,relwidth=0.1,relheight=0.04)
        Button(f2,text="Clear",bg="#1DA1F2",command=lambda: delete(input2)).place(relx=0.65,rely=0.68,relwidth=0.1,relheight=0.04)
                
# ----Clearing contents of text box:----       
def delete(textBox):
    textBox.delete(1.0,END)

# ----Clearing contents of Frame:---- 
def clearFrame(frame):
    for w in frame.winfo_children():
        print(w)
        w.place_forget()
    if frame == f2:
        Label(f2,text="Input Matrix",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold"),borderwidth = 3,
         relief="sunken").place(relx=0.36,rely=0.04,relwidth=0.18,relheight=0.08)
    elif frame == f3:
        Label(f3,text="Output Matrix",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold"),borderwidth = 3,
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
    output1 = Text(f3,bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold"))
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
    Label(f3,text="Determinant of Matrix Entered: ",bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold")).place(relx=0.1,rely=0.4,relheight=0.08)
    Label(f3,text=str(d),bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold")).place(relx=0.18,rely=0.5,relheight=0.09,relwidth=0.04)



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
    Button(f2,text="Transpose",bg="#192734",fg="#2069e0",font=("italic",15,"bold"),highlightthickness=10,highlightbackground="#2069e0",command=lambda: calTrans(row,col,input1)).place(relx=0.28,rely=0.7,relwidth=0.15,relheight=0.1)
    Button(f2,text="Inverse",bg="#192734",fg="#2069e0", font=("italic",15,"bold"),command=lambda: calInverse(row,col,input1)).place(relx=0.46,rely=0.7,relwidth=0.15,relheight=0.1)
    Button(f2,text="Determinant", bg="#192734",fg="#2069e0",font=("italic",15,"bold"),command=lambda: calDet(row,col,input1)).place(relx=0.36 ,rely=0.82,relwidth=0.15,relheight=0.1)    
    
def showMatrix2(e1,e2,e3,e4,input1,input2):
    if checkEmpty(e1,e2):
        return
    elif checkEmpty(e3,e4):
        return
    row1 = int(e1.get())
    col1 = int(e2.get())
    row2 = int(e3.get())
    col2 = int(e4.get())        
    Button(f2,text="Addition[A+B]",bg="#192734",fg="#2069e0",font=("italic",12,"bold"),command=lambda: matrixAdd(row1,col1,row2,col2,input1,input2)).place(relx=0.28,rely=0.73,relwidth=0.18,relheight=0.08)
    Button(f2,text="Substraction[A-B]",bg="#192734",fg="#2069e0",font=("italic",12,"bold"), command=lambda: matrixSub(row1,col1,row2,col2,input1,input2)).place(relx=0.49,rely=0.73,relwidth=0.18,relheight=0.08)
    Button(f2,text="Multiplication[A*B]",bg="#192734",fg="#2069e0",font=("italic",12,"bold"), command=lambda: matrixMul(row1,col1,row2,col2,input1,input2)).place(relx=0.28 ,rely=0.84,relwidth=0.18,relheight=0.08)
    Button(f2,text="Substraction[B-A]",bg="#192734",fg="#2069e0",font=("italic",12,"bold"),command = lambda: matrixSub(row2,col2,row1,col1,input2,input1)).place(relx=0.49 ,rely=0.84,relwidth=0.18,relheight=0.08)
    
        
# /*/*/*/ Main Root for our Program /*/*/*/ 
root = Tk()
root.state('zoomed')
root.title("Matrix Calculator")
root.minsize(1350, 650)

# ----Frame 1: Contains Option----
f1 = Frame(root,bg="#181818")
f1.place(relwidth=1,relheight=0.3)
Label(f1,text="Matrix Calculator",bg="#181818",fg="#1DA1F2",font=("Helvetica",20,"bold"),borderwidth = 3,
         relief="sunken").place(relx=0.38,relwidth=0.25,relheight=0.2)
n = StringVar()
choice = ttk.Combobox(f1, width = 27,textvariable = n)
choice['values'] = (' Single', ' Double')
choice.place(relx=0.46,rely=0.24,relwidth=0.1)
choice.current(0)
Button(f1,text="Select",bg="#657786",command=lambda: showFrame(choice)).place(relx=0.5,rely=0.34)

# ----Frame 2: Contains Input Matrix----
f2 = Frame(root,bg="#192734",highlightbackground="#001933",highlightthickness=1)
f2.place(rely=0.15,relwidth=0.65,relheight=0.9)
Label(f2,text="Input Matrix",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold"),borderwidth = 3,
         relief="sunken").place(relx=0.36,rely=0.04,relwidth=0.18,relheight=0.08)
Label(f2,text="Number of Rows",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.32,rely=0.15,relwidth=0.17)
e1 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
e1.place(relx=0.5,rely=0.15,relwidth=0.04)
Label(f2,text="Number of Columns",bg="#192734",fg="#E1E8ED",font=("Times",13,"bold","italic")).place(relx=0.32,rely=0.2,relwidth=0.17)
e2 = Entry(f2,bg="#657786",fg="#E1E8ED",font=("Helvetica",12,"bold"))
e2.place(relx=0.5,rely=0.2,relwidth=0.04)
Button(f2,text="Continue",bg="#1DA1F2",command=lambda: showMatrix1(e1,e2,input1)).place(relx=0.4,rely=0.25,relwidth=0.07)
input1 = Text(f2,bg="#181818",fg="#F5F8FA",font=("helvetica",14,"bold")) 
input1.configure(insertbackground="#ffffff")
input1.place(relx=0.3,rely=0.3,relwidth=0.3,relheight=0.3)
Button(f2,text="Clear",bg="#1DA1F2",command=lambda: delete(input1)).place(relx=0.4,rely=0.62,relwidth=0.07,relheight=0.05)

# ----Frame 3: Contains Output Matrix----
f3 = Frame(root,bg="#192734",highlightbackground="#001933",highlightthickness=1)
f3.place(relx=0.65,rely=0.15,relwidth=1,relheight=0.9)
Label(f3,text="Output Matrix",bg="#192734",fg="#2069e0",font=("Helvetica",17,"bold"),borderwidth = 3,
         relief="sunken").place(relx=0.12,rely=0.04,relwidth=0.12,relheight=0.08)
root.mainloop()