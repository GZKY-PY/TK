# coding:utf-8
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

try:
    from mysqlDB import Mysql
except:
    pass
    
# 初始化
window = tk.Tk()
window.title('Data Query ！')

window.geometry('1500x800')

l = tk.Label(window, text='请输入关键字查询', font=('Yahei', 11), width=40, height=2)
l.pack()

input_button = tk.Entry(window, show=None, font=('Yahei', 12), width=32)  # 明文形式
input_button.pack()

tk.Label(window, font=('Yahei', 8), width=20, height=1).pack()  # 过渡

m_listbox_var = tk.StringVar()


# 数据展示列表
def listbox(temp_list):
    m_listbox_var.set('')
    yscrolly = tk.Scrollbar(window)
    yscrolly.pack(side=tk.RIGHT, fill=Y)

    m_list = tk.Listbox(window, font=('Arial', 11), listvariable=m_listbox_var, selectmode=tk.BROWSE, width=300,
                        height=150, yscrollcommand=yscrolly.set)
    for item in temp_list:
        m_list.insert(tk.END, item)
    m_list.pack(fill=tk.BOTH)
    yscrolly.config(command=m_list.yview)


def get_sql():
    M = Mysql("test")
    data_list = M.query_data("law_content")

    value = input_button.get().strip()
    if value == '':
        tkinter.messagebox.showwarning(title='warning', message='请输入关键字')
    else:
        lst = []
        for data in data_list:
            fenci_words_list = [i for i in data[3].split(' ') if i != '']
            if value in fenci_words_list:
                lst.append(data[1] + ' ' + data[2])
            else:
                # tkinter.messagebox.showwarning(title='Sorry', message='抱歉,查询无果')
                listbox(['抱歉,查询无果'])
        if len(lst) > 0:
            listbox(lst)


B = tk.Button(window, text="查询", font=('Yahei', 10), width=10, height=1, command=get_sql)
B.pack()

tk.Label(window, font=('Yahei', 8), width=20, height=1).pack()  # 过渡

# 启动
window.mainloop()
