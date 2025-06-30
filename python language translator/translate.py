from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
root = Tk()
root.geometry('1100x320')
root.resizable(0,0)
root.iconbitmap('logo simpli.ico')
root['bg']= 'skyblue'

root.title('language translator by hehe')
Label(root ,text="Language translator", font="Arial 20 bold").pack()

# creating a input box and a output area
Label(root, text="enter text",font='arial 13 bold',bg='white smoke').place(x=165,y=90)

Input_text= Entry(root,width=60)
Input_text.place(x=30,y=130)
Input_text.get()

Label(root, text="output",font='arial 13 bold',bg='white smoke').place(x=780,y=90)
Output_text = Text(root,font='arial 13',height=11,wrap=WORD,padx=5,pady=5,width=50)
Output_text.place(x=500,y=100)

#giving the options for target language translation
language = list(LANGUAGES.values())
dest_language =ttk.Combobox(root, values= language, width=22)
dest_language.place(x=130,y=160)
dest_language.set('choose lanhguage')

def translate():
    translator = Translator()
    translated = translator.translate(text= Input_text.get(), dest= dest_language.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

trans_btn = Button(root,text= 'Translate', font='arial 12 bold', pady=5 ,command=translate,bg='orange', activebackground='green')
trans_btn.place(x=445,y=180)

root.mainloop()
