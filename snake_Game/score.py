from turtle import Turtle


class Scorebord(Turtle):
      def __init__(self):
          super().__init__()
          self.score = 0
          with open("data.txt",mode="r") as data:
              self.highscore = int(data.read())
          self.penup()
          self.color("white")
          self.goto(x=0, y=275)
          self.write(f"Score: {self.score} High_Score: {self.highscore} " , move= False , align='center', font=("Arial" , 15 , "normal"))
          self.hideturtle()

      def update_score(self):
          self.clear()
          self.write(f"Score: {self.score} High_Score: {self.highscore} " , move= False , align='center', font=("Arial" , 15 , "normal"))

      # def game_over(self):
      #     self.goto(0,0)
      #     self.write(f"GAME OVER!", move=False, align='center', font=("Arial", 15, "normal"))
      #     self.reset_score()
      #
      def increase_score(self):
          self.score += 1
          self.update_score()

      def reset_score(self):
          if self.score > self.highscore:
              self.highscore = self.score
              with open("data.txt" ,mode= "w") as data:
                  data.write(f"{self.highscore}")
              self.score = 0
              self.update_score()
