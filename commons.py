ALLOWED_FILE_EXT = {'tex', 'txt'}

def is_filename_ok(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_EXT
