import tkinter as tk
from login_page import LoginPage

def main():
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
