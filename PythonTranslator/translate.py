#Note:- this code is to be run only on pycharm
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(0, 0)
root.title('Language Translator by Hehe')
root.configure(bg='skyblue')

Label(root, text="Language Translator", font="Arial 20 bold", bg='skyblue').pack()

# Input
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

# Output
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)
Output_text = Text(root, font='arial 13', height=8, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=580, y=125)

# Language Dropdown
language = list(LANGUAGES.values())
lang_dict = {v: k for k, v in LANGUAGES.items()}  # Reverse mapping: name -> code

dest_language = ttk.Combobox(root, values=language, width=22)
dest_language.place(x=130, y=160)
dest_language.set('Choose Language')

# Translate Function
def translate():
    translator = Translator()
    try:
        lang_name = dest_language.get()
        lang_code = lang_dict.get(lang_name.lower())
        if not lang_code:
            Output_text.delete(1.0, END)
            Output_text.insert(END, "Please select a valid language.")
            return
        translated = translator.translate(text=Input_text.get(), dest=lang_code)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)
    except Exception as e:
        Output_text.delete(1.0, END)
        Output_text.insert(END, f"Translation failed: {str(e)}")

# Translate Button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5,command=translate, bg='orange', activebackground='green')
trans_btn.place(x=445, y=125)

root.mainloop()
