import os


def remove_old_img(img):
    if os.path.exists(img):
        os.remove(img)