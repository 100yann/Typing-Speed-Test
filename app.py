import _tkinter
import tkinter
import customtkinter
import time
from source_text import all_texts

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("green")

source_text = all_texts[1]
text_list = source_text.split()
REMAINING_TIME = 60


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.source_text = source_text
        self.geometry('800x800')
        self.title('Typing Speed Test')
        self.config(padx=50, pady=100)

        
        self.textbox = customtkinter.CTkEntry(master=self,
                                              height=300,
                                              width=400,
                                              )
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")
        self.textbox.focus()

        self.reading_text = tkinter.Text(master=self,
        height=5,
        wrap='word')
        self.reading_text.insert("0.0", self.source_text)
        self.reading_text.configure(state='disabled')
        self.reading_text.place(relx=0.5, rely=0.2, anchor="center")
        self.start_index = 0
        self.word_to_highlight = 0
        self.remove_index = 0
        self.highlight_word()
        self.textbox.bind('<space>', lambda event: (self.return_text(), self.highlight_word()))
        self.textbox.bind('<Return>', lambda event: self.correct_words())
        self.timer()



    def get_word_indicies(self, word, func):
        if func == "add":
            indices = (self.start_index, self.start_index+len(word))
            self.start_index += len(word) + 1
            return indices
        elif func == "remove":
            if self.word_to_highlight > 0:
                indices = (self.remove_index, self.remove_index+len(word))
                self.remove_index += len(word) + 1
                return indices
                



    def highlight_word(self):
        if self.word_to_highlight > 0:
            previous_word = text_list[self.word_to_highlight - 1]
            try:
                previous_word_pos = self.get_word_indicies(previous_word, "remove")
                self.reading_text.tag_remove('highlightline', f"1.{previous_word_pos[0]}", f"1.{previous_word_pos[1]}")
            except _tkinter.TclError:
                pass

        word = text_list[self.word_to_highlight]
        word_pos = self.get_word_indicies(word, "add")
        starting_pos = word_pos[0]
        ending_pos = word_pos[1]
        self.reading_text.tag_add('highlightline', f"1.{starting_pos}", f"1.{ending_pos}")
        self.reading_text.tag_configure('highlightline', background='yellow')
        self.word_to_highlight +=1  


    def return_text(self):
        input_text = list(self.textbox.get().split())
        return input_text

    def correct_words(self):
        text = self.return_text()
        correct_words = 0
        for index, word in enumerate(text):
            if word == text_list[index]:
                correct_words +=1
        return correct_words


    def timer(self):
        global REMAINING_TIME
        REMAINING_TIME -= 1
        print(REMAINING_TIME)
        if REMAINING_TIME > 50:
            self.after(1000, self.timer)
            self.entry = customtkinter.CTkEntry(master=self,
                                    placeholder_text=REMAINING_TIME,
                                    bg_color='transparent',
                                    width=30,
                                    )
            self.entry.place(relx=0.0, rely=0.0, anchor="nw")
        else:
            wpm = self.correct_words()
            print(f'You can write {wpm} words per minute.')
            self.textbox.configure(state='disabled')
