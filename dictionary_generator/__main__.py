import datetime

import pathlib

from dictionary_generator.table.generator import Generator


def main():
    name = input("ФИО:\n")
    date_of_birth = input("Дата рождения:\n")
    group = input("Группа:\n")
    weight = input("Вес:\n")
    height = input("Рост:\n")

    document_name = input("название документа:\n")

    while True:
        start_str = input("дата начала занятий, формат: %d.%m.%Y:\n")
        try:
            start = datetime.datetime.strptime(start_str, "%d.%m.%Y")
        except ValueError:
            print("некоректная дата")
        else:
            break

    while True:
        end_str = input("дата конца занятий, формат: %d.%m.%Y:\n")
        try:
            end = datetime.datetime.strptime(end_str, "%d.%m.%Y")
        except ValueError:
            print("некоректная дата")
        else:
            break

    while True:
        try:
            frequency = int(input("Количество занятий в день?\n"))
        except ValueError:
            print("некоректное число")
        else:
            break

    generator = Generator()

    document = generator.generate(
        name=name,
        date_of_birth=date_of_birth,
        group=group,
        weight=weight,
        height=height,
        start=start,
        end=end,
        frequency=frequency,
    )

    here = pathlib.Path(__file__).parent
    document_path = here / (document_name + ".docx")

    with open(document_path, "wb") as w:
        w.write(document.getbuffer().tobytes())

    print("Документ успешно сохранен в ", document_path)


if __name__ == "__main__":
    main()
