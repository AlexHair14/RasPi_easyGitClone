from git import Repo, GitError
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

class _error():
    def __init__(self, root):
        self.error_on_screen = False
        self.error_label = tk.Label(root, fg= 'red')
        
    def blip_error(self,Error):
        if self.error_label.winfo_ismapped():
            self.error_label.configure(text="")

        self.error_label.configure(text= Error)
        self.error_label.pack()
    

def clone_repo(info_instance, error_instance):
    url = info_instance.get_url()
    dir = info_instance.get_path()

    if dir == "":
        info_instance.set_path()
        dir = info_instance.get_path()


    dir_in_path = os.listdir(dir)
    folder_created = False
    folder_name = "Repo"
    attempt = 1
    # If the specified directory is not empty it creates a new directory named Repo in specified directory 
    # If Repo is already in directory it will retry with Repo(1) Repo(2) ... Repo(10) until it finds a unique name 

    # if path is empty this is needed because a repository needs an empty directory 
    if len(dir_in_path) == 0:
        path = dir
    # if there's stuff in the PATH
    else:
        # While we haven't made a folder
        while folder_created == False:
            #
            if folder_name in dir_in_path:
                folder_name = "Repo(" + str(attempt) + ")"
                attempt += 1 
            else:
                new_path = os.path.join(dir,folder_name)
                os.mkdir(new_path)
                path = new_path
                folder_created = True

    try:
        print("attempted to clone: " + str(url) + " to this directory" + str(path)  )
        Repo.clone_from(url=url, to_path=path)
    except GitError:
        error_instance.blip_error("Repository not valid")
        if folder_created:
            os.rmdir(path)

class _info:
    def __init__(self):
        self.path = ""
        self.url = ""

    def set_path(self):
        self.path = filedialog.askdirectory(title="Select a directory")
    
    def set_url(self,url_var):
        self.url = url_var.get()

    def get_path(self):
        return self.path
    
    def get_url(self):
        return self.url
    



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x400')
    root.title("Easy-Clone")

    info = _info()
    error = _error(root)
    

    url = StringVar()

    url_directions = tk.Label(root, text= "Enter a valid public repository ").pack(pady= 10)

    url_box = tk.Entry(root, textvariable = url, width= 25).pack()


    dir_button = tk.Button(root, text="Click to select a directory", command= info.set_path).pack(pady= 20)

    commit = tk.Button(root, text= "Clone repository", command= lambda : [info.set_url(url), clone_repo(info, error)]).pack(pady= 10)

    root.mainloop()