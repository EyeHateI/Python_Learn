import yaml
import os
import tkinter as tk
import tkinter.messagebox
curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath1 = os.path.join(curpath,'C_T.yaml')
yamlpath2 = os.path.join(curpath,'F_T.yaml')
f1 = open(yamlpath1,'r+',encoding='utf-8')
f.close()
f2 = open(yamlpath2,'r+',encoding='utf-8')
f2.close

window = tk.Tk()
window.title('答题v4.0')
window.geometry('500x300')

Tittle = tk.Label(window,text='选择题')