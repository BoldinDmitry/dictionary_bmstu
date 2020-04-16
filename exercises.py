import random

from exercises_abs import ExerciseAbstract


class Rod20(ExerciseAbstract):
    _description = "Протяжка штанги к подбородку 20кг"
    _pulse = [145, 160]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "В порядке",
                        "Легкая одышка"
                        "Немного устал",
                        "Немного болят руки",
                        "Немного болят плечи",
                        "Болят плечи",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25", "4x25", "3x20", "4x20", "5x20"]
        return self._description + random.choice(repeat)
