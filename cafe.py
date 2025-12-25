import tkinter as tk
from tkinter import messagebox

menu = {
     'Coffee': 50,
     'Tea': 30,
     'Burger': 40,
     'Sandwich': 60,
     'Cake': 400,
     'Pastry': 60,
}

root = tk.Tk()
root.title('Cafe Management System')
root.geometry('500x500')
 
tk.Label(root, text='Cafe Management System', font=('Arial', 18, 'bold')).pack(pady=10)


menu_frame = tk.LabelFrame(root, text='Menu', font=('Arial', 14))
menu_frame.pack(pady=10, fill='x', padx=20)


vars_dict = {}
for item, price in menu.items():
    var = tk.IntVar()
    tk.Checkbutton(menu_frame, text=f'{item} - Rs {price}', variable=var,
                   font=('Arial',12)).pack(anchor='w', padx=10)
    vars_dict[item] = var
    

def calculate_bill():
    total = 0
    receipt_text = '----- Receipt -----\n'
    for item, var in vars_dict.items():
        if var.get() == 1:
            total += menu[item]
            receipt_text += f'{item} - Rs {menu[item]}\n'
    
    if total == 0:
        messagebox.showwarning('No Selection', "Please select at least one item!")   
        return
    
    receipt_text += f"\nTotal Bill: Rs {total}\n--------------------"
    
    receipt_area.delete('1.0', tk.END)
    receipt_area.insert(tk.END, receipt_text)
    
    
    total_label.config(text=f"Total Bill: Rs {total}")


tk.Button(root, text='Generate Bill', command=calculate_bill, bg='blue', fg='white',
          font=('Arial', 12)).pack(pady=10)   


receipt_area = tk.Text(root, height=10, width=40, font=('Arial',12))
receipt_area.pack(pady=10)

total_label = tk.Label(root, text="Total Bill: Rs 0", font=('Arial', 14, 'bold'), fg='green')
total_label.pack(pady=10)

root.mainloop()
