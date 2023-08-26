from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from src.downloader import YouTubeDownloader, get_vid_link

class YouTubeDownloaderGUI:
    def __init__(self, master, downloader):
        self.master = master
        self.downloader = downloader
        self.master.title('YouTube Downloader')
        self.master.geometry('400x250')
        
        self.url_label = Label(master, text="YouTube URL or Keyword:")
        self.url_label.pack()
        
        self.url_entry = Entry(master, width=50)
        self.url_entry.pack()
        
        self.res_label = Label(master, text="Resolution:")
        self.res_label.pack()
        
        self.res_combobox = ttk.Combobox(master, values=("Highest", "720p", "480p", "360p", "240p", "144p"))
        self.res_combobox.current(0)
        self.res_combobox.pack()
        
        self.path_label = Label(master, text="Save to:")
        self.path_label.pack()
        
        self.path_entry = Entry(master, width=40)
        self.path_entry.insert(0, self.downloader.output_path)
        self.path_entry.pack(side=LEFT)
        
        self.path_button = Button(master, text="Browse", command=self.browse)
        self.path_button.pack(side=RIGHT)
        
        self.download_button = Button(master, text="Download", command=self.download)
        self.download_button.pack()
        
    def browse(self):
        folder_selected = filedialog.askdirectory()
        self.path_entry.delete(0, END)
        self.path_entry.insert(0, folder_selected)
        
    def download(self):
        url_or_keyword = self.url_entry.get()
        res = self.res_combobox.get()
        save_path = self.path_entry.get()
        self.downloader.output_path = save_path  # Update the output path
        if "https:" in url_or_keyword and "youtu" in url_or_keyword:
            if res == "Highest":
                self.downloader.get_highest_res_video(url_or_keyword)
            else:
                self.downloader.get_video(url_or_keyword, res)
        else:
            url = get_vid_link(url_or_keyword)
            print(f"Downloading from {url}...")
            if res == "Highest":
                self.downloader.get_highest_res_video(url)
            else:
                self.downloader.get_video(url, res)

# In the main block, update the code like this
if __name__ == "__main__":
    root = Tk()
    yt_downloader = YouTubeDownloader("downloads")  # This can be updated later
    app = YouTubeDownloaderGUI(root, yt_downloader)
    root.mainloop()
