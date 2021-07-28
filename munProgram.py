from tkinter import *
from tkinter import font, Grid
import time

dict = {}


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x800")
        self.pad_frame = Frame(self.master, background="bisque")
        self.pad_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.master, 0, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)

        Grid.rowconfigure(self.pad_frame, 1, weight=4)
        Grid.columnconfigure(self.pad_frame, 0, weight=1)
        self.topFrame = Frame(self.pad_frame, bg='red')
        self.takeRoll = Button(self.topFrame, text="Take Roll", width=10, height=3, command=self.takeRoll)
        self.takeRoll.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.editRoll = Button(self.topFrame, text="Edit Roll", width=10, height=3, command=self.editRoll)
        self.editRoll.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.butt1 = Button(self.topFrame, text="Button3", width=10, height=3)
        self.butt1.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.butt2 = Button(self.topFrame, text="Button4", width=10, height=3)
        self.butt2.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.topFrame.grid(row=0, sticky="ew")

        self.centerFrame = Frame(self.pad_frame, bg='pink')
        Grid.rowconfigure(self.centerFrame, 0, weight=1, uniform="x")
        Grid.columnconfigure(self.centerFrame, 0, weight=1, uniform="x")
        Grid.columnconfigure(self.centerFrame, 1, weight=1, uniform="x")
        # tabControl = tNotebook(self.centerFrame)
        # tab1 = tFrame(tabControl)
        # tab2 = tFrame(tabControl)
        # tabControl.add(tab1, text='Tab 1')
        # tabControl.add(tab2, text='Tab 2')
        # tabControl.grid(column=0, row=0, padx=30, pady=30)
        # tLabel(tab1, text="”Welcome to GeeksForGeeks”").grid(column=0, row=0, padx=30, pady=30)
        # tLabel(tab2, text="”Lets dive into the world of computers”").grid(column=0, row=0, padx=30, pady=30)

        self.leftFrame = Frame(self.centerFrame, bg='orange')
        self.leftFrame.grid(row=0, column=0, sticky="nsew")
        self.rightFrame = Frame(self.centerFrame, bg='green')
        self.rightFrame.grid(row=0, column=1, sticky="nsew")
        self.topicFrame = Frame(self.leftFrame, bg='pink')
        self.topicFrame.grid(row=0, column=0, sticky="nsew")
        self.topiccc = Label(self.topicFrame, text="TOPIC")
        self.topiccc.place(relx=0.5, rely=0.5, anchor="center")

        # self.crossOut = Button(self.rightFrame, text="cross out words", command=self.strikethru())
        # self.crossOut.pack(side="top", pady=(10, 0), padx=10)

        self.spkrlist = Text(self.rightFrame, font=("", 28, ""))
        self.spkrlist.tag_configure("overstrike", overstrike=True)
        self.spkrlist.pack(fill="both", pady=10, padx=10)

        self.timerFrame = Frame(self.leftFrame, bg='purple')
        self.label = Label(self.timerFrame, text="")
        self.label.place(relx=0.5, rely=0.5, anchor="center")
        self.update_clock()

        self.timerFrame.grid(row=1, column=0, sticky="nsew")
        Grid.rowconfigure(self.leftFrame, 0, weight=1)
        Grid.rowconfigure(self.leftFrame, 1, weight=1)
        Grid.columnconfigure(self.leftFrame, 0, weight=1)
        self.centerFrame.grid(row=1, sticky="nsew", rowspan=2)

        self.start()

    def start(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.attributes('-topmost', 'true')
        self.app = CountryInput(self.newWindow)

    def takeRoll(self):
        self.newWindow = Toplevel(self.master)
        self.app = TakeRoll(self.newWindow)

    def editRoll(self):
        self.newWindow = Toplevel(self.master)
        self.app = EditRoll(self.newWindow)

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.master.after(1000, self.update_clock)

    # def strikethru(self):
    #     self.spkrlist.tag_add("overstrike", "insert-1c", "insert")
    #
    #     # move the cursor to the previous position
    #     self.spkrlist.mark_set("insert", "insert-1c")
    # self.content = self.spkrlist.selection_get()
    # f = font.Font(self.content, self.content.cget("font"))
    # f.configure(overstrike=True)
    # self.content.configure(font=f)


class TakeRoll:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.present = Label(self.frame, text="Present")
        self.present.grid(row=0, column=0, padx=10)
        self.voting = Label(self.frame, text="Present\nIn Voting")
        self.voting.grid(row=0, column=1, padx=10)
        self.absent = Label(self.frame, text="Absent")
        self.absent.grid(row=0, column=2, padx=10)
        file = open('countries.txt', 'r')
        lines = file.readlines()
        count = 1
        self.status = []
        for line in lines:  # why???
            MODES = [("present", 0),
                     ("voting", 1),
                     ("absent", 2)]
            var = StringVar()
            self.status.append(var)
            for stat, column in MODES:
                myButton = Radiobutton(self.frame, variable=var, value=stat)
                myButton.grid(row=count, column=column)
            label = Label(self.frame, text=line)
            label.grid(row=count, column=3)
            count += 1
        self.submit_but = Button(self.frame, text="Submit", width=10, height=2, command=self.submit)
        self.submit_but.grid(row=(count + 1), columnspan=4, pady=(25, 0))
        self.frame.pack(pady=20, padx=20)

    # (line + " " + stat).get()
    def clicked(self, value):
        myLabel = Label(self.frame, text=value)
        myLabel.grid(row=2, column=0)

    def submit(self):
        with open("countries.txt") as f:
            lines = f.read().splitlines()
        with open("countries.txt", "w") as f:
            for line, var in zip(lines, self.status):
                print(line + ", " + var.get(), file=f)
        with open("countries.txt") as f:
            for line in f:
                (key, val) = line.split(", ")
                dict[key] = val
        f.close()
        self.master.destroy()


class EditRoll:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        # self.present = Label(self.frame, text="Present")
        # self.present.grid(row=0, column=0, padx=10)
        # self.voting = Label(self.frame, text="Present\nIn Voting")
        # self.voting.grid(row=0, column=1, padx=10)
        # self.absent = Label(self.frame, text="Absent")
        # self.absent.grid(row=0, column=2, padx=10)
        file = open('countries.txt', 'r')
        lines = file.readlines()
        self.counter = 0
        for key in dict:
            button = Button(self.frame, text=key, command=lambda key=key: self.editCountry(key)).grid(row=self.counter + 1,
                                                                                              column=0, pady=5,
                                                                                              padx=5)
            label = Label(self.frame, text=dict[key]).grid(row=self.counter + 1, column=2)
            self.counter += 1
        self.frame.pack(pady=20, padx=20)

    def editCountry(self, country):
        self.newWindow2 = Toplevel(self.master)
        self.newWindow2.title(country)
        present = Label(self.newWindow2, text="Present").grid(row=0, column=0, padx=(15, 10), pady=10)
        voting = Label(self.newWindow2, text="Present\nIn Voting").grid(row=0, column=1, padx=10, pady=10)
        absent = Label(self.newWindow2, text="Absent").grid(row=0, column=2, padx=10, pady=10)
        self.var2 = StringVar()
        presRadio2 = Radiobutton(self.newWindow2, value="present", variable=self.var2).grid(row=1, column=0)
        voteRadio2 = Radiobutton(self.newWindow2, value="in voting", variable=self.var2).grid(row=1, column=1)
        absentRadio2 = Radiobutton(self.newWindow2, value="absent", variable=self.var2).grid(row=1, column=2)
        label2 = Label(self.newWindow2, text=country).grid(row=1, column=3, padx=(0, 15))
        submit_but2 = Button(self.newWindow2, text="Submit", width=10, height=2, command=self.submitCountry(country)). \
            grid(row=2, columnspan=4, pady=(25, 15))
        print(country)

    def submitCountry(self, country):
        for key in dict:
            if key == country:
                dict[key] = self.var2.get()
        with open("countries.txt", "w") as f:
            for key, value in dict.items():
                f.write('%s, %s\n' % (key, value))
        f.close()
        # self.newWindow2.destroy()

    def submit(self):
        with open("countries.txt") as f:
            for line in f:
                (key, val) = line.split(", ")
                dict[int(key)] = val
        with open("countries.txt", "w") as f:
            for key, value in dict.items():
                f.write('%s, %s\n' % (key, value))
        f.close()
        self.master.destroy()


class CountryInput:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.label = Label(self.frame,
                           text="Welcome to the MUN Debate Software\nPlease enter the countries in your committee")
        self.label.pack(pady=10, padx=15)
        self.text = Text(self.frame, width=30, height=20, bg="#5b92e5", padx=10, pady=10,
                         highlightcolor="#5b92e5")
        self.text.pack(padx=20, pady=10)
        self.submit_but = Button(self.frame, text="Submit", width=10, height=2, command=self.submit)
        self.submit_but.pack()
        self.frame.pack(pady=10)

    def submit(self):
        lines = self.text.get("1.0", "end-1c").splitlines()
        lines.sort()
        f = open("countries.txt", "w+")
        for line in lines:
            f.write(line + "\n")
        f.close()
        self.master.destroy()


def main():
    root = Tk()
    root.title("Model United Nations")
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Calibri", size=14)
    app = MainApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
