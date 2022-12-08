import random
from utilts import *
class Winning_Numbers():
    print("\n\33[36mPowerball Lottery, by Yeshiva using python program\33[0m")
    print(".....\33[35mGOOD_LUCK\33[0m...... ")
    # list of random number of powerball of winning_numbers from 1 up to 10
    powerball_no = random.randint(1, 10)
    def win_no(self):
        print("Your random drawn winning Numbers:")
        # list of random number of winning_numbers from 1 up to 20
        win_no = range(1, 20)
        win_index = random.sample(win_no, k=5)  # k= 5 it is five random selected numbers from winning numbers
        # sort() used to order numbers in ascending order of winning numbers after print out the result
        win_index.sort()
        # this code is to give different colors for winning numbers and powerball numbers or random selected lottery no
        print("\t", blue, win_index, yellow, self.powerball_no, reset)
        return win_index
class Lucky_Numbers():
    # list of random number of powerball of lucky_numbers from 1 up to 10
    powerball = random.randint(1, 10)
    def lucky_no(self):
        print("Your lucky choice Numbers:")
        # list of random number of Lucky_Numbers from 1 up to 20
        lucky_number = range(1, 20)
        lucky_index = random.sample(lucky_number, k=5)  # k= 5 it is fiv  random selected numbers from Lucky_numbers
        # sort() used to order numbers in ascending order for lucky_numbers after print out the result
        lucky_index.sort()
        # to give color of lucky numbers and luck powerball
        print("\t", blue, lucky_index, yellow, self.powerball, reset)
        return lucky_index
class Optionc_Get(Winning_Numbers, Lucky_Numbers):
    # this will be how we check our winning_number numbers and lucky_numbers with powerball
    def optionfun(self):
        countwite = 0  # will count how many white balls we match
        c1 = self.lucky_no()
        d1 = self.win_no()
        # will check numbers for matches
        for i in c1:
            for j in d1:
                if i == j:
                    countwite += 1
                    # check for prizes and compared match balls
        if countwite == 0 and self.powerball == self.powerball_no:
            print("No White Balls, Just the Powerball: \33[32m$4\33[0m")
        elif countwite == 1 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Ball and the Powerball: \33[32m$4\33[0m")
        elif countwite == 2 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: \33[32m$7\33[0m")
        elif countwite == 3 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: \33[32m$7\33[0m")
        elif countwite == 3 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: \33[32m$100\33[0m")
        elif countwite == 4 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: \33[32m$100\33[0m")
        elif countwite == 4 and self.powerball == self.powerball_no:
            print(countwite, "Correct White Balls and the Powerball: \33[32m$10,000\33[0m")
        elif countwite == 5 and self.powerball != self.powerball_no:
            print(countwite, "Correct White Balls, but no Powerball: $1,000,000")
        elif countwite == 5 and self.powerball == self.powerball_no:
            print("Correct White Balls and the Powerball: Jackpot $324,000,000")
        else:
            print("\33[31mTry again!\33[0m")
