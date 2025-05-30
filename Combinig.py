import sqlite3
import customtkinter as ctk

with sqlite3.connect('Teacher_Data.db') as conn:
    cursor = conn.cursor()
    
#-------All Search By Funtions    
def searchbyId(Id, cursor):
    cursor.execute('SELECT * FROM TeacherData WHERE Id = ?',
                   (Id,))
    result = cursor.fetchone()
    
    return[result] if result is not None else[]
    
def searchbyname(name, cursor):        
        cursor.execute('SELECT * FROM TeacherData WHERE NAME LIKE ?', 
                       ('%'+ name+'%',))
        result = cursor.fetchall()
        
        return[result] if result is not None else[]

def searchbynumber(number, cursor):
    cursor.execute('SELECT * FROM TeacherData WHERE Phone = ?',
                   (number,))
    result = cursor.fetchone()
    
    return[result] if result is not None else[]
           
def searchbyDepart(Depart, cursor):
    cursor.execute('SELECT * FROM TeacherData WHERE Department = ?',
                   (Depart,))
    result = cursor.fetchall()
    
    return[result] if result is not None else [] 
           

def searchbyBranch(Branch, cursor):
    cursor.execute('SELECT * FROM TeacherData WHERE Branch = ?',
                   (Branch,))
    result = cursor.fetchall()
    
    return[result] if not None else []     


def searchbycity(City, cursor):
    cursor.execute('SELECT * FROM TeacherData WHERE City = ?',
                   (City,))
    result = cursor.fetchall()
    
    return[result] if not None else []    

# -------- ADDING GUI 

app = ctk.CTk()
app.title("MasterPiece")
app.geometry("400x150")
app.grid_columnconfigure((0,1,2), weight=1)
    
#---------USING BUTTON CLICKER
    
def changeHandler(values):
    print(values) # Id select by the user
    entry.configure(placeholder_text = values) 
    # entry.delete(0, ctk.END)
    
def buttonClicker():
    selected_field = comboBox.get()
    userInput = entry.get() #Typed by the user
    
    resultBox.delete("0.0", ctk.END)
       
    if selected_field == 'id':
        result = searchbyId(userInput, cursor)
    elif selected_field == 'Name':
        result = searchbyname(userInput, cursor)
    elif selected_field == 'Phone':
        result = searchbynumber(userInput, cursor)
    elif selected_field == 'Department':
        result = searchbyDepart(userInput, cursor)
    elif selected_field == 'City':
        result = searchbycity(userInput, cursor)                      
    elif selected_field == 'Branch':
        result = searchbyBranch(userInput, cursor)        
    else:
        result = ['Invalid field selceted']
    
    if result:
        for row in result:
            print(row)
    else:
        print("No result found")        
                
def fieldSearch():
    global entry, comboBox, resultBox
    comboBox = ctk.CTkComboBox(master=app, 
                       values=["Id","Name","Department",
                      "Branch", "City","email","Phone"],
                      command=changeHandler
                      )
    comboBox.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    
    entry = ctk.CTkEntry(app, placeholder_text="Id")
    entry.grid(row = 0, column = 1, pady = 10, sticky = 'w')
    
    resultBox = ctk.CTkTextbox(app, height=100, width=300)
    resultBox.grid(row =1, column = 0, padx = 10, pady = 10)
    
    btn = ctk.CTkButton(master=app,text="Submit", border_width=2,
                        width=50,command = buttonClicker)

    btn.grid(row = 0, column = 2, pady = 10, sticky = 'w')
    
fieldSearch()    
app.mainloop()