import _tkinter
import tkinter
import customtkinter
import time
from source_text import all_texts

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("green")

source_text = all_texts[1]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.source_text = source_text
        self.geometry('800x800')
        self.title('Typing Speed Test')
        self.config(padx=50, pady=100)
        self.textbox = customtkinter.CTkEntry(master=self,
                                              height=200,
                                              width=400)
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")
        self.textbox.bind('<space>', lambda event: self.return_text())
        self.textbox.bind('<Return>', lambda event: self.correct_words())
    def display_text(self):
        self.reading_text = customtkinter.CTkTextbox(master=self,
                                                     width=600,
                                                     height=200,
                                                     corner_radius=10,
                                                     fg_color=("white", "gray"),
                                                     wrap='word',
                                                     font=("Ardoise Std", 20)
                                                     )
        self.reading_text.insert("0.0", self.source_text)
        self.reading_text.configure(state='disabled')
        self.reading_text.place(relx=0.5, rely=0.2, anchor="center")

    def add_highlighter(self, starting_index, end_index):
        self.reading_text.tag_add('start', starting_index, end_index)
        self.reading_text.tag_config("start", background="cyan", foreground="white")

    def check_text(self, source, input):
        if source == input:
            print('okay')

    def return_text(self):
        input_text = list(self.textbox.get().split())
        return input_text

    def correct_words(self):
        text = self.return_text()
        print(text)
        correct_words = 0
        for index, word in enumerate(text):
            print(index, word)
            if word == source_text.split()[index]:
                correct_words +=1
        print(correct_words)

