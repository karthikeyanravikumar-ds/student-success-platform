from pathlib import Path
from uuid import uuid4


def generate_filename(filename: str):

    extension = Path(filename).suffix

    return f"{uuid4()}{extension}"