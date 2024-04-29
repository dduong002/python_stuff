import tkinter as tk
import time

def start_button_clicked():

    text_box.delete(1.0, tk.END)
    # Display first custom text for 5 seconds
    custom_text1 = '''Greetings, I hope your day is going well. Your in for a treat.
Am about to tell you a story.. 😊'''
    text_box.insert(tk.END, custom_text1)
    root.update_idletasks()
    time.sleep(4)
    text_box.delete(1.0, tk.END)

    # Display first custom text for 5 seconds
    custom_text2 = '''Once a upon a time, there was a young bear name Teddy. 
Let call him PVT Teddy Bear ;)\n'''
    text_box.insert(tk.END, custom_text2)
    root.update_idletasks()
    time.sleep(2)

    custom_text3 = '''PVT Teddy Bear was attending school more his work. He wasn't a shitbag soldier compare to his other soldier.'''
    text_box.insert(tk.END, custom_text3)
    root.update_idletasks()
    time.sleep(2)

root = tk.Tk()
root.title("Start Button Application")
root.geometry("500x250") # set window size

text_box = tk.Text(root, width=50, height=12, )
text_box.pack()
text_box.config(font=("Time New Roman", 12)) # set font size to 16

# Display "Click the start button to begin 😊" when the application is run
text_box.insert(tk.END, "     Click the start button to begin 😊   ")
root.update_idletasks()

start_button = tk.Button(root, text="Start", command=start_button_clicked)
start_button.pack()


root.mainloop()