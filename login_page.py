import tkinter as tk
from tkinter import messagebox
from candidate_confirmation import CandidateConfirmationPage

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("登录")
        self.root.geometry("450x200")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)

        self.create_widgets()

    def create_widgets(self):
        # Blue header
        header_frame = tk.Frame(self.root, bg='blue', height=100)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(header_frame, text="山东省春季高考数字媒体类技能考试", bg='blue', fg='white', font=("黑体", 18))
        header_label.pack(pady=10)

        # Admission Ticket Number/ID Number
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        self.ticket_id_label = tk.Label(form_frame, text="准考证/身份证号:")
        self.ticket_id_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.ticket_id_entry = tk.Entry(form_frame, width=30)
        self.ticket_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Name
        self.name_label = tk.Label(form_frame, text="姓名:")
        self.name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        login_button = tk.Button(button_frame, text="登录", width=10, command=self.login)
        login_button.pack(side=tk.LEFT, padx=10)

        cancel_button = tk.Button(button_frame, text="取消", width=10, command=self.clear_form)
        cancel_button.pack(side=tk.LEFT, padx=10)

    def login(self):
        ticket_id = self.ticket_id_entry.get()
        name = self.name_entry.get()

        if ticket_id and name:
            self.root.destroy()  # Close current window
            CandidateConfirmationPage(ticket_id, name)
        else:
            messagebox.showwarning("输入错误", "请填写所有的信息！")

    def clear_form(self):
        self.ticket_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
