import tkinter as tk
from tkinter import ttk
from exam_page import ExamPage
from utils import center_window
from notice import load_notice  # Import the load_notice function

class CandidateConfirmationPage:
    def __init__(self, ticket_id, name):
        self.ticket_id = ticket_id
        self.name = name

        self.root = tk.Tk()
        self.root.title("考生信息确认")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.root)

        basic_info_tab = ttk.Frame(tab_control)
        notice_tab = ttk.Frame(tab_control)

        tab_control.add(basic_info_tab, text="基本信息")
        tab_control.add(notice_tab, text="考生须知")

        tab_control.pack(expand=1, fill="both")

        # Basic Information Tab
        tk.Label(basic_info_tab, text="考生基本信息确认", font=("黑体", 14)).pack(pady=10)

        form_frame = tk.Frame(basic_info_tab)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="准考证号:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.admission_ticket_entry = tk.Entry(form_frame, width=30)
        self.admission_ticket_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="身份证号:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.id_number_entry = tk.Entry(form_frame, width=30)
        self.id_number_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="姓名:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="性别:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.gender_entry = tk.Entry(form_frame, width=30)
        self.gender_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="考场:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.room_entry = tk.Entry(form_frame, width=30)
        self.room_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="座号:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        self.seat_entry = tk.Entry(form_frame, width=30)
        self.seat_entry.grid(row=5, column=1, padx=5, pady=5)

        self.fill_basic_info()

        # Set all fields as read-only
        self.set_read_only()

        # Notice Tab
        notice_text = tk.Text(notice_tab, wrap=tk.WORD)
        notice_text.insert(tk.END, load_notice())  # Load the notice text from the notice.py file
        notice_text.config(state=tk.DISABLED)
        notice_text.pack(expand=1, fill="both", padx=10, pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        confirm_button = tk.Button(button_frame, text="确认", width=10, command=self.confirm)
        confirm_button.pack(side=tk.LEFT, padx=10)

        cancel_button = tk.Button(button_frame, text="取消", width=10, command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=10)

    def fill_basic_info(self):
        if self.ticket_id.startswith("2"):
            self.admission_ticket_entry.insert(0, self.ticket_id)
            self.id_number_entry.insert(0, "371000000000000000")
        elif self.ticket_id.startswith("371"):
            self.admission_ticket_entry.insert(0, "23700123456789")
            self.id_number_entry.insert(0, self.ticket_id)

        self.name_entry.insert(0, self.name)
        self.gender_entry.insert(0, "男/女")
        self.room_entry.insert(0, "1")
        self.seat_entry.insert(0, "01")

    def set_read_only(self):
        self.admission_ticket_entry.config(state="readonly")
        self.id_number_entry.config(state="readonly")
        self.name_entry.config(state="readonly")
        self.gender_entry.config(state="readonly")
        self.room_entry.config(state="readonly")
        self.seat_entry.config(state="readonly")

    def confirm(self):
        self.root.destroy()  # Close current window
        ExamPage()

    def cancel(self):
        self.root.destroy()  # Close current window
        from login_page import LoginPage
        root = tk.Tk()
        LoginPage(root)
