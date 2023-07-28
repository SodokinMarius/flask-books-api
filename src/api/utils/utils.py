import os

allowed_extensions = set(['image/jpeg','image/png','jpeg'])

def allowed_file(filename):
    name,filetype = os.path.splitext(filename)
    return  filetype in allowed_extensions