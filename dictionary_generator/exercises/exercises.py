import random

from dictionary_generator.exercises.exercises_abs import ExerciseAbstract


class Rod20(ExerciseAbstract):
    _description = "Протяжка штанги к подбородку 20кг"
    _pulse = [145, 160]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Немного болят плечи",
                        "Болят плечи",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25", "4x25", "3x20", "4x20", "5x20"]
        return self._description + " " + random.choice(repeat) + "\n"


class LungesDB(ExerciseAbstract):
    _description = "Выпады с гантелями"
    _pulse = [145, 170]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят ноги",
                        "Одышка",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x15 5кг",
                  "4x15 5кг",
                  "3x20 5кг",
                  "4x20 5кг",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class PullUp(ExerciseAbstract):
    _description = "Подтягивания"
    _pulse = [145, 160]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Болят руки",
                        "Болят мышцы спины",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["2x10 ",
                  "4x15 ",
                  "3x15 ",
                  "4x12 ",
                  "3x10 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class PushUp(ExerciseAbstract):
    _description = "Отжимания"
    _pulse = [125, 150]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Болят руки",
                        "Одышка",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x20 ",
                  "4x15 ",
                  "3x15 ",
                  "4x20 ",
                  "2x30 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class ArmCurl10(ExerciseAbstract):
    _description = "Сгибание рук с гантелями 10кг"
    _pulse = [125, 150]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x25 ",
                  "3x20 ",
                  "4x20 ",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class ArmExtension5(ExerciseAbstract):
    _description = "Разгибание руки из-за головы с гантелей 5кг"
    _pulse = [135, 150]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x25 ",
                  "3x20 ",
                  "4x20 ",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class ArmAbduction5(ExerciseAbstract):
    _description = "Отведение рук с гантелями 5кг"
    _pulse = [135, 155]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Немного болят плечи",
                        "Болят плечи",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x25 ",
                  "3x20 ",
                  "4x20 ",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class ArmCurl20(ExerciseAbstract):
    _description = "Сгибание рук со штангой 20кг"
    _pulse = [135, 170]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Болят плечи",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x25 ",
                  "3x20 ",
                  "4x20 ",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class RodTraction20(ExerciseAbstract):
    _description = "Тяга штанги 20кг"
    _pulse = [135, 170]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Болят плечи",
                        "Болит спина",
                        "Немного болит спина",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x20 ",
                  "4x20 ",
                  "3x15 ",
                  "4x12",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class BackPushUp(ExerciseAbstract):
    _description = "Обратные отжимания"
    _pulse = [125, 150]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Немного болят руки",
                        "Болят плечи",
                        "Болит спина",
                        "Немного болит спина",
                        "Болят руки",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x20 ",
                  "4x20 ",
                  "3x15 ",
                  "4x12",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class Burpee(ExerciseAbstract):
    _description = "Берпи"
    _pulse = [125, 180]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "В норме",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x20 ",
                  "4x20 ",
                  "3x15 ",
                  "4x12",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class Twisting(ExerciseAbstract):
    _description = "Скручивания"
    _pulse = [125, 180]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Болит пресс",
                        "Немного болит пресс",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x20 ",
                  "3x30 ",
                  "4x25",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"


class BackTwisting(ExerciseAbstract):
    _description = "Обратные Скручивания"
    _pulse = [125, 180]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Болит пресс",
                        "Немного болит пресс",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        repeat = ["3x25 ",
                  "4x20 ",
                  "3x30 ",
                  "4x25",
                  "5x20 ",
                  ]
        return self._description + " " + random.choice(repeat) + "\n"