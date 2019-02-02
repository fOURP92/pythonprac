#----Calculator----
import tkinter as tk

window = tk.Tk()
window.title("fOURP's Calculator.")
window.geometry('200x200')
expression = ""
choice = True
var = tk.StringVar()
var_entry = tk.Entry(window , text = 'var', textvariable = var)
var_entry.grid(row = 0, column = 0, columnspan = 10)
var_entry.focus()
var.set(expression)
def press(num):
   global expression
   expression = expression + str(num)
   var.set(expression)
def clear():
    global expression 
    expression = "" 
    var.set("") 
def equals():
   try:
      global expression
      total = str(eval(expression))
      var.set(total)
   except:
      var.set(" Error ") 
      expression = "" 



btn0 = tk.Button(window, text = '0', command = lambda: press(0), height = 1, width = 7)
btn0.grid(row = 5, column = 1)
btn1 = tk.Button(window, text = '7', command = lambda: press(7), height = 1, width = 7)
btn1.grid(row = 2, column = 0)
btn2 = tk.Button(window, text = '8', command = lambda: press(8), height = 1, width = 7)
btn2.grid(row = 2, column = 1)
btn3 = tk.Button(window, text = '9', command = lambda: press(9), height = 1, width = 7)
btn3.grid(row = 2, column = 2)
btn4 = tk.Button(window, text = '4', command = lambda: press(4), height = 1, width = 7)
btn4.grid(row = 3, column = 0)
btn5 = tk.Button(window, text = '5', command = lambda: press(5), height = 1, width = 7)
btn5.grid(row = 3, column = 1)
btn6 = tk.Button(window, text = '6', command = lambda: press(6), height = 1, width = 7)
btn6.grid(row = 3, column = 2)
btn7 = tk.Button(window, text = '1', command = lambda: press(1), height = 1, width = 7)
btn7.grid(row = 4, column = 0)
btn8 = tk.Button(window, text = '2', command = lambda: press(2), height = 1, width = 7)
btn8.grid(row = 4, column = 1)
btn9 = tk.Button(window, text = '3', command = lambda: press(3), height = 1, width = 7)
btn9.grid(row = 4, column = 2)
btnClear = tk.Button(window, text = 'C', command = clear, height = 1, width = 7)
btnClear.grid(row = 5, column = 2)
btnMultiply = tk.Button(window, text = '*', command = lambda: press("*"), height = 1, width = 2)
btnMultiply.grid(row = 2, column = 3)
btnAdd = tk.Button(window, text = '+', command = lambda: press("+"), height = 1, width = 2)
btnAdd.grid(row = 3, column = 3)
btnSub = tk.Button(window, text = '-', command = lambda: press("-"), height = 1, width = 2)
btnSub.grid(row = 4, column = 3)
btnDivide = tk.Button(window, text = '/', command = lambda: press("/"), height = 1, width = 2)
btnDivide.grid(row = 5, column = 3)
btnEquals = tk.Button(window, text = '=' , command = equals, height = 1, width = 7)
btnEquals.grid(row = 5, column = 0)
 
window.mainloop()


      





