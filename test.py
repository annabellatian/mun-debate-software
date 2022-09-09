# from tkinter import *
# from tkinter.ttk import *
#
# # creates a Tk() object
# master = Tk()
#
# # sets the geometry of main
# # root window
# master.geometry("200x200")
#
#
# # function to open a new window
# # on a button click
# def openNewWindow():
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
#
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window")
#
#     # sets the geometry of toplevel
#     newWindow.geometry("300x150")
#
#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text="This is a new window").pack()
#     btn1 = Button(newWindow,
#                   text="submit",
#                   command=lambda: newWindow.destroy())
#     btn1.pack(pady=10)
#
#
# label = Label(master,
#               text="This is the main window")
#
# label.pack(pady=10)
#
# # a button widget which will open a
# # new window on button click
# btn = Button(master,
#              text="Click to open a new window",
#              command=openNewWindow)
# btn.pack(pady=10)
#
# # mainloop, runs infinitely
# mainloop()
# # from tkinter import *
# #
# # root = Tk()
# # root.title('yeet')
# #
# # MODES = [
# #     ("Present", "present", 0),
# #     ("Present in Voting", "voting", 1),
# #     ("Absent", "absent", 2)]
# #
# # status = StringVar()
# # status.set("present")
# #
# # for text, stat, column in MODES:
# #     myButton = Radiobutton(root, text=text, variable=status, value=stat)
# #     myButton.grid(row=0, column=column)
# #
# #
# # def clicked(value):
# #     myLabel = Label(root, text=value)
# #     myLabel.grid(row=2, column=0)
# #
# #
# # myBut = Button(root, text="Click", command=lambda: clicked(status.get()))
# # myBut.grid(row=1, column=0)
# # mainloop()
#
# # This is a tutorial on how to use multiple checkbuttons in tkinter through an example of a basic survey!
# # First of all of course we will have to import tkinter and create a window!
# # import tkinter
# #
# # MyRoot = tkinter.Tk()
# #
#
# # # Now the type of program I will be creating is a quick survey asking some basic questions and giving your options using checkbuttons.
# # # First I will be using the entrybox, button and label widget, to make this actually look like a survey, by creating a label and a program for it.
# # def EntryBoxFunc():
# #     name = EntryBox.get()
# #     Label1.config(text="Hello %s!! Please continue and finish your survey!" % name)
# #
# #
# # Label1 = tkinter.Label(MyRoot, text="What is your name?")
# # EntryBox = tkinter.Entry(MyRoot)
# # Button1 = tkinter.Button(MyRoot, text="Enter", command=EntryBoxFunc)
# # Label1.pack(padx=30, pady=10)
# # EntryBox.pack(padx=30, pady=10)
# # Button1.pack(padx=30, pady=10)
# #
# #
# # # This will make it so whatever you type in as your name, that will now come up in your label. Here I will be
# # # creating my function for the final results! When creating these functions I'll need to know whether a CB (
# # # checkbutton) is clicked or not, I can find this out using the .get option for the variable I create. If the value
# # # of the .get is 0 then the CB is not clicked, if it is 1 then it is clicked.
# # def Results():
# #     ReviewRoot = tkinter.Tk()
# #     ReviewRoot.title = "Results"
# #     # Question 1 Review.
# #     while True:
# #         if (MaleCB.get() == 0) and (FemaleCB.get() == 0):
# #             tkinter.Label(ReviewRoot, text="Please tell me your gender.").pack(pady=30, padx=30)
# #             break
# #         elif (MaleCB.get() == 1) and (FemaleCB.get() == 1):
# #             tkinter.Label(ReviewRoot, text="Please only pick one gender!").pack(pady=30, padx=30)
# #             break
# #         elif MaleCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are a male!").pack(pady=30, padx=30)
# #             break
# #         elif FemaleCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are a male!").pack(pady=30, padx=30)
# #             break
# #     # Question 2 Review.
# #     while True:
# #         if (YoungsterCB.get() == 0) and (TeenCB.get() == 0) and (AdultCB.get() == 0):
# #             tkinter.Label(ReviewRoot, text="Please select an option as your age!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 1) and (TeenCB.get() == 1) and (AdultCB.get() == 1):
# #             tkinter.Label(ReviewRoot, text="Please select one option as your age!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 1) and (TeenCB.get() == 1) and (AdultCB.get() == 0):
# #             tkinter.Label(ReviewRoot, text="Please select one option as your age!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 1) and (TeenCB.get() == 0) and (AdultCB.get() == 1):
# #             tkinter.Label(ReviewRoot, text="Please select one option as your age!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 0) and (TeenCB.get() == 1) and (AdultCB.get() == 1):
# #             tkinter.Label(ReviewRoot, text="Please select one option as your age!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 1) and (TeenCB.get() == 0) and (AdultCB.get() == 0):
# #             tkinter.Label(ReviewRoot, text="You are between the ages of 10 and 14!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 0) and (TeenCB.get() == 1) and (AdultCB.get() == 0):
# #             tkinter.Label(ReviewRoot, text="You are between the ages of 15 and 19!").pack(pady=30, padx=30)
# #             break
# #         elif (YoungsterCB.get() == 0) and (TeenCB.get() == 0) and (AdultCB.get() == 1):
# #             tkinter.Label(ReviewRoot, text="You are either 20 years old or older!").pack(padx=30, pady=30)
# #             break
# #     # Question 3 Review.
# #     while True:
# #         if SkeetCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are a skeet!").pack(padx=30, pady=30)
# #             break
# #         else:
# #             tkinter.Label(ReviewRoot, text="You are not a skeet!").pack(padx=30, pady=30)
# #             break
# #     while True:
# #         if JockCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are a jock!").pack(padx=30, pady=30)
# #             break
# #         else:
# #             tkinter.Label(ReviewRoot, text="You are not a jock!").pack(padx=30, pady=30)
# #             break
# #     while True:
# #         if CoolCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are cool!").pack(padx=30, pady=30)
# #             break
# #         else:
# #             tkinter.Label(ReviewRoot, text="You are not cool!").pack(padx=30, pady=30)
# #             break
# #     while True:
# #         if NerdCB.get() == 1:
# #             tkinter.Label(ReviewRoot, text="You are a nerd!").pack(padx=30, pady=30)
# #             break
# #         else:
# #             tkinter.Label(ReviewRoot, text="You are not a nerd!").pack(padx=30, pady=30)
# #             break
# #
# #
# # # I will now be creating all of my labels(which will act as questions) and checkbuttons and then I will pack them!
# # # As well I will be giving each checkbutton an IntVar(), so that my final results program will know whether or not the button is checked or not.
# # # Question 1 Stuff.
# # Label2 = tkinter.Label(MyRoot, text="Are you male or female?")
# # MaleCB = tkinter.IntVar()
# # FemaleCB = tkinter.IntVar()
# # CB1 = tkinter.Checkbutton(MyRoot, text="Male", variable=MaleCB)
# # CB2 = tkinter.Checkbutton(MyRoot, text="Female", variable=FemaleCB)
# # Label2.pack(anchor='w')
# # CB1.pack(anchor='w')
# # CB2.pack(anchor='w')
# # # Question 2 Stuff.
# # Label3 = tkinter.Label(MyRoot, text="How old are you?")
# # YoungsterCB = tkinter.IntVar()
# # TeenCB = tkinter.IntVar()
# # AdultCB = tkinter.IntVar()
# # CB3 = tkinter.Checkbutton(MyRoot, text="10-14", variable=YoungsterCB)
# # CB4 = tkinter.Checkbutton(MyRoot, text="15-19", variable=TeenCB)
# # CB5 = tkinter.Checkbutton(MyRoot, text="20+", variable=AdultCB)
# # Label3.pack(anchor='w')
# # CB3.pack(anchor='w')
# # CB4.pack(anchor='w')
# # CB5.pack(anchor='w')
# # # Question 3 Stuff.
# # Label4 = tkinter.Label(MyRoot,
# #                        text="Which of the following best describes your personality type?  (Click all that apply!)")
# # SkeetCB = tkinter.IntVar()
# # JockCB = tkinter.IntVar()
# # CoolCB = tkinter.IntVar()
# # NerdCB = tkinter.IntVar()
# # CB6 = tkinter.Checkbutton(MyRoot, text="Skeet", variable=SkeetCB)
# # CB7 = tkinter.Checkbutton(MyRoot, text="Jock", variable=JockCB)
# # CB8 = tkinter.Checkbutton(MyRoot, text="Cool", variable=CoolCB)
# # CB9 = tkinter.Checkbutton(MyRoot, text="Nerd", variable=NerdCB)
# # Label4.pack(anchor='w')
# # CB6.pack(anchor='w')
# # CB7.pack(anchor='w')
# # CB8.pack(anchor='w')
# # CB9.pack(anchor='w')
# # # And here is the results button.
# # ResultsButton = tkinter.Button(MyRoot, text="Results", command=Results)
# # ResultsButton.pack(padx=30, pady=10)
# # # And don't forget to loop your window so it actually works!
# # MyRoot.mainloop()
#
# # class TakeRoll:
# #     def __init__(self, master):
# #         self.master = master
# #         self.frame = tk.Frame(self.master)
# #         # self.present = tk.Label(self.frame, text="Present")
# #         # self.present.grid(row=0, column=0, padx=10)
# #         # self.voting = tk.Label(self.frame, text="Present\nIn Voting")
# #         # self.voting.grid(row=0, column=1, padx=10)
# #         # self.absent = tk.Label(self.frame, text="Absent")
# #         # self.absent.grid(row=0, column=2, padx=10)
# #         file = open('countries.txt', 'r')
# #         lines = file.readlines()
# #         count = 1
# #         for line in lines:  # why???
# #             # MODES = [
# #             #     ("", "present", 0),
# #             #     ("", "voting", 1),
# #             #     ("", "absent", 2)]
# #             # self.country = line
# #             # self.country = tk.StringVar()
# #             #
# #             # for text, stat, column in MODES:
# #             #     myButton = tk.Radiobutton(self.frame, text=text, variable=self.country, value=stat)
# #             #     myButton.grid(row=count, column=column)
# #             label = tk.Label(self.frame, text=line)
# #             label.grid(row=count, column=1)
# #             count += 1
# #             # status = tk.StringVar()
# #             # status.set("pepperoni")
# #             # presRadio = tk.Radiobutton(self.frame, value="present", variable=status)
# #             # presRadio.grid(row=count, column=0)
# #             # voteRadio = tk.Radiobutton(self.frame, value="in voting", variable=status)
# #             # voteRadio.grid(row=count, column=1)
# #             # absentRadio = tk.Radiobutton(self.frame, value="absent", variable=status)
# #             # absentRadio.grid(row=count, column=2)
# #         self.submit_but = tk.Button(self.frame, text="Submit", width=10, height=2, command=self.submit)
# #         self.submit_but.grid(row=(count + 1), columnspan=4, pady=(25, 0))
# #         self.frame.pack(pady=20, padx=20)
# #
# #     # (line + " " + stat).get()
# #     def clicked(self, value):
# #         myLabel = tk.Label(self.frame, text=value)
# #         myLabel.grid(row=2, column=0)
# #
# #     def submit(self):
# #         with open("countries.txt") as f:
# #             lines = f.read().splitlines()
# #         with open("countries.txt", "w") as f:
# #             for line in lines:
# #                 print(line + " " + self.country.get(), file=f)
# #         myLabel = tk.Label(self.frame, text=self.country.get())
# #         myLabel.grid(row=2, column=0)
# #         f.close()
# #
# #         # self.master.destroy()
#
#
# # with open("countries.txt") as f:
# #     lines = f.read().splitlines()
# # with open("countries.txt", "w") as f:
# #     for line, var in zip(lines, self.status):
# #         print(line + " " + var.get(), file=f)
#
#
# # import tkinter as tk
# #
# # class Demo1:
# #     def __init__(self, master):
# #         self.master = master
# #         self.frame = Frame(self.master)
# #         self.text = Text(width=30, height=20, bg="#5b92e5", padx=10, pady=10, highlightcolor="#5b92e5")
# #         self.text.pack(padx=20, pady=10)
# #         countries=self.text.get("1.0","end-1c")
# #         self.button1 = Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
# #         self.button1.pack()
# #         self.frame.pack()
# #     def new_window(self):
# #         print("hello")
# #         f = open("countries.txt", "w+")
# #         f.write(self.text.get("1.0", "end-1c"))
# #         f.close()
# #         print(self.text.get("1.0", "end-1c"))
# #         self.newWindow = Toplevel(self.master)
# #         self.app = Demo2(self.newWindow)
# #
# # class Demo2:
# #     def __init__(self, master):
# #         self.master = master
# #         self.frame = Frame(self.master)
# #         self.quitButton = Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
# #         self.quitButton.pack()
# #         self.frame.pack()
# #     def close_windows(self):
# #         self.master.destroy()
# #
# # def main():
# #     root = Tk()
# #     app = Demo1(root)
# #     root.mainloop()
# #
# # if __name__ == '__main__':
# #     main()
#
# # import PySimpleGUI as sg
# # import tkinter
# #
# #
# # def printCountries():
# #     f = open('countries.txt')
# #     lines = f.read().splitlines()
# #     f.close()
# #     for line in lines:
# #         countries.append(line)
# #
# #
# # countries = []
# # printCountries()
# # print(countries)
# # # [sg.Checkbox(), sg.Checkbox(), sg.Checkbox(), sg.Text("USA")]
# #
# # # def window1():
# # #     layout = [[sg.Text("ROLL")], [sg.Text(values['_TEXT_'])]]
# # #     window = sg.Window("ROLL", layout)
# # #     event1, values1 = window.read()
# #
# #
# # layout = [[sg.Text("Welcome to the MUN Software")], [sg.MLine(key="_TEXT_", size=(40, 20))],
# #           [sg.Button("OK"), sg.Button("CANCEL")]]
# # window = sg.Window(title="Model UN", layout=layout, margins=(500, 200))
# #
# # while True:
# #     event, values = window.read()
# #     # End program if user closes window or
# #     # presses the OK button
# #     if event == "OK":
# #         f = open("countries.txt", "w+")
# #         f.write(values["_TEXT_"])
# #         f.close()
# #         # window1()
# #         break
# #     if event == sg.WIN_CLOSED or event == "CANCEL":
# #         break
# #
# # window.close()
# #
# # countries = []
# # printCountries()
# # num = len(countries)
# #
# # layout = [ [sg.Text('ROLL')], [sg.Text('Present'), sg.Text('Voting'), sg.Text('Absent')], *[[sg.Radio('     ',
# # "STATUS"+countries[i]), sg.Radio('     ', "STATUS"+countries[i]), sg.Radio('', "STATUS"+countries[i]),
# # sg.Text(countries[i])] for i in range(num)], [sg.Button('Show'), sg.Button('Exit')] ] window = sg.Window(
# # title="Model UN", layout=layout, margins=(500, 200))
# #
# # while True:
# #     event, values = window.read()
# #     # End program if user closes window or
# #     # presses the OK button
# #     if event == sg.WIN_CLOSED or event == "CANCEL":
# #         break
# #
# # window.close()


import sounddevice as sd
from scipy.io.wavfile import write


# def record(duration):
#     freq = 44100  # Sampling frequency
#     recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)  # Start recorder with the given values of
#     # duration and sample frequency
#     sd.wait()  # Record audio for the given number of seconds
#     write('kanye.wav', freq, recording)  # This will convert the NumPy array to an audio file with the given sampling
#     # frequency
#
#
# record(10)

from threading import *
from time import *

class App1(Thread):
    def run(self):

        for i in range(5):
            print("thread 1")
            sleep(1)


class App2(Thread):
    def run(self):
        for i in range(5):
            print("thread 2")
            sleep(1)

class App3(Thread):
    def run(self):
        for i in range(5):
            print("thread 3")
            sleep(1)

app1 = App1()
app2 = App2()
app3 = App3()


app1.start()
app2.start()
app3.start()

#
# fs = 44100  # Sample rate
# seconds = 3  # Duration of recording
#
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
# sd.wait()  # Wait until recording is finished
# write('output.wav', fs, myrecording)  # Save as WAV file

