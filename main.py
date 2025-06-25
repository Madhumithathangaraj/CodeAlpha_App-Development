'''import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import style

if__name__ == '__main__':

 #create the main GUI window
 root = tk.TK()
 root.title('Flashcards App')
 root.geometry('500x400')

#apply styling to the GUI elements
style = style(theme='superhero')
style.configure('TLabel', font=('Tkdefaultfont',18))
style.configure('TButton', font =('Tkdefaultfont',16))

#set up variable
set_name_var = tk.StringVar()
word_var = tk.StringVar()
definition_var + tk.StringVar()

#create notebook widget
notebokk = ttk.Notebook(root)
notebokk.pack(fill='both',expand=True)

#create the "create set" tab and its content
create_set_frame = ttk.Frame(notebook)
notebook.add(create_set_frame,text="Create Set")

#label and entry widget set name,word and definition
ttk.Label(create_set_frame,text='Set Name:').pack(padx=5,pady=5)
ttk.Entry(create_set_frame,textvariable=set_name_var,width=30).pack(padx=5,pady=5)
ttk.Label(create_set_frame,text='word:').pack(padx=5,pady=5)
ttk.Entry(create_set_frame,textvariable=set_name_var,width=30).pack(padx=5,pady=5)
ttk.Label(create_set_frame,text='definition:').pack(padx=5,pady=5)
ttk.Entry(create_set_frame,textvariable=set_name_var,width=30).pack(padx=5,pady=5)

#button to add a word to the set (command=add_word) => for the next part
ttk.Button(create_set_frame,text= 'Add word').pack(padx=5,pady=10)

#Button to save the set 
ttk.Button(create_set_frame,text='Save set').pack(padx=5,pady=10)

#create the "select set" tab and its content
select_set_frame = ttk.Frame(notebook)
notebook.add(select_set_frame,text="Select Set")

#combobox widget for selecting existing flashcard sets


root.mainloop()'''
import tkinter as tk

# Sample flashcards
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Germany?", "answer": "Berlin"},
    {"question": "What is the capital of Italy?", "answer": "Rome"}
]

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard App")
        self.index = 0
        self.showing_answer = False

        # Display area
        self.label = tk.Label(master, text="", font=("Arial", 18), wraplength=400, justify="center")
        self.label.pack(pady=20)

        # Navigation buttons
        button_frame = tk.Frame(master)
        button_frame.pack()

        self.prev_button = tk.Button(button_frame, text="Previous", command=self.prev_card)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.flip_button = tk.Button(button_frame, text="Flip", command=self.flip_card)
        self.flip_button.grid(row=0, column=1, padx=10)

        self.next_button = tk.Button(button_frame, text="Next", command=self.next_card)
        self.next_button.grid(row=0, column=2, padx=10)

        self.update_card()

    def update_card(self):
        card = flashcards[self.index]
        self.label.config(text=card["question"])
        self.showing_answer = False

    def flip_card(self):
        card = flashcards[self.index]
        if self.showing_answer:
            self.label.config(text=card["question"])
        else:
            self.label.config(text=card["answer"])
        self.showing_answer = not self.showing_answer

    def next_card(self):
        if self.index < len(flashcards) - 1:
            self.index += 1
            self.update_card()

    def prev_card(self):
        if self.index > 0:
            self.index -= 1
            self.update_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()



