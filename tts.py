import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

root = tk.Tk()
root.title('TTS')
root.configure(background="pink")
root.resizable(0,0)
label = tk.Label(root, text="Type Something", bg="pink", font="Arial 30 bold")
label.pack()
textbox = tk.Entry(root, width=35, font="Arial 25")
textbox.pack()

def speak(text):
    engine.say(text)
    engine.runAndWait()

button = tk.Button(root, text= "SPEAK", bg="blue", font="Arial 25 bold", command=lambda:speak(textbox.get()))
button.pack()
root.mainloop()
