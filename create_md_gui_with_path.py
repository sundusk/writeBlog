import os
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, filedialog
from datetime import datetime

# 创建文件的函数
def create_file():
    # 获取用户输入的文件名和保存路径
    filename = file_name_var.get() + '.md'
    save_path = save_path_var.get()

    if not save_path:
        messagebox.showerror("错误", "请指定文件保存路径")
        return

    title = file_name_var.get()  # 使用文件名作为标题

    # 获取当前日期
    today = datetime.today().strftime('%Y-%m-%d')

    # 如果没有这个文件夹，则创建
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 完整路径
    filepath = os.path.join(save_path, filename)

    # 创建文件并写入内容
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write(f'title: "{title}"\n')
            f.write(f'date: "{today}"\n')
            f.write('---\n\n')
            f.write('这是一个新的文章\n')
        messagebox.showinfo("成功", f'文件 {filename} 已创建在 {save_path} 文件夹中')
    except Exception as e:
        messagebox.showerror("错误", f"文件创建失败: {str(e)}")

# 浏览文件夹的函数
def browse_folder():
    folder_selected = filedialog.askdirectory()
    save_path_var.set(folder_selected)

# 关闭窗口的函数
def cancel():
    root.quit()

# 创建主窗口
root = Tk()
root.title("创建文章")

# 设置窗口大小
root.geometry("400x250")

# 创建输入框的变量
file_name_var = StringVar()
save_path_var = StringVar()

# 标签和输入框
Label(root, text="文件名（即文章名）:").pack(pady=10)
Entry(root, textvariable=file_name_var).pack()

Label(root, text="保存路径:").pack(pady=10)
Entry(root, textvariable=save_path_var).pack()

# 浏览按钮
Button(root, text="浏览", command=browse_folder).pack(pady=5)

# 创建按钮
Button(root, text="确定", command=create_file).pack(pady=10, side='left', padx=50)
Button(root, text="取消", command=cancel).pack(pady=10, side='right', padx=50)

# 运行主循环
root.mainloop()