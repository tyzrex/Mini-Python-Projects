import tkinter
import customtkinter
from pytube import YouTube

def download_video():
    youtube_url = link.get()
    if youtube_url == "":
        complete_label.configure(text="Please enter a URL",text_color="red")
        complete_label.place(anchor="center", relx=0.5, rely=0.48)
        return
    try:
        yt = YouTube(youtube_url, on_progress_callback=progress_bar)
        video_title.configure(text=yt.title)
        get_video = yt.streams.get_highest_resolution()
        get_video.download()
        
    except:
        complete_label.configure(text="Error while downloading video. Please try again.",text_color="red")
    complete_label.configure(text="Download Complete")
    complete_label.place(anchor="center", relx=0.5, rely=0.48)


def progress_bar(stream, chunk, bytes_remaining):
    video_size = stream.filesize
    downloaded = video_size - bytes_remaining
    percentage_downloaded = int(downloaded/video_size * 100)
    percentage_label.update()
    percentage_label.configure(text=f"{percentage_downloaded}%")
    download_slider.set(percentage_downloaded/100)
    download_slider.update()
        

customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("System")

app = customtkinter.CTk()
app.geometry("720x500")
app.title("Youtube Downloader")

#app title
title = customtkinter.CTkLabel(app, text="Youtube Video Downloader", font=("Helvetica", 40))
title.place(anchor="center", relx=0.5, rely=0.1)

# label for the textbox
textbox_title = customtkinter.CTkLabel(app, text="Enter the URL of the video you want to download:", font=("Helvetica", 20))
textbox_title.place(anchor="center", relx=0.5, rely=0.2)

# textbox for irl
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=600, height=50, font=("Helvetica", 20),placeholder_text="Enter URL here",textvariable=url_var)
link.place(anchor="center", relx=0.5, rely=0.25)

# Download Button
button = customtkinter.CTkButton(app, text="Download", font=("Helvetica", 20), width=120, height=50,command=download_video)
button.place(anchor="center", relx=0.5, rely=0.35)

#complete label
complete_label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 20))
complete_label.place(anchor="center", relx=0.5, rely=0.5)

#youtube video title
video_title = customtkinter.CTkLabel(app, text="", font=("Helvetica", 20))
video_title.place(anchor="center", relx=0.5, rely=0.43)

# slider for download percentage
download_slider = customtkinter.CTkProgressBar(app, width=600)
download_slider.place(anchor="center", relx=0.5, rely=0.5)
download_slider.set(0)

# label for percentage
percentage_label = customtkinter.CTkLabel(app, text="0%", font=("Helvetica", 20))
percentage_label.place(anchor="center", relx=0.5, rely=0.55)

if __name__ == "__main__":
    app.mainloop()