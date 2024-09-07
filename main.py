"""Linn Yatha Solution"""
import random , string

class Robot:

    def __init__(self):
        self.robot_name = "" 
        self.name_generator()
        print(self.robot_name)
        

    def name_generator(self):
        for i in range(5):
            if i < 2:
                self.robot_name += random.choice(string.ascii_letters).upper()
            else:
                self.robot_name += str(random.randint(0,9))


if __name__ == "__main__":
    robot_name = Robot()

"""End here"""