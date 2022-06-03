import subprocess
from werkzeug.datastructures import FileStorage
from commons import Result, CompErrInfo
import os

def compile(file: FileStorage) -> Result:
    file.save('./resources/t_file.tex')
    
    result_code = 0
    err = None
    try:
        result_code = subprocess.check_call(                                                             \
            ['pdflatex', '-output-directory' '/resources', '-file-line-error', 'resources/t_file.tex']   \
        )
        
    except subprocess.CalledProcessError as e:
        result_code = e.returncode
        err = CompErrInfo(e.returncode, e.stderr)

    return Result(None, None)
