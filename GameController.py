import pandas as pd
import numpy as np
import geopy.distance as dist
import random
from Model import Model
from GameGui import View


class Controller:
    def __init__(self, model: Model, view: View):
        self.game_status = []
        self.model = model
        self.view = view
        self.read_file("countries_codes_and_coordinates.csv")
        self.choose_country(self.model.countries)
        view.setup_window(self, self.model.chosen_country[0])
        view.fill_combobox(self.model.countries)

    def process_guess(self, *args):
        guess = self.view.get_guess()
        if not self.read_input(guess):
            self.view.not_a_country()
        else:
            if self.model.chosen_country[0].upper() == guess.upper():
                self.view.win()
            else:
                self.game_status.append(
                    [self.model.guess[0], self.calc_distance(self.model.chosen_country, self.model.guess),
                     self.calc_direction(self.model.chosen_country, self.model.guess)])
                if len(self.game_status) == 6:
                    self.view.lose(self.model.chosen_country[0])
                else:
                    self.view.wrong_guess(self.game_status)

    def start_game(self):
        # self.view.display_country(self.model.chosen_country[0])
        self.view.start_mainloop()

    def read_file(self, data_location):
        self.model.countries = pd.read_csv(f"{data_location}").to_numpy()

    def read_input(self, guess) -> list:
        countries = self.model.countries
        for i in range(0, len(countries)):

            current_country = countries[i][0]
            if current_country.upper() == guess.upper():
                self.model.guess = [countries[i][0], countries[i][4].replace("\"", ""),
                                    countries[i][5].replace("\"", "")]
                return True

        return False

    def choose_country(self, countries: np.array) -> list:
        chosen = random.randint(0, len(countries))
        self.model.chosen_country = [countries[chosen][0], countries[chosen][4].replace("\"", ""),
                                     countries[chosen][5].replace("\"", "")]

    def calc_distance(self, country: list, guess: list) -> int:
        loc1 = [float(country[1]), float(country[2])]
        loc2 = [float(guess[1]), float(guess[2])]
        return int(dist.distance(loc1, loc2).km)

    def re_calc_longitude(self, lon: int) -> int:
        if lon < 0:
            lon = abs(lon)
        else:
            lon = 180 + (180 - lon)
        return lon

    def calc_direction(self, country: list, guess: list) -> str:
        latitude = ""
        if float(country[1].strip(" ")) > float(guess[1].strip(" ")) + 10:
            latitude = "North-"
        elif float(country[1].strip(" ")) < float(guess[1].strip(" ")) + 10:
            latitude = "South-"
        lon_country = self.re_calc_longitude(float(country[2].strip(" ")))
        lon_guess = self.re_calc_longitude(float(guess[2].strip(" ")))

        if lon_guess - lon_country > 0:
            if lon_guess - lon_country < 180:
                longitude = "East"
            else:
                longitude = "West"
        else:
            if abs(lon_guess - lon_country) < 180:
                longitude = "West"
            else:
                longitude = "East"

        return latitude + longitude
