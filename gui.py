import tkinter as tk
from tkinter import filedialog, messagebox
import pdf2final_list
import text2ppt
import shutil
import os

def generate_presentation(*args):
    global label, ent, window, exit_button
    exit_button.config(text='Processing...')
    try:
        intext = ent.get()
        ent.destroy()
        label.destroy()
        window.update()
        if "," in intext:
            l1 = [_.strip() for _ in intext.split(",")]
        else:
            l1 = [intext]
        print(l1)
        x = pdf2final_list.process(l1)
        print("\n\n", x)
        text2ppt.presentate(x)
        file_path = filedialog.asksaveasfilename(defaultextension='.pptx',
                                                 filetypes=[('PowerPoint files', '*.pptx'),
                                                            ('All files', '*.*')])
        shutil.copy("PPT.pptx", file_path)
        messagebox.showinfo("SUCCESS", "File Saved Successfully")
        os.startfile(file_path)
    except Exception as e:
        messagebox.showerror("ERROR", e)
    exit_button.config(text='Exit')
    ent = tk.Entry(window, font=('Arial', 10), fg='black', bg='white', borderwidth=2, relief='groove')
    ent.grid(row=2, column=0, pady=15, sticky="ew", padx=30)
    label = tk.Label(window, text='Enter comma separated topics', font=('Arial', 24, 'bold'), fg='black', bg='white')
    label.grid(row=1, column=0, pady=30, padx=30, sticky="ew")
    ent.bind('<Return>', generate_presentation)

# Create the Tkinter window
window = tk.Tk()
window.title("Printing Service")
window.geometry("600x375")  # Increase the window size
window.configure(bg='white')

# Create a label asking for comma separated topics
label = tk.Label(window, text='Enter comma-separated topics', font=('Arial', 27, 'bold'), fg='black', bg='white')
label.grid(row=1, column=0, pady=30, padx=30, sticky="ew")

# Create an entry widget for input
ent = tk.Entry(window, font=('Arial', 15), fg='black', bg='white', borderwidth=2, relief='groove')
ent.grid(row=2, column=0, pady=15, sticky="ew", padx=30)

# Create an exit button widget
exit_button = tk.Button(window, text='Exit', command=window.quit, font=('Arial', 18), fg='white', bg='red', padx=15, pady=7, borderwidth=2, relief='groove')
exit_button.grid(row=3, column=0, pady=30, padx=60, sticky="ew")

# Add a hover effect to the exit button
def on_enter_exit(e):
    exit_button.config(bg='darkred')
def on_leave_exit(e):
    exit_button.config(bg='red')

exit_button.bind('<Enter>', on_enter_exit)
exit_button.bind('<Leave>', on_leave_exit)

ent.bind('<Return>', generate_presentation)

# Run the Tkinter event loop
window.mainloop()
