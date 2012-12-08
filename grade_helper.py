# -*- coding: utf-8 -*-
import string
import re
from Tkinter import *
import tkFileDialog

REGEX = re.compile('(\d+|\d+\.\d+)\/(\d+|\d+\.\d+)')
MODES = [('None', 0), ('+10 EC', 1), ('+20 EC', 2), ('+25 EC', 3)]

class App:
        def __init__(self, master):
                self.frame = Frame(master)
                self.frame.pack(side=BOTTOM)
                self.vault = self.calculate() 
                self.option = IntVar()
                self.option.set(0)
                self.list_labels(self.vault, self.option)
                for text, mode in MODES:
                        self.radio_button = Radiobutton(master=self.frame, text = text, variable=self.option, value=mode, width=40, command = self.apply_handler, indicatoron=0, relief="flat")
                        self.radio_button.grid(columnspan=2)                        
                self.button2 = Button(self.frame, text = "QUIT", width = 40, fg = "red", command=self.frame.quit)
                self.button2.grid(row = 8, columnspan=2)
        def apply_handler(self):
                self.list_labels(self.vault, self.option)
        
        def list_labels(self, vaulty, option):
                vault = list(vaulty)
                if option.get() == 1:
                        vault[0] -= 10
                elif option.get() == 2:
                        vault[0] -= 20
                elif option.get() == 3:
                        vault[0] -= 25
                self.label = Label(self.frame, text = "현재 잃은 점수: ")
                self.label.grid(row=0, sticky = W)
                self.label_= Label(self.frame, text = ' '+str(vault[0]), width = 10, anchor = "e")
                self.label_.grid(row=0, column=1, sticky = E)
                self.label1 = Label(self.frame, text = "현재 점수/현재 가능점수: ") 
                self.label1.grid(row=1, sticky = W)
                self.label1_= Label(self.frame, text = str(vault[1]-vault[0])+'/'+str(vault[1]), width = 20, anchor = "e")
                self.label1_.grid(row=1, column=1, sticky = E)
                self.label2 = Label(self.frame, text = "현재 성적: ")
                self.label2.grid(row=2, sticky = W)
                self.label2_ = Label(self.frame, text = str(100*(1-vault[0]/vault[1]))+'%', width = 20, anchor = "e")
                self.label2_.grid(row=2, column=1, sticky = E)
                self.letter_grade = Label(self.frame, text = '당신의 성적은 '+self.get_grade(100*(1-vault[0]/vault[1])) + ' 입니다.', width = 40)
                self.letter_grade.grid(row=3, columnspan=2)

        def calculate(self):
                file = tkFileDialog.askopenfile(mode='r', filetypes=[('text files', '.txt')])
                TOTAL_MAX = 0
                TOTAL_LOSS = 0
                CURRENT = 0
                for line in file:
                        TEST = REGEX.search(line)
                        if TEST != None:                               
                                front = float(TEST.groups()[0])
                                CURRENT += front
                                back = float(TEST.groups()[1])
                                LOSS = back - front
                                if (LOSS) > 0:
                                        TOTAL_LOSS += LOSS
                                TOTAL_MAX += back
                return [TOTAL_LOSS, TOTAL_MAX]
        def get_grade(self, value):
                GRADE = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F']
                #{97:'A+', 93:'A', 90:'A-', 87:'B+', 83:'B', 80:'B-', 77:'C+', 73:'C', 70:'C-', 67:'D+', 63:'D', 60:'D-', 0:'F'}
                if value >= 97:
                        return GRADE[0]
                elif value < 97 and value >= 93:
                        return GRADE[1]
                elif value < 93 and value >= 90:
                        return GRADE[2]
                elif value < 90 and value >= 87:
                        return GRADE[3]
                elif value < 87 and value >= 83:
                        return GRADE[4]
                elif value < 83 and value >= 80:
                        return GRADE[5]
                elif value < 80 and value >= 77:
                        return GRADE[6]
                elif value < 77 and value >= 73:
                        return GRADE[7]
                elif value < 73 and value >= 70:
                        return GRADE[8]
                elif value < 70 and value >= 60:
                        return GRADE[9]
                else:
                        return GRADE[10]

if __name__ == "__main__":
        root= Tk()
        root.wm_title("Chinese GRADE HELPER")
        app = App(root)
        root.mainloop()
                
