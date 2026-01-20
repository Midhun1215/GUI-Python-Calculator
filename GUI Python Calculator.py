#Importing tkinter for the Graphical User Interface (GUI) to make the Calculator

import tkinter as tk
from tkinter import font

window = tk.Tk()

#Window settings for the outline of the calculator

window.title("Simple Calculator")
window.geometry("700x700")

#Design of the Entry Box for the calculator

window_entry = tk.Entry(font=('Arial', 20), fg='white', bg='black', borderwidth=10)

#Functions for the Buttons of the Calculator

def click(Number):
  current_number = window_entry.get()
  window_entry.delete(0, tk.END)
  window_entry.insert(0, str(current_number) + str(Number))

def clear():
  window_entry.delete(0, tk.END)
  
def delete():
  window_entry.delete(len(window_entry.get()) -1,tk.END)

def decimal_point():
     window_entry.insert(tk.END, '.')       
    
def add():
  global first_number
  global operation
  global no_digit
  first_number = window_entry.get()
  no_digit = int(len(first_number))
  window_entry.insert(tk.END,'+')
  operation = "add"
def subtract():
  global first_number
  global operation
  global no_digit
  first_number = window_entry.get()
  no_digit = int(len(first_number))
  window_entry.insert(tk.END,'-')
  operation = "subtract"

def multiply():
  global first_number
  global operation
  global no_digit
  first_number = window_entry.get()
  no_digit = int(len(first_number))
  window_entry.insert(tk.END,'x')
  operation = "multiply"
  
def divide():
  global first_number
  global operation
  global no_digit
  first_number = window_entry.get()
  no_digit = int(len(first_number))
  window_entry.insert(tk.END,'÷')
  operation = "divide"
   
def equal():
  global second_number
  second_number = window_entry.get()
  second_number = second_number[no_digit + 1 :]
  window_entry.delete(0, tk.END)

  # Choosing the right operation to perform:
  
  if operation == "add":
    sum = float(first_number) + float(second_number)
    if (sum - int(sum)) == 0:
      sum = int(sum)
    window_entry.insert(0, str(sum))
  elif operation == "subtract":
    difference = float(first_number) - float(second_number)
    if (difference - int(difference)) == 0:
      difference = int(difference)
    window_entry.insert(0, str(difference))
    
  elif operation == "multiply":
    product = float(first_number) * float(second_number)
    if (product- int(product)) == 0:
      product = int(product)
    window_entry.insert(0, str(product))
    
  elif operation == "divide":    
    
    #To check if the Second number is zero, due to a prperty in division that the second number should never  be 0
    
    if second_number == '0':
      window_entry.insert(0, 'ERROR')
      
    else:
      quotient = float(first_number) / float(second_number)
      if (quotient - int(quotient)) == 0:
        quotient = int(quotient)
      window_entry.insert(0, str(quotient))
      
#Design of Each button

button_1 = tk.Button(padx=45 , pady=30,font=('Arial', 25),fg='orange',bg='black',text='1',command=lambda: click(1))

button_2 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='2',command=lambda: click(2))

button_3 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='3',command=lambda: click(3))

button_4 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange', bg='black',text='4',command=lambda:click(4))

button_5 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='5',command=lambda: click(5))

button_6 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='6',command=lambda: click(6))

button_7 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='7',command=lambda: click(7))

button_8 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black', text='8',command=lambda:click(8))

button_9 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='9',command=lambda: click(9))

button_0 = tk.Button(padx=45,pady=30,font=('Arial', 25),fg='orange',bg='black',text='0',command=lambda: click(0))

button_clear = tk.Button(padx=25,pady=35,font=('Arial', 20),fg='orange',bg='black',text='Clear',command=clear)

button_delete = tk.Button(padx=15,pady=12,font=('Arial', 20),fg='orange',bg='black',text='Delete',command=delete)

button_add = tk.Button(padx=42,pady=30,font=('Arial', 25),fg='orange',bg='black',text='+',command=add)

button_equal = tk.Button(padx=35,pady=258,font=('Arial', 25),fg='orange',bg='black',text='=',command=equal)

button_subtract = tk.Button(padx=46,pady=30,font=('Arial', 25),fg='orange',bg='black',text='-',command=subtract)

button_multiply = tk.Button(padx=44,pady=30,font=('Arial', 25),fg='orange',bg='black',text='x',command=multiply)

button_divide = tk.Button(padx=42,pady=30,font=('Arial', 25),fg='orange',bg='black',text='÷',command=divide)

button_decimal = tk.Button(padx=50,pady=30,font=('Arial', 25),fg='orange',bg='black',text='.',command=decimal_point)

#Positioning of All Buttons

window_entry.grid(column=0, row=0 ,columnspan = 3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_clear.grid( row = 4, column=2)
button_delete.grid(row=0, column=3)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row = 0 ,column=4, rowspan = 5)
button_decimal.grid(row=4, column=0)

tk.mainloop()