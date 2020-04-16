import datetime
import inspect
import sys

from docx import Document

import exercises_abs
from exercises import *


def random_day(x):
    one_day = datetime.timedelta(days=1)
    return random.choice([x - one_day, x, x + one_day])


if __name__ == '__main__':
    # start_input = input("Введите дату в формате: %d-%m-%Y")
    start = datetime.datetime.strptime("21-06-2014", "%d-%m-%Y")
    end = datetime.datetime.strptime("07-07-2014", "%d-%m-%Y")

    frequency = 4

    weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    day_time = ["утро", "день"]

    date_generated = [
        random_day(start + datetime.timedelta(days=x)) for x in range(0, (end - start).days, frequency)]

    all_exercises = []
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and obj != exercises_abs.ExerciseAbstract:
            all_exercises.append(obj())

    document = Document()
    table = document.add_table(rows=1, cols=5)

    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'День недели, число, месяц, год, время занятия'
    hdr_cells[1].text = 'Содержания физкультурного занятия'
    hdr_cells[2].text = 'Пульс'
    hdr_cells[3].text = 'Самочувствие'
    hdr_cells[4].text = 'Желание заниматься'

    for date in date_generated:
        string_date = ", ".join([weekdays[date.weekday()], date.strftime("%d.%m.%Y"), random.choice(day_time)])

        random.shuffle(all_exercises)

        exercises_count = 1
        description, pulse, state_of_health = "", [], ""

        for i in range(exercises_count):
            description += (all_exercises[i].description() + " ")
            pulse.append(all_exercises[i].pulse())
            state_of_health += (all_exercises[i].state_of_health() + " ")

        pulse_int = int(sum(pulse) / len(pulse))

        row_cells = table.add_row().cells

        row_cells[0].text = string_date
        row_cells[1].text = description
        row_cells[2].text = str(pulse_int)
        row_cells[3].text = state_of_health
        row_cells[4].text = "+"

    document.save('demo.docx')
