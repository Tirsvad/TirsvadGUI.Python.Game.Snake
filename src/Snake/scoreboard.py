from turtle import Turtle
import os.path
import json
from tkinter import simpledialog, messagebox
from constants import *


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.user_name = ""
        # if game_data file is missing we populate game_data with a dict
        self.game_data = {
            "last_user": "",
            "high_score": [
                {
                    "name": "Tirsvad GUI",
                    "score": 1
                },
            ]
        }
        self.x_cor = 0
        self.y_cor = 200
        if os.path.isfile(DATA_FILE):
            with open(DATA_FILE) as f:
                self.game_data = json.load(f)
        self.user_name = simpledialog.askstring(title="User name", prompt="Please enter your name",
                                                initialvalue=self.game_data["last_user"])
        self.game_data.update({"last_user": self.user_name})
        with open(DATA_FILE, "w") as f:
            json_dumps_str = json.dumps(self.game_data, indent=4)
            print(json_dumps_str, file=f)

    def update_scoreboard(self):
        self.write(arg=f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.update_scoreboard()
        self.print_line(f"Game over", font_type="bold")
        self.print_line("")
        i = self.check_if_new_highscore()
        if i != "":
            self.print_line(f"You got a high score")

        for index in range(0, len(self.game_data["high_score"])):
            if index == i:
                self.print_line(
                    f"{self.game_data['high_score'][index]['name']:<25}  \
                        {self.game_data['high_score'][index]['score']:>5}",
                    font_type="bold"
                )
            else:
                self.print_line(
                    f"{self.game_data['high_score'][index]['name']:<25}  \
                        {self.game_data['high_score'][index]['score']:>5}"
                )

        return messagebox.askyesno(title="Snake message", message="Continue game?")

    def check_if_new_highscore(self):
        for index in range(0, len(self.game_data["high_score"])):
            if self.score >= self.game_data["high_score"][index]["score"]:
                self.game_data["high_score"].insert(index, {"name": self.user_name, "score": self.score})
                if len(self.game_data["high_score"]) > 5:
                    del self.game_data["high_score"][-1]
                with open(DATA_FILE, "w") as f:
                    json.dump(self.game_data, f, indent=4)
                return index

    def print_line(self, msg: str = "", font_type: str = "normal"):
        self.goto(self.x_cor, self.y_cor)
        self.write(msg, align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, font_type))
        self.y_cor -= FONT_SIZE + 6

    def reset_score(self):
        self.goto(0, 270)
        self.x_cor = 0
        self.y_cor = 200
        self.clear()
        self.update_scoreboard()
