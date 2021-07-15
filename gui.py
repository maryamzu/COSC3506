import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
  
def send_message():
    {
     }
  
# message editor
window = tk.Tk()
window.title("Message Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_send = tk.Button(fr_buttons, text="Send", command=send_message)
btn_send.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


'''window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text = "Choose recipient:", 
        font = ("Times New Roman", 10)).grid(column = 0, 
        row = 15, padx = 10, pady = 25)
  
n = tk.StringVar()
userList = ttk.Combobox(window, width = 27, 
                            textvariable = n)

# Adding combobox drop down list
userList['values'] = ('Paul', 'Sreemathi', 'Maryam', 'Helia')
userList.grid(column = 1, row = 15)

# Shows list item as default
userList.current(1) 
'''
window.mainloop()
