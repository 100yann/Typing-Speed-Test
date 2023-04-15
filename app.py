import _tkinter
import tkinter
import customtkinter
import time
import re
from source_text import all_texts

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme("green")

source_text = all_texts[1]
text_list = source_text.split()
REMAINING_TIME = 60
words_and_indices = {}


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.source_text = source_text
        self.geometry('1080x1080')
        self.title('Typing Speed Test')
        self.state('zoomed')
        self.config(padx=50, pady=100)
        self.reading_text = tkinter.Text(master=self, 
                                         height=10,
                                         width=80,
                                         wrap='word',
                                         font=('Ardoise Std', 16)
                                         )
        self.reading_text.insert("0.0", self.source_text)
        self.reading_text.configure(state='disabled', padx=10, pady=10)
        self.reading_text.place(relx=0.5, rely=0.2, anchor="center")
        self.start_index = 0
        self.word_to_highlight = 0
        self.written_word = 0
        self.correct_words = 0

        self.textbox = customtkinter.CTkTextbox(master=self,
                                height=100,
                                width=250,
                                wrap='word',
                                )
        self.textbox.place(relx=0.5, rely=0.5, anchor="center")
        self.textbox.focus_set()
        self.textbox.bind('<space>', lambda event: self.return_text())
        self.textbox.bind('<Return>', lambda event: self.correct_words())
        self.highlight_word(text_list[0])

        self.timer()




    def get_word_indicies(self, word):
        word_indices = (self.start_index, self.start_index+len(word))
        return word_indices
        

    def highlight_word(self, input_word):
        if self.written_word > 0:
            self.reading_text.tag_delete('highlight', 
                                         f'1.{words_and_indices[self.written_word-1][1]}', 
                                         f'1.{words_and_indices[self.written_word-1][2]}')

        word = text_list[self.written_word]   
        word_pos = self.get_word_indicies(word)
        starting_pos, ending_pos = word_pos[0], word_pos[1]
        self.reading_text.tag_add('highlight', f"1.{starting_pos}", f"1.{ending_pos}")
        self.reading_text.tag_configure('highlight', background='yellow')
        words_and_indices[self.written_word] = [word, starting_pos, ending_pos]

        # if self.written_word > 0 and input_word != text_list[self.written_word]:
        #     starting_pos, ending_pos = words_and_indices[self.written_word][1], words_and_indices[self.written_word][2]
        #     self.reading_text.tag_add('incorrect', f"1.{starting_pos}", f"1.{ending_pos}")
        #     self.reading_text.tag_configure('incorrect', underline=True, underlinefg='red')
        if self.written_word > 0 and input_word == text_list[self.written_word-1]:
            print(input_word, text_list[self.written_word-1])
            self.correct_words += 1

        self.start_index += len(word) + 1
        self.written_word += 1



    def return_text(self):
        get_input = (self.textbox.get('1.0', 'end')).strip()
        for char in get_input:
            if char.isalpha():
                self.textbox.delete('1.0', "end")
                self.highlight_word(get_input)
                break
        




    def timer(self):
        global REMAINING_TIME
        REMAINING_TIME -= 1
        if REMAINING_TIME > 0:
            self.after(1000, self.timer)
            self.entry = customtkinter.CTkEntry(master=self,
                                    placeholder_text=REMAINING_TIME,
                                    bg_color='transparent',
                                    width=30,
                                    )
            self.entry.place(relx=0.0, rely=0.0, anchor="nw")
        else:
            wpm = self.correct_words
            print(f'You can write {wpm} words per minute.')
            self.textbox.configure(state='disabled')
