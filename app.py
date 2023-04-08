import _tkinter
import tkinter
import customtkinter
import time
from source_text import all_texts

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("green")

source_text = all_texts[1]
text_list = source_text.split()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.source_text = source_text
        self.geometry('800x800')
        self.title('Typing Speed Test')
        self.config(padx=50, pady=100)
        self.textbox = customtkinter.CTkEntry(master=self,
                                              height=200,
                                              width=400,
                                              )
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")

        self.reading_text = tkinter.Text(master=self,
        height=5,
        wrap='word')
        self.reading_text.insert("0.0", self.source_text)
        self.reading_text.configure(state='disabled')
        self.reading_text.place(relx=0.5, rely=0.2, anchor="center")

        self.word_to_highlight = 0 
        self.highlight_word()
        self.textbox.bind('<space>', lambda event: (self.return_text(), self.highlight_word()))
        self.textbox.bind('<Return>', lambda event: self.correct_words())
        

    def get_word_indicies(self, text, word):
        indices = []
        words = text.split()
        start_index = 0
        for char in range(len(words)):
            if words[char].strip(",.") == word:
                indices.append((start_index, start_index+len(words[char])))
            start_index += len(words[char]) + 1
        return indices

    def highlight_word(self):
        pos = self.get_word_indicies(source_text, text_list[self.word_to_highlight])
        if len(pos) > 1: 
            self.reading_text.tag_add('addHighlight', f"0.{pos[0][0]}", f"0.{pos[0][1]}")
        self.reading_text.tag_configure('addHighlight', background='yellow')
        self.word_to_highlight +=1
 


    def return_text(self):
        input_text = list(self.textbox.get().split())
        return input_text

    def correct_words(self):
        text = self.return_text()
        print(text)
        correct_words = 0
        for index, word in enumerate(text):
            if word == source_text.split()[index]:
                correct_words +=1
        print(correct_words)

