import tkinter as tk
from tkinter.ttk import Combobox
from PIL import ImageTk, Image


class View:

    def setup_window(self, controller, country):
        self.window = tk.Tk()
        self.window.geometry(f"500x500+700+300")
        self.window.title("Worldle")
        img = ImageTk.PhotoImage(file=f"country_pics/{country}.png")
        self.panel = tk.Label(self.window, image=img)
        self.panel.pack()
        self.panel.image = img
        self.information_display = tk.Label(self.window, text="Your guess")
        self.information_display.pack()
        self.combo = Combobox(self.window)
        self.combo.place(x=200, y=300)
        self.combo.pack()
        self.btn = tk.Button(self.window, text="Guess", fg='black', command=controller.process_guess)
        self.btn.place(x=250, y=350)
        self.btn.pack()

    def display_guess(self, status):
        pass

    def wrong_guess(self, guess_list):
        self.information_display[
            "text"] = f"From {guess_list[len(guess_list) - 1][0]} go {guess_list[len(guess_list) - 1][1]} " \
                      f"km to the {guess_list[len(guess_list) - 1][2]}"

    def not_a_country(self):
        self.information_display["text"] = "You chose an invalid country, try again"
        self.combo["text"] = ""

    def win(self):
        self.information_display["text"] = f"You win!! It was indeed {self.combo.get().lower().capitalize()}."
        self.btn["state"] = "disabled"

    def lose(self, country):
        self.information_display["text"] = f"You lose :( It was actually {country}."
        self.btn["state"] = "disabled"

    def display_country(self, country):
        img = ImageTk.PhotoImage(file=f"country_pics/{country}.png")
        panel = tk.Label(self.window, image=img)
        panel.pack()

    def fill_combobox(self, matrix: list):
        for m in matrix:
            if m[0] not in self.combo['values']:
                self.combo['values'] = (*self.combo['values'], m[0].replace("\"", ""))

    def start_mainloop(self):
        self.window.mainloop()

    def print_text(self, country):
        self.information_display["text"] = country

    def get_guess(self):
        return self.combo.get()
