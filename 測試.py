import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

root = tk.Tk()
root.title("嘿嘿簡單計算器")

display = tk.Entry(root, width=20, font=('Arial', 14))
display.grid(row=0, column=0, columnspan=4)

current_expression = ""

def update_operator(new_operator):
    global current_expression
    if current_expression and current_expression[-1] in '+-*/':
        current_expression = current_expression[:-1] + new_operator
    elif current_expression and current_expression[-1].isdigit():
        current_expression += new_operator
    display.delete(0, tk.END)
    display.insert(tk.END, current_expression)

def button_click(value):
    global current_expression
    current_expression += value
    display.delete(0, tk.END)
    display.insert(tk.END, current_expression)

def equal_click():
    global current_expression
    try:
        result = eval(current_expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        current_expression = str(result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear_all():
    global current_expression
    current_expression = ""
    display.delete(0, tk.END)

def open_website(url):
    webbrowser.open_new(url)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('😒', 0, 3),
    ('Youtube', 1, 4), ('Google', 2, 4), ('酷課雲', 3, 4), ('Gmail', 4, 4),
    ('NewButton', 0, 4)  # 新增的按鍵
]

# 定義連結對應的網址
links = {
    'Youtube': 'https://www.youtube.com/',
    'Google': 'https://www.google.com',
    '酷課雲': 'https://cooc.tp.edu.tw/main',
    'Gmail': 'https://mail.google.com'
}

for (text, row, col) in buttons:
    if text in '+-*/':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda value=text: update_operator(value))
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=equal_click)
    elif text == '😒':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear_all)
    elif text in ['Youtube', 'Google', '酷課雲', 'Gmail']:
        button = tk.Button(root, text=text, width=10, height=2, font=('Arial', 14), command=lambda url=links[text]: open_website(url))
    elif text == 'NewButton':
        # 調整圖片大小
        image = Image.open('1.png')
        image = image.resize((100, 50))
        photo = ImageTk.PhotoImage(image)
        button = tk.Button(root, image=photo, width=105, height=50, command=lambda: print("New Button Clicked"))
        button.image = photo  # 保持圖片參考，避免被垃圾回收
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

root.mainloop()