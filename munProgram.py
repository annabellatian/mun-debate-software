from threading import *
from tkinter import *
from tkinter import font, Grid, messagebox
import sounddevice as sd
from scipy.io.wavfile import write
import pygame
import time

country_dict = {}


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x800")
        pad_frame = Frame(self.master, background="bisque")
        pad_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.master, 0, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)
        Grid.rowconfigure(pad_frame, 1, weight=4)
        Grid.columnconfigure(pad_frame, 0, weight=1)
        top_frame = Frame(pad_frame, bg="#5b92e5")
        self.take_roll_but = Button(top_frame, text="Take Roll", width=10, height=3, command=self.take_roll)
        self.take_roll_but.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.edit_roll_but = Button(top_frame, text="Edit Roll", width=10, height=3, command=self.edit_roll)
        self.edit_roll_but.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.motions_but = Button(top_frame, text="Motions", width=10, height=3, command=self.motions)
        self.motions_but.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        self.voting_but = Button(top_frame, text="Voting Procedures", width=10, height=3, command=self.voting)
        self.voting_but.pack(fill="x", side="left", padx=10, pady=10, expand="YES")
        top_frame.grid(row=0, sticky="ew")

        center_frame = Frame(pad_frame, bg="#5b92e5")
        Grid.rowconfigure(center_frame, 0, weight=1, uniform="x")
        Grid.columnconfigure(center_frame, 0, weight=1, uniform="x")
        Grid.columnconfigure(center_frame, 1, weight=1, uniform="x")
        center_frame.grid(row=1, sticky="nsew", rowspan=2)

        left_frame = Frame(center_frame, bg="#5b92e5")
        left_frame.grid(row=0, column=0, sticky="nsew")
        right_frame = Frame(center_frame, bg="#A0C1F4")
        right_frame.grid(row=0, column=1, sticky="nsew")
        topic_frame = Frame(left_frame, bg="#4478C7")
        topic_frame.grid(row=0, column=0, sticky="nsew")
        self.topic1 = Entry(topic_frame, justify='center', font=("", 42, ""))
        self.topic1.place(relx=0.5, rely=0.3, anchor="center")
        self.topic2 = Entry(topic_frame, justify='center', font=("", 36, ""))
        self.topic2.place(relx=0.5, rely=0.6, anchor="center")
        Text(right_frame, font=("", 28, "")).pack(fill="both", pady=10, padx=10)

        timer_frame = Frame(left_frame, bg="#2C5FAD")
        self.minute = StringVar()
        self.second = StringVar()

        # setting the default value as 0
        self.minute.set("00")
        self.second.set("00")
        self.state = False
        Button(timer_frame, text='Reset', command=self.reset_time, font=('Helvetica', 20)).place(relx=0.7, rely=0.7,
                                                                                                 anchor='center')
        Button(timer_frame, text='Pause', command=self.pause, font=('Helvetica', 20)).place(relx=0.5, rely=0.7,
                                                                                            anchor='center')
        Button(timer_frame, text='Start', command=self.start_timer, font=('Helvetica', 20)).place(relx=0.3, rely=0.7,
                                                                                                  anchor='center')
        self.minuteEntry = Entry(timer_frame, width=2, text="00", font=('Helvetica', 50),
                                 textvariable=self.minute)
        self.minuteEntry.place(relx=0.43, rely=0.5, anchor='center')

        self.secondEntry = Entry(timer_frame, width=2, text="00", font=('Helvetica', 50),
                                 textvariable=self.second)
        self.secondEntry.place(relx=0.58, rely=0.5, anchor='center')

        timer_frame.grid(row=1, column=0, sticky="nsew")
        Grid.rowconfigure(left_frame, 0, weight=1)
        Grid.rowconfigure(left_frame, 1, weight=1)
        Grid.columnconfigure(left_frame, 0, weight=1)
        # self.countdown(du)
        self.start()

    def start_timer(self):
        if not self.state:
            self.state = True
            self.mins = self.minute
            self.secs = self.second
            self.duration = int(int(self.minute.get()) * 60 + int(self.second.get()))
            t1 = Thread(target=self.record)
            t2 = Thread(target=self.countdown)
            t1.start()
            t2. start()

    def countdown(self):
        if self.state:
            if self.duration <= 0:
                self.error_message(1)
            while self.duration > -1:
                self.mins, self.secs = divmod(self.duration, 60)  # divmod(firstvalue = temp//60, secondvalue = temp%60)
                self.minute.set("%s" % self.mins)
                self.second.set("%s" % self.secs)
                root.update()  # updating the GUI window after decrementing the temp value every time
                time.sleep(1)
                if self.duration == 0:  # when temp value = 0; then a messagebox pop's up with a message:"Time's up"
                    pygame.mixer.init()
                    pygame.mixer.music.load("ringtone.mp3")
                    pygame.mixer.music.play(loops=0)
                    messagebox.showinfo("Time Countdown", "Time's up ")
                self.duration -= 1  # after every one sec the value of temp will be decremented by one

    def record(self):
        freq = 44100  # Sampling frequency
        recording = sd.rec(int(self.duration * freq), samplerate=freq, channels=1)  # Start recorder with the given
        # values of
        # duration and sample frequency
        sd.wait()  # Record audio for the given number of seconds
        write(self.topic1.get() + " - " + self.topic2.get() + ".wav", freq,
              recording)  # This will convert the NumPy array to an audio file with the given sampling
        # frequency

    def pause(self):  # Pause the clock
        if self.state == True:
            self.state = False

    def reset_time(self):  # Reset the clock
        self.minute.set("00")
        self.second.set("00")
        self.running = False

    def start(self):
        self.new_win = Toplevel(self.master)
        self.new_win.attributes('-topmost', 'true')
        self.app = CountryInput(self.new_win)

    def take_roll(self):
        self.new_win = Toplevel(self.master)
        self.app = TakeRoll(self.new_win)

    def edit_roll(self):
        self.new_win = Toplevel(self.master)
        self.app = EditRoll(self.new_win)

    def motions(self):
        self.new_win = Toplevel(self.master)
        self.app = Motions(self.new_win)

    def voting(self):
        self.new_win = Toplevel(self.master)
        self.app = Voting(self.new_win)

    def error_message(self, error_num):
        if error_num == 1:
            messagebox.showerror(title="Error", message="Please fill out all required fields") # fix error messages


class TakeRoll(MainApplication):
    def __init__(self, master):
        self.new_win1 = master
        self.frame = Frame(self.new_win1)
        Label(self.frame, text="Present").grid(row=0, column=0, padx=10)
        Label(self.frame, text="Present\nand Voting").grid(row=0, column=1, padx=10)
        Label(self.frame, text="Absent").grid(row=0, column=2, padx=10)
        file = open('countries.txt', 'r')
        lines = file.readlines()
        country = []
        for line in lines:
            country.append(line.split(",", 1)[0])
        count = 1
        self.status = []
        print(country)
        for x in country:
            modes_roll = [("present", 0),
                          ("voting", 1),
                          ("absent", 2)]
            var_status = StringVar()
            self.status.append(var_status)
            for stat, column in modes_roll:
                Radiobutton(self.frame, variable=var_status, value=stat).grid(row=count, column=column)
            Label(self.frame, text=x).grid(row=count, column=3)
            count += 1
        Button(self.frame, text="Submit", width=10, height=2, command=self.submit).grid(row=(count + 1), columnspan=4,
                                                                                        pady=(25, 0))
        self.frame.pack(pady=20, padx=20)

    def submit(self):
        print("status: ", self.status)
        for x in self.status:
            if x.get() == '':
                self.error_message(1)
                return 1
        country_dict.clear()
        with open("countries.txt") as f:
            for line in f:
                country_dict[(line.split(",", 1)[0]).strip()] = " "
                print(country_dict)
        for key, var in zip(country_dict, self.status):
            country_dict[key] = var.get()
        with open("countries.txt", "w") as f:
            for key, value in country_dict.items():
                f.write(key + ", " + value + "\n")
        f.close()
        print(country_dict)
        self.new_win1.destroy()


class EditRoll(MainApplication):
    def __init__(self, master):
        self.new_win1 = master
        frame = Frame(self.new_win1)
        counter = 0
        print(country_dict)
        for key in country_dict:
            Button(frame, text=key, command=lambda country=key: self.editCountry(country)).grid(row=counter + 1,
                                                                                                column=0,
                                                                                                pady=5, padx=5)
            Label(frame, text=country_dict[key]).grid(row=counter + 1, column=2)
            counter += 1
        Button(frame, text="Add country", command=lambda: self.addCountry()).grid(row=counter + 1, column=0)
        frame.pack(pady=20, padx=20)

    def editCountry(self, country):
        self.new_win2 = Toplevel(self.new_win1)
        self.new_win2.title(country)
        self.status = StringVar()
        Label(self.new_win2, text="Present").grid(row=0, column=0, padx=(15, 10), pady=10)
        Label(self.new_win2, text="Present\nand Voting").grid(row=0, column=1, padx=10, pady=10)
        Label(self.new_win2, text="Absent").grid(row=0, column=2, padx=10, pady=10)
        Radiobutton(self.new_win2, value="present", variable=self.status).grid(row=1, column=0)
        Radiobutton(self.new_win2, value="voting", variable=self.status).grid(row=1, column=1)
        Radiobutton(self.new_win2, value="absent", variable=self.status).grid(row=1, column=2)
        Label(self.new_win2, text=country).grid(row=1, column=3, padx=(0, 15))
        Button(self.new_win2, text="Submit", width=10, height=2,
               command=lambda key=country: self.submitCountry(country)).grid(row=2, columnspan=4, pady=(25, 15))

    def submitCountry(self, country):
        if self.status.get() == '':
            self.error_message(1)
            return 1
        for key in country_dict:
            if key == country:
                country_dict[key] = self.status.get()
        print(country_dict)
        with open("countries.txt", "w") as f:
            for key, value in country_dict.items():
                f.write('%s, %s\n' % (key, value))
        f.close()
        self.new_win2.destroy()
        self.new_win1.update()

    def addCountry(self):
        self.add_country_win = Toplevel(self.new_win1)
        self.add_country_win.title("Add Country")
        country_name = Entry(self.add_country_win, justify='center', font=("", 28, ""), fg='black', bg='white')
        country_name.grid(row=0, columnspan=3, padx=(15, 10), pady=10)
        self.var2 = StringVar()
        Label(self.add_country_win, text="Present").grid(row=1, column=0, padx=10, pady=10)
        Label(self.add_country_win, text="Present\nIn Voting").grid(row=1, column=1, padx=10, pady=10)
        Label(self.add_country_win, text="Absent").grid(row=1, column=2, padx=10, pady=10)
        Radiobutton(self.add_country_win, value="present", variable=self.var2).grid(row=2, column=0)
        Radiobutton(self.add_country_win, value="voting", variable=self.var2).grid(row=2, column=1)
        Radiobutton(self.add_country_win, value="absent", variable=self.var2).grid(row=2, column=2)
        Button(self.add_country_win, text="Submit", width=10, height=2,
               command=lambda key=country_name.get(): self.submitNewCountry(country_name.get())). \
            grid(row=3, columnspan=3, pady=(25, 15))

    def submitNewCountry(self, country):
        if self.var2.get() == '' or not country.strip():
            self.error_message(1)
            return 1
        country_dict[country] = self.var2.get()
        with open("countries.txt", "w") as f:
            for key, value in sorted(country_dict.items()):
                f.write('%s, %s\n' % (key, value))
        f.close()
        self.add_country_win.destroy()
        self.new_win1.update()


class CountryInput(MainApplication):
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        Label(self.frame, text="Welcome to the MUN Debate Software\nPlease enter the countries in your committee").pack(
            pady=10, padx=15)
        self.country_input = Text(self.frame, width=30, height=20, bg="#5b92e5", padx=10, pady=10,
                                  highlightcolor="#5b92e5")
        self.country_input.pack(padx=20, pady=10)
        Button(self.frame, text="Submit", width=10, height=2, command=self.submit).pack()
        self.frame.pack(pady=10)

    def submit(self):
        if not self.country_input.get("1.0").strip():
            self.error_message(1)
            return 1
        lines = self.country_input.get("1.0", "end-1c").splitlines()
        lines.sort()
        f = open("countries.txt", "w+")
        for line in lines:
            f.write(line + "\n")
            country_dict[line] = ''
        f.close()
        self.master.destroy()


class Motions:
    def __init__(self, master):
        self.new_win1 = master
        self.frame = Frame(self.new_win1)
        Label(self.new_win1, text="Motions!", font=("", 32, "")).pack(pady=(20, 15), padx=20)
        self.motion_type = ["Start of Committee", "Debate", "Voting Procedures", "End of Committee"]
        Button(self.new_win1, text=self.motion_type[0], font=("", 24, ""),
               command=lambda: self.display_motions(0)).pack(pady=10, padx=15)
        Button(self.new_win1, text=self.motion_type[1], font=("", 24, ""),
               command=lambda: self.display_motions(1)).pack(pady=10, padx=15)
        Button(self.new_win1, text=self.motion_type[2], font=("", 24, ""),
               command=lambda: self.display_motions(2)).pack(pady=10, padx=15)
        Button(self.new_win1, text=self.motion_type[3], font=("", 24, ""),
               command=lambda: self.display_motions(3)).pack(pady=(10, 20), padx=15)
        self.motions = [["Motion to open committee", "Motion to set the agenda", "Motion to open debate",
                         "Motion to open the speakers’ list", "Motion to amend the agenda"],
                        ["Motion to limit / extend speaker’s time", "Motion for a moderated caucus",
                         "Motion for an unmoderated caucus", "Motion for a roll call caucus",
                         "Motion to limit/extend debate", "Motion to introduce a working paper",
                         "Motion to introduce an amendment", "Motion to table a resolution",
                         "Motion to take from the table", "Motion to enter voting procedures"],
                        ["Motion to divide the question", "Motion to change voting style",
                         "Motion to table a resolution", "Motion to take from the table"],
                        ["Motion to suspend committee", "Motion to adjourn"]]

    def display_motions(self, type_num):
        motion_win = Toplevel(self.new_win1)
        motion_win.title(self.motion_type[type_num])
        Label(motion_win, text=self.motion_type[type_num] + " Motions", font=("", 32, "")).pack(pady=(20, 15), padx=20)
        for i in range(0, len(self.motions[type_num])):
            Label(motion_win, text=self.motions[type_num][i], font=("", 24, "")).pack(pady=(10, 20), padx=15)


class Voting(MainApplication):
    def __init__(self, master):
        self.new_win1 = master
        frame = Frame(self.new_win1)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.new_win1, 0, weight=1)
        Grid.columnconfigure(self.new_win1, 0, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        Grid.columnconfigure(frame, 1, weight=1)
        Grid.columnconfigure(frame, 2, weight=1)
        Grid.columnconfigure(frame, 3, weight=1)
        Grid.rowconfigure(frame, 0, weight=1)
        Grid.rowconfigure(frame, 1, weight=1)
        Grid.rowconfigure(frame, 2, weight=1)
        Grid.rowconfigure(frame, 3, weight=1)
        Label(frame, text="Voting Procedures", font=("", 32, "")).grid(row=0, columnspan=4, sticky="nsew")
        Label(frame, text="Type of Vote", font=("", 20, ""), justify="center").grid(row=1, column=0, pady=10,
                                                                                    padx=15)
        Label(frame, text="Voting Style", font=("", 20, ""), justify="center").grid(row=2, column=0, pady=10,
                                                                                    padx=15)
        Label(frame, text="Vote Required", font=("", 20, ""), justify="center").grid(row=3, column=0, pady=10,
                                                                                     padx=15)
        vote_type = [("substantive", 1), ("procedural", 2)]
        vote_style = [("standard", 1), ("roll call", 2), ("unanimous consent", 3)]
        vote_maj = [("simple", 1), ("2/3", 2)]
        self.var_type = StringVar()
        for x, column in vote_type:
            Radiobutton(frame, variable=self.var_type, value=x, text=x).grid(row=1, column=column, pady=10,
                                                                             padx=15)
        self.var_style = StringVar()
        for x, column in vote_style:
            Radiobutton(frame, variable=self.var_style, value=x, text=x).grid(row=2, column=column, pady=10,
                                                                              padx=15)
        self.var_maj = StringVar()
        for x, column in vote_maj:
            Radiobutton(frame, variable=self.var_maj, value=x, text=x).grid(row=3, column=column, pady=10, padx=15)
        Button(frame, text="Submit", width=10, height=2, command=self.submit_det).grid(row=4, columnspan=4)

    def submit_det(self):
        self.vote_info = [self.var_type.get(), self.var_style.get(), self.var_maj.get()]
        for x in self.vote_info:
            if x == '':
                self.error_message(1)
                return 1
        self.submit()

    def submit(self):
        self.vote_win = Toplevel(self.new_win1)
        self.vote_win.title("Model United Nations")
        pad_frame = Frame(self.vote_win)
        pad_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.vote_win, 0, weight=1)
        Grid.columnconfigure(self.vote_win, 0, weight=1)
        Grid.rowconfigure(pad_frame, 0, weight=1)
        Grid.columnconfigure(pad_frame, 0, weight=1)
        Grid.columnconfigure(pad_frame, 1, weight=1)
        Grid.columnconfigure(pad_frame, 2, weight=1)
        Grid.columnconfigure(pad_frame, 3, weight=1)
        if self.vote_info[1] == "standard":
            Label(pad_frame, text=self.vote_info[0] + ", " + self.vote_info[1] + ", " + self.vote_info[2],
                  font=("", 32, "")).grid(row=0, columnspan=3)
            yes = StringVar()
            Label(pad_frame, text="FOR", font=("", 20, "")).grid(row=1, column=0, pady=(10, 0))
            Entry(pad_frame, width=5, textvariable=yes, justify="center").grid(row=2, column=0, pady=(0, 10))
            no = StringVar()
            Label(pad_frame, text="AGAINST", font=("", 20, "")).grid(row=1, column=1, pady=(10, 0))
            Entry(pad_frame, width=5, textvariable=no, justify="center").grid(row=2, column=1, pady=(0, 10))
            abstain = StringVar()
            vote_count = [yes, no, abstain]
            if self.vote_info[0] == "substantive":
                Label(pad_frame, text="ABSTAIN", font=("", 20, "")).grid(row=1, column=2, pady=(10, 0))
                Entry(pad_frame, width=5, textvariable=abstain, justify="center").grid(row=2, column=2, pady=(0, 10))
                vote_count[2] = abstain
            else:
                abstain.set(0)
            Button(pad_frame, text="Submit", width=10, height=2, command=lambda key=vote_count: self.standard_submit(
                vote_count)).grid(row=3, columnspan=3, pady=10)
            Grid.rowconfigure(self.vote_win, 1, weight=1)
            Grid.rowconfigure(self.vote_win, 2, weight=1)
            Grid.rowconfigure(self.vote_win, 3, weight=1)
        elif self.vote_info[1] == "roll call":
            Label(pad_frame, text=self.vote_info[0] + ", " + self.vote_info[1] + ", " + self.vote_info[2],
                  font=("", 32, "")).grid(row=0, columnspan=5)
            Label(pad_frame, text="YES", font=("", 20, "")).grid(row=1, column=0, padx=10, pady=10)
            Label(pad_frame, text="NO", font=("", 20, "")).grid(row=1, column=1, padx=10, pady=10)
            vote_answer = [("YES", 0),
                           ("NO", 1)]
            if self.vote_info[0] == "substantive":
                vote_answer.append(("ABSTAIN", 2))
                Label(pad_frame, text="ABSTAIN", font=("", 20, "")).grid(row=1, column=2, padx=10, pady=10)
            file = open('countries.txt', 'r')
            lines = file.readlines()
            self.country = []
            for line in lines:
                self.country.append(line.split(",", 1)[0])
            count = 2
            self.status = []
            self.rights = []
            for key, val in country_dict.items():
                if val == "absent":
                    continue
                var_status = StringVar()
                self.status.append(var_status)
                y = 3
                if val == "voting":
                    y = 2
                for stat, column in vote_answer[0:y]:
                    Radiobutton(pad_frame, variable=var_status, value=stat).grid(row=count, column=column)
                    Grid.rowconfigure(pad_frame, count, weight=1)
                rights_var = StringVar()
                self.rights.append(rights_var)
                Checkbutton(pad_frame, variable=rights_var).grid(row=count, column=3)
                Label(pad_frame, text=key).grid(row=count, column=4, padx=10)
                count += 1
            Button(pad_frame, text="Submit", width=10, height=2, command=self.rollcall_submit).grid(row=(count + 1),
                                                                                                    columnspan=5,
                                                                                                    pady=(25, 0))
        elif self.vote_info[1] == "unanimous consent":
            Label(pad_frame, text=self.vote_info[0] + ", " + self.vote_info[1] + ", " + self.vote_info[2],
                  font=("", 32, "")).grid(row=0, columnspan=2)
            Button(pad_frame, text="PASS", width=10, height=2, command=lambda key="PASS": self.unanimous_submit(
                key)).grid(row=1, column=0, padx=(25, 0))
            Button(pad_frame, text="FAIL", width=10, height=2, command=lambda key="FAIL": self.unanimous_submit(
                key)).grid(row=1, column=1, padx=(0, 25))
            Grid.rowconfigure(pad_frame, 1, weight=1)

    def standard_submit(self, vote_count):
        print("vote_count: ", vote_count)
        for x in vote_count:
            if not x.get().strip():
                self.error_message(1)
                return 1
        self.results_win = Toplevel(self.new_win1)
        self.results_win.geometry("300x400")
        frame = Frame(self.results_win)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.results_win, 0, weight=1)
        Grid.columnconfigure(self.results_win, 0, weight=1)
        Grid.rowconfigure(frame, 0, weight=1)
        Grid.rowconfigure(frame, 1, weight=1)
        Grid.rowconfigure(frame, 2, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        result = "FAIL"
        if self.vote_info[2] == "simple":
            if vote_count[0].get() > vote_count[1].get():
                result = "PASS"
        elif self.vote_info[2] == "2/3":
            if int(vote_count[0].get()) >= (
                    (int(vote_count[0].get()) + (int(vote_count[1].get()) + (int(vote_count[2].get())))) * 2 / 3):
                result = "PASS"
        Label(frame, text=result, font=("", 32, "")).grid(row=0)
        if len(vote_count) == 3:
            Label(frame, text=vote_count[0].get() + " - " + vote_count[1].get() + " - " + vote_count[2].get(),
                  font=("", 24, "")).grid(row=1)
        else:
            Label(frame, text=vote_count[0].get() + " - " + vote_count[1].get(), font=("", 24, "")).grid(row=1)
        Button(frame, text="EXIT", width=10, height=2, command=self.exit_voting).grid(row=2)

    def rollcall_submit(self):
        yes = 0
        no = 0
        abstain = 0
        for x in self.status:
            if x.get() == "YES":
                yes += 1
            elif x.get() == "NO":
                no += 1
            elif x.get() == "ABSTAIN":
                abstain += 1
            else:
                self.error_message(1)
                return 1
        vote_count = [yes, no, abstain]
        self.rights_country = []
        count = 0
        for x in self.rights:
            if x.get():
                self.rights_country.append(count)
            count += 1
        self.results_win = Toplevel(self.new_win1)
        frame = Frame(self.results_win)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        Grid.rowconfigure(self.results_win, 0, weight=1)
        Grid.columnconfigure(self.results_win, 0, weight=1)
        Grid.rowconfigure(frame, 0, weight=1)
        Grid.rowconfigure(frame, 1, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)
        result = "FAIL"
        if self.vote_info[2] == "simple":
            if vote_count[0] > vote_count[1]:
                result = "PASS"
        elif self.vote_info[2] == "2/3":
            if int(vote_count[0]) >= ((int(vote_count[0]) + (int(vote_count[1]) + (int(vote_count[2])))) * 2 / 3):
                result = "PASS"
        Label(frame, text=result, font=("", 32, "")).grid(row=0, column=0)
        if len(vote_count) == 3:
            Label(frame, text=str(vote_count[0]) + " - " + str(vote_count[1]) + " - " + str(vote_count[2]),
                  font=("", 24, "")).grid(row=1, column=0)
        else:
            Label(frame, text=str(vote_count[0]) + " - " + str(vote_count[1]), font=("", 24, "")).grid(
                row=1, column=0)
        count = 3
        if len(self.rights_country) >= 1:
            Label(frame, text="\nRights", font=("", 28, "")).grid(row=count, column=0, padx=40)
            Grid.rowconfigure(frame, count, weight=1)
            count += 1
            print(self.rights_country)
            for x in self.rights_country:
                Label(frame, text=self.country[x], font=("", 24, "")).grid(row=count, column=0)
                Grid.rowconfigure(frame, count, weight=1)
                count += 1
        Button(frame, text="EXIT", width=10, height=2, command=self.exit_voting).grid(row=count, column=0, pady=10)
        Grid.rowconfigure(frame, count, weight=1)

    def unanimous_submit(self, result):
        if result == "FAIL":
            self.vote_info[1] = "roll call"
            self.submit()
        else:
            self.results_win = Toplevel(self.new_win1)
            self.results_win.geometry("300x400")
            frame = Frame(self.results_win)
            frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            Grid.rowconfigure(self.results_win, 0, weight=1)
            Grid.columnconfigure(self.results_win, 0, weight=1)
            Grid.rowconfigure(frame, 0, weight=1)
            Grid.columnconfigure(frame, 0, weight=1)
            Label(frame, text=result, font=("", 32, "")).grid(row=0, column=0)
            Button(frame, text="EXIT", width=10, height=2, command=self.exit_voting).grid(row=1, column=0)

    def exit_voting(self):
        self.results_win.destroy()
        self.new_win1.destroy()


root = Tk()
root.title("Model United Nations")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Calibri", size=14)
app = MainApplication(root)
root.mainloop()
