import random
import tkinter as tk

# Predefined quotes list (text, author)
QUOTES = [
    ("Be yourself; everyone else is already taken.", "Oscar Wilde"),
    ("Two things are infinite: the universe and human stupidity.", "Albert Einstein"),
    ("So many books, so little time.", "Frank Zappa"),
    ("A room without books is like a body without a soul.", "Marcus Tullius Cicero"),
    ("Be the change you wish to see in the world.", "Mahatma Gandhi")
]

class QuoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Quote Generator")
        self.configure(padx=30, pady=30, bg="#f4f4f9")

        self.quote_text = tk.StringVar()
        self.quote_label = tk.Label(self, textvariable=self.quote_text,
                                    wraplength=400, font=("Helvetica", 16),
                                    fg="#333333", bg=self["bg"], justify="center")
        self.quote_label.pack(pady=(0,20))

        self.btn = tk.Button(self, text="New Quote", command=self.new_quote,
                             font=("Helvetica", 14), bg="#556B2F", fg="white",
                             activebackground="#6B8E23", padx=10, pady=5)
        self.btn.pack()
        
        self.new_quote()  # Display a random quote on start

    def new_quote(self):
        q, a = random.choice(QUOTES)
        self.quote_text.set(f"“{q}”\n\n— {a}")

if __name__ == "__main__":
    app = QuoteApp()
    app.mainloop()
