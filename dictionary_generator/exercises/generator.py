import inspect
import sys
import random
from dictionary_generator.exercises import exercises_abs
from dictionary_generator.exercises.exercises import *
from dictionary_generator.exercises.warmups import *
from dictionary_generator.exercises.coldups import *


class Exercises:
    def __init__(self):

        self.all_exercises = []
        self.warms = []
        self.colds = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and issubclass(obj, exercises_abs.ExerciseAbstract) \
                    and obj != exercises_abs.ExerciseAbstract:
                self.all_exercises.append(obj())

        result = []

        for name in self.all_exercises:
            if str(name.__class__.__name__).find("WarmUp") != -1:
                self.warms.append(name)
            if str(name.__class__.__name__).find("ColdUp") != -1:
                self.colds.append(name)
            if (str(name.__class__.__name__).find("WarmUp") == -1) and (str(name.__class__.__name__).find("ColdUp") == -1):
                result.append(name)

        self.all_exercises = result

    def get_random_exercises(self, count):

        random.shuffle(self.all_exercises)

        # +warmup
        j = random.randint(0,len(self.warms)-1)
        description, pulse, state_of_health = self.warms[j].description()+"\n", str(self.warms[j].pulse())+"\n", \
                                              self.warms[j].state_of_health()+"\n"

        # +exercises
        for i in range(2,count+2):
            description += self.all_exercises[i].description() + "\n"
            pulse += str(self.all_exercises[i].pulse()) + "\n"
            state_of_health += self.all_exercises[i].state_of_health() + "\n"

        # +endup (заминка)
        j = random.randint(0,len(self.colds)-1)
        description += self.colds[j].description()+"\n"
        pulse += str(self.colds[j].pulse())+"\n"
        state_of_health += self.colds[j].state_of_health()+"\n"

        return description, pulse, state_of_health
