from git import Repo
import tkinter as tk






frame = tk.Tk()

frame.title("Easy GitClone")
frame.geometry('400x200')

class clone:
    def __init__(self):
        self.url = ""
        self.dir = ""
    def get_url(self):
        self.url = input_url.get(1.0, "end-1c")
    def get_dir(self):
        self.dir = input_dir.get(1.0, "end-1c")
    def clone_repo(self):
        repo = Repo.clone_from(url = self.url, to_path = self.dir)
        repo.close()
    

    

# TextBox Creation
input_url = tk.Text(frame, height = 5, width = 20)
input_url.pack()
input_dir = tk.Text(frame, height = 5, width = 20)
input_dir.pack()

work = clone()

# Enter button
confirm = tk.Button(frame, text = "enter", command = lambda: [work.get_url(), work.clone_repo()])
confirm.pack()



frame.mainloop()