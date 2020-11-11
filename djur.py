import foodmanager
import hygienemanager
import healthmanager

import datetime
import random

class Djur:

    def __init__(self, namn):
        self.__namn = namn
        
        self.__birth = datetime.datetime.now()
        self.__last_updated = datetime.datetime.now()
        
        self.foodmanager = foodmanager.FoodManager()
        self.hygienmanager = hygienemanager.HygieneManager()
        self.healthmanager = healthmanager.HealthManager()


        self.__faces = ('XP', ":'(", ':(', ':|', ':)', ':D')


    def update(self):
        """
        Uppdaterar djurets delar.
        """

        elapsed_seconds = (datetime.datetime.now() - self.__last_updated).total_seconds()
        self.__last_updated = datetime.datetime.now()

        self.foodmanager.update(elapsed_seconds)
        self.hygienmanager.update(elapsed_seconds)
        self.healthmanager.update(elapsed_seconds)


    def status(self, test_mode=False):
        """
        Uppdaterar, beräknar status och returnerar en ansiktsstring.
        """
        
        self.update()

        # Kolla om död
        if min(self.foodmanager.hunger, self.hygienmanager.hygiene, self.healthmanager.happiness) < 0:
            status = -1
        
        elif max(self.foodmanager.hunger, self.hygienmanager.hygiene, self.healthmanager.happiness) > 100:
            status = -1
        
        else:
            status = min(self.foodmanager.hunger, self.hygienmanager.hygiene, self.healthmanager.happiness)

        if test_mode:
            print(f'Food: {self.foodmanager.hunger}, Hygiene: {self.hygienmanager.hygiene}, Happiness: {self.healthmanager.happiness}')
        

        if status <= 0:
            return self.__faces[0]
        elif status <= 20:
            return self.__faces[1]
        if status <= 40:
            return self.__faces[2]
        if status <= 60:
            return self.__faces[3]
        if status <= 80:
            return self.__faces[4]
        else:
            return self.__faces[5]