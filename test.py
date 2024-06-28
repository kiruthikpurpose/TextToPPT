from openai import AsyncOpenAI
import asyncio
import time

async def generate_openai_summary(prompt):
    client = AsyncOpenAI(api_key="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")
    completion = await client.completions.create(
        model="davinci-codex",
        prompt=prompt,
        max_tokens=200,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    response = completion.choices[0].text.strip()
    return response

def process(topic_list):
    data_list = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for topic in topic_list:
        dct = {}
        summary = loop.run_until_complete(generate_openai_summary("I am giving you a topic. I want a summary of " + topic))
        dct["Topic"] = topic
        dct["Summary"] = summary.split("Summary:")[1].split("\n")
        print(dct)
        code = loop.run_until_complete(generate_openai_summary("I am giving you a topic... " + topic))
        code = code.replace("```python", "```")
        print(code)
        try:
            code = (code.split("```"))[1].split("```")[0]
        except:
            pass
        dct["Code"] = code
        data_list.append(dct)
        if len(topic_list) > 1:
            time.sleep(55)
    return data_list

# Example usage
'''topics = ["What's the most popular ski resort in Europe?", "Another topic"]
result = process(topics)
print(result)'''


import tkinter as tk
from tkinter import filedialog, messagebox
import pdf2final_list
import text2ppt
import shutil
import os

def generate_presentation(*args):
    try:
        intext = ent.get()
        ent.destroy()
        label.destroy()
        window.update()
        
        if "," in intext:
            topics = [topic.strip() for topic in intext.split(",")]
        else:
            topics = [intext]
        
        presentation_data = pdf2final_list.process(topics)
        text2ppt.presentate(presentation_data)
        
        file_path = filedialog.asksaveasfilename(defaultextension='.pptx',
                                                 filetypes=[('PowerPoint files', '*.pptx'),
                                                            ('All files', '*.*')])
        if file_path:
            shutil.copy("PPT.pptx", file_path)
            messagebox.showinfo("Success", "Presentation saved successfully.")
            os.startfile(file_path)
        else:
            messagebox.showwarning("Warning", "No file path selected.")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        exit_button.config(text='Exit')
        ent = tk.Entry(window, font=('Arial', 24, 'bold'), fg='#f2f2f2', bg='#333333', borderwidth=0, relief='groove')
        ent.grid(row=2, column=0, pady=30, sticky="news", padx=20)
        label = tk.Label(window, text='Enter comma separated topics', font=('Arial', 12, 'bold'), fg='#333333', bg='#f2f2f2')
        label.grid(row=1, column=0, pady=20, padx=20, sticky="news")
        ent.bind('<Return>', generate_presentation)

# Create the Tkinter window
window = tk.Tk()
window.title("Presentation Generator")
window.configure(bg='#f2f2f2')

# Create a label asking for comma separated topics
label = tk.Label(window, text='Enter Comma-Separated Topics', font=('Arial', 20, 'bold'), fg='#333333', bg='#f2f2f2')
label.grid(row=0, column=0, pady=(50, 20), padx=20, sticky="ew")

# Create an entry widget for input
ent = tk.Entry(window, font=('Arial', 24, 'bold'), fg='#f2f2f2', bg='#333333', borderwidth=0, relief='groove')
ent.grid(row=1, column=0, pady=(0, 20), sticky="ew", padx=20)

# Create a generate button widget
generate_button = tk.Button(window, text='Generate Presentation', command=generate_presentation, font=('Arial', 14), fg='#f2f2f2', bg='#333333', padx=20, pady=10, borderwidth=0, relief='groove')
generate_button.grid(row=2, column=0, pady=(0, 20), padx=20, sticky="ew")

# Create an exit button widget
exit_button = tk.Button(window, text='Exit', command=window.quit, font=('Arial', 14), fg='#f2f2f2', bg='#333333', padx=20, pady=10, borderwidth=0, relief='groove')
exit_button.grid(row=3, column=0, pady=(0, 50), padx=20, sticky="ew")

# Add hover effects to buttons
def on_enter(event):
    event.widget.config(bg='#555555')

def on_leave(event):
    event.widget.config(bg='#333333')

generate_button.bind('<Enter>', on_enter)
generate_button.bind('<Leave>', on_leave)
exit_button.bind('<Enter>', on_enter)
exit_button.bind('<Leave>', on_leave)

# Run the Tkinter event loop
window.mainloop()
