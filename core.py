from io import TextIOWrapper
import os
import time

def add_preambule(file: TextIOWrapper):
    pass

def save_and_compile(text):
    t_file = open('./resources/t_file.tex', 'w')
    t_file.write(text)
    t_file.close()
    return compile_saved()

def compile_saved():
    os.system("pdflatex -interaction nonstopmode -output-directory /resources resources/t_file.tex > NUL 2>&1")
    time.sleep(1.5)


def change_preset(default_file_name: str):
    name = "resources/defaults/" + default_file_name
    with open("resources/t_file.tex", "w") as t_file,  open(name, "r") as template:
        for line in template:
            t_file.write(line)
        t_file.close()
        template.close()
