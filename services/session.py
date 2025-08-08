latest_image_path: str | None = None

def set_latest_image(path: str):
    global latest_image_path
    latest_image_path = path

def get_latest_image() -> str | None:
    return latest_image_path
