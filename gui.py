# coding: utf-8
"""gui test file"""

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from languagedetector import LanguageDetector

ld = LanguageDetector()
ld.addDict('fr', 'dict/dico_fr.txt')
ld.addDict('en', 'dict/dico_en.txt')
ld.addDict('de', 'dict/dico_de.txt')
ld.addDict('es', 'dict/dico_es.txt')
ld.addDict('it', 'dict/dico_it.txt')
ld.addDict('ru', 'dict/dico_ru.txt')

def run_detection(event):
    text_to_detect = text_area.get('1.0', END)
    detection = ld.detect(text_to_detect)
    label_detection.config(text=detection)
    flag_img = PhotoImage(file='flags/{}.gif'.format(detection))
    canv_flag.delete('all')
    canv_flag.img = flag_img
    canv_flag.create_image(2,2, anchor=NW, image=canv_flag.img)

root = Tk()
root.title('gui - ldetect')

frame_detection = Frame(root)
frame_detection.pack(side=TOP)

label = Label(frame_detection, text='Language:')
label.pack(side=LEFT)

label_detection = Label(frame_detection, text='?', fg='blue')
label_detection.pack(side=LEFT)

canv_flag = Canvas(frame_detection, width=16, height=11)
canv_flag.pack(side=LEFT)

text_area = ScrolledText(root)
text_area.bind("<KeyRelease>", run_detection)
text_area.pack(side=BOTTOM)

root.geometry('300x150')

root.mainloop()
