import subprocess
import os
import time
from werkzeug.datastructures import FileStorage
from commons import Result, CompErrInfo

def compile_file(file: FileStorage) -> Result:
    file.save('./resources/t_file.tex')
    # return compile_saved()sss

def save_and_compile(text) -> Result:
    t_file = open('./resources/t_file.tex', 'w')
    t_file.write(text)
    t_file.close()
    return compile_saved()

def compile_saved() -> Result:
    result_code = 0
    os.system("pdflatex -interaction nonstopmode -output-directory /resources resources/t_file.tex > NUL 2>&1")
    time.sleep(1.5)
