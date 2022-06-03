ALLOWED_FILE_EXT = {'tex', 'txt'}

def is_filename_ok(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT

class Result:
    def __init__(self, val, err) -> None:
        self.ok = val
        self.err = err

    def is_err(self):
        return bool(self.err)

    def is_ok(self):
        return bool(self.ok)

    def get_ok(self):
        if self.ok:
            return self.ok
        else: 
            raise ValueError
    
    def get_err(self):
        if self.err:
            return self.err
        else: 
            raise ValueError

class CompErrInfo: 
    def __init__(self, returncode, stderr) -> None:
        self.returncode = returncode
        self.stderr = stderr
