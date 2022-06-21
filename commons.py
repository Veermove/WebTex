ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def is_filename_ok(filename: str) -> bool:
    try:
        return filename and filename.split(".")[-1] in ALLOWED_EXTENSIONS
    except:
        return False
