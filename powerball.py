import random
from utilts import *
class Winning_Numbers():
    print("\n .....GOOD_LUCK...... \n")
    powerball_no = random.randint(1, 10)
    def win_no(self):
        print("Your random drawn winning Numbers:")
        win_no = range(1, 20)
        win_index = random.sample(win_no, k=5)
        win_index.sort()
        print(blue, win_index, yellow, self.powerball_no, reset)
        return win_index
class Lucky_Numbers():
    powerball = random.randint(1, 10)
    def lucky_no(self):
        print("Your lucky choice Numbers:")
        lucky_number = range(1, 20)
        lucky_index = random.sample(lucky_number, k=5)
        lucky_index.sort()
        print(blue, lucky_index, yellow, self.powerball, reset)
        return lucky_index
class Childclass(Winning_Numbers, Lucky_Numbers):
    def childfun(self):
        countwite = 0
        c1 = self.lucky_no()
        d1 = self.win_no()
        for i in c1:
            for j in d1:
                if i == j:
                    countwite += 1
        if countwite == 0 and self.powerball == self.powerball_no:
            print("No White Balls, Just the Powerball: $4")
        elif countwite == 1 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Ball and the Powerball: $4")
        elif countwite == 2 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: $7")
        elif countwite == 3 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: $7")
        elif countwite == 3 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: $100")
        elif countwite == 4 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: $100")
        elif countwite == 4 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: $10,000")
        elif countwite == 5 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: $1,000,000")
        elif countwite == 5 and self.powerball == self.powerball_no:
            print("Correct White Balls and the Powerball: Jackpot $324,000,000")
        else:
            print("Try again!")
