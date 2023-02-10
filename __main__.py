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
        self.error_label.grid(padx=5, pady= 5)
    

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
        error_instance.blip_error("Clone completed")
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
    root.title("Easy-Clone")

    info = _info()
    error = _error(root)
    

    url = StringVar()

    url_frame = tk.Frame(root, bg= "light grey")
    url_frame.grid(row=1, padx = 20, pady=10)
    url_directions = tk.Label(url_frame, text= "Enter a valid public repository").grid(row= 1,  padx = 5, pady= 5)
    url_box = tk.Entry(url_frame, textvariable = url, width= 50).grid(row=2, padx=5, pady= 5)


    dir_frame = tk.Frame(root, bg= "light grey")
    dir_frame.grid(row=2, padx = 20, pady=10)
    dir_button = tk.Button(dir_frame, text="Click to select a directory", command= info.set_path).grid( padx=5, pady = 5)

    commit_frame = tk.Frame(root, bg= "light grey")
    commit_frame.grid(row=3, padx = 20, pady=10)
    commit = tk.Button(commit_frame, text= "Clone repository", command= lambda : [info.set_url(url), clone_repo(info, error)]).grid(padx = 5, pady= 5)

    root.mainloop()