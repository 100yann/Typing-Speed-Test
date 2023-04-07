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
        


    def highlight_word(self):
        word = text_list[self.word_to_highlight]
        self.reading_text.tag_remove('activeLine', "1.0", 'end')
        countVar = tkinter.StringVar()
        pos = self.reading_text.search(f"\\m{word}\\M", '1.0', stopindex='end', regexp=True, count=countVar)
        print(f'position={pos}')
        self.reading_text.tag_add(word, pos, "%s + %sc"%(pos, countVar.get()))
        self.reading_text.tag_configure(word, background='yellow')
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

