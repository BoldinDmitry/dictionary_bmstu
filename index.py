#!/usr/bin/env python3

import datetime
import time
import random
import sys
import json

import pathlib

from dictionary_generator.table.generator import Generator

def main():
    generator = Generator()

    inp = json.loads(sys.argv[1])

    dt = datetime.datetime.now() # datetime, из которой переводим в timestamp
    timestmp = str(time.mktime(dt.timetuple())) # Вот, а это timestamp
    document_name = "file_"+timestmp+"_"+str(round(random.uniform(1, 199999999)))
    document = generator.generate(
        name=inp['name'],
        date_of_birth=inp['date_of_birth'],
        group=inp['group'],
        weight=inp['weight'],
        height=inp['height'],
        start=datetime.datetime.strptime(inp['start'], "%d.%m.%Y"),
        end=datetime.datetime.strptime(inp['end'], "%d.%m.%Y"),
        frequency=int(inp['frequency']),
    )

    here = pathlib.Path(__file__).parent
    document_path = here / "output" / (document_name + ".docx")

    with open(document_path, "wb") as w:
        w.write(document.getbuffer().tobytes())

    print(document_path.name)

main()