from pathlib import Path
from shutil import rmtree
from main import skip_prompts


def checkFileExistsAndDelete(filepath):
    file = Path(filepath)
    if file.exists() and (skip_prompts or input(f"The file {filepath} exists but should have been removed. Do you want to delete it? (y/n) ") == 'y'):
        try:
            if file.is_file():
                file.unlink()
            else:
                rmtree(filepath)
        except PermissionError:
            print(f"Unable to remove file {filepath} : Permission Error")
