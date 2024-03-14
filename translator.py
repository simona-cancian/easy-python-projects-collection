from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator


root = Tk()
root.title("Translator")
root.geometry("1080x400")

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(200, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        translator = Translator()
        if text_:
            detected_language = detect(str(text_))
            print("Detected Language:", detected_language)
            print(type(text_), text_)
            translation = translator.translate(text_, src=detected_language, dest=c3).text
            text2.delete(1.0, END)
            text2.insert(END, translation)
    except Exception as e:
        messagebox.showerror("Translation Error", "An error occurred during translation. Please try again.")
        print(e)


# Icon
image_icon = PhotoImage(file="translate.png")
# <a href="https://www.flaticon.com/free-icons/translate" title="translate icons">Translate icons created by Pixel perfect - Flaticon</a>
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="exchange.png")
# <a href="https://www.flaticon.com/free-icons/double-arrow" title="double arrow icons">Double arrow icons created by Pixel perfect - Flaticon</a>
image_label = Label(root, image=arrow_image, width=150, bg="white")
image_label.place(x=460, y=50)

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2",
                   bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
