import tkinter as tk
from tkinter import messagebox, ttk
import time
from notice import load_notice

class ExamPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("考试管理")
        self.root.geometry("340x150")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)

        self.create_widgets()
        self.start_timer()

        self.root.mainloop()

    def create_widgets(self):
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Hand in Paper Button (initially disabled)
        self.hand_in_button = tk.Button(button_frame, text="交卷", width=15, state=tk.DISABLED, command=self.hand_in_paper)
        self.hand_in_button.pack(side=tk.LEFT, padx=10)

        # Notice Button
        self.notice_button = tk.Button(button_frame, text="须知", width=15, command=self.show_notice)
        self.notice_button.pack(side=tk.LEFT, padx=10)

        # Timer label with increased font size and 黑体字体
        self.timer_label = tk.Label(self.root, text="开考倒计时: 00:00:00", font=("SimHei", 20))
        self.timer_label.pack(pady=20)

        # Timer phase (1 for 开考倒计时, 2 for 考试倒计时)
        self.timer_phase = 1

    def show_notice(self):
        # Pop-up window to show the notice content
        notice_window = tk.Toplevel(self.root)
        notice_window.title("考生须知")
        notice_window.geometry("400x300")
        notice_window.resizable(True, True)
        self.center_window(notice_window)  # Center the window

        # Scrollable text area
        text_area = tk.Text(notice_window, wrap=tk.WORD)
        text_area.insert(tk.END, load_notice())
        text_area.config(state=tk.DISABLED)  # Make it read-only
        text_area.pack(expand=1, fill="both", padx=10, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(text_area)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_area.yview)

    def start_timer(self):
        self.start_countdown(90, "开考倒计时: {:02}:{:02}:{:02}")  # Format: Hours:Minutes:Seconds

    def start_countdown(self, countdown_time, format_str):
        if countdown_time >= 0:
            hours, remainder = divmod(countdown_time, 3600)
            mins, secs = divmod(remainder, 60)
            time_format = format_str.format(hours, mins, secs)
            self.timer_label.config(text=time_format)

            # Control button state based on the current phase
            if self.timer_phase == 1:  # 开考倒计时
                self.hand_in_button.config(state=tk.DISABLED)
            elif self.timer_phase == 2:  # 考试倒计时
                if countdown_time <= 600:  # 10 minutes = 600 seconds
                    self.hand_in_button.config(state=tk.NORMAL)
                else:
                    self.hand_in_button.config(state=tk.DISABLED)

            if countdown_time > 0:
                self.root.after(1000, self.start_countdown, countdown_time - 1, format_str)
            else:
                if self.timer_phase == 1:  # Switch to test countdown
                    self.timer_phase = 2
                    self.start_countdown(3000, "考试倒计时: {:02}:{:02}:{:02}")  # 50 minutes
                else:
                    # Once the countdown finishes, handle the end of the exam
                    self.end_of_exam()

    def hand_in_paper(self):
        # Confirmation popup before handing in the paper
        result = messagebox.askyesno("提示信息", "是否确认交卷")
        if result:
            self.show_loading_screen()

    def show_loading_screen(self):
        # Loading screen simulation
        loading_window = tk.Toplevel(self.root)
        loading_window.title("正在交卷")
        loading_window.geometry("300x100")
        loading_window.resizable(False, False)
        self.center_window(loading_window)  # Center the window

        progress_label = tk.Label(loading_window, text="Loading...")
        progress_label.pack(pady=10)

        progress_bar = ttk.Progressbar(loading_window, length=200, mode='determinate')
        progress_bar.pack(pady=10)
        
        loading_percentage = tk.Label(loading_window, text="0%")
        loading_percentage.pack()

        # Simulate loading progress
        self.update_progress(progress_bar, loading_percentage, 0, loading_window)

    def update_progress(self, progress_bar, loading_percentage, value, window):
        if value <= 100:
            progress_bar['value'] = value
            loading_percentage.config(text=f"{value}%")
            self.root.after(30, self.update_progress, progress_bar, loading_percentage, value + 1, window)
        else:
            window.destroy()
            messagebox.showinfo("信息", "考试提交成功！")
            self.root.quit()

    def end_of_exam(self):
        # End of exam handling on the main thread
        messagebox.showinfo("时间到", "考试时间到，您的答卷将会被自动提交，请点击确定按钮！")
        self.show_loading_screen()

    def center_window(self, window):
        # Method to center a given window
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    ExamPage()
