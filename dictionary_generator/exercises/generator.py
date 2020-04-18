import inspect
import sys
from dictionary_generator.exercises import exercises_abs
from dictionary_generator.exercises.exercises import *


class Exercises:
    def __init__(self):
        self.all_exercises = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):

            if inspect.isclass(obj) and issubclass(obj, exercises_abs.ExerciseAbstract) \
                    and obj != exercises_abs.ExerciseAbstract:
                self.all_exercises.append(obj())

    def get_random_exercises(self, count):
        random.shuffle(self.all_exercises)

        description, pulse, state_of_health = "", "", ""

        for i in range(count):
            description += self.all_exercises[i].description() + "\n"
            pulse += str(self.all_exercises[i].pulse()) + "\n"
            state_of_health += self.all_exercises[i].state_of_health() + "\n"

        return description, pulse, state_of_health
