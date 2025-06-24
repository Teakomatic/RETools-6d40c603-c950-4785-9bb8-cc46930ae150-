import os
from conf import CAD_TYPES, IMG_TYPES
import rhinoscriptsyntax as rs
import Rhino

def current_folder():
    return Rhino.ApplicationSettings.FileSettings.WorkingFolder


def get_files_recursive(folder, filetypes):
    result = []

    for root, _, files in os.walk(folder):
        for file in files:
            for ext in filetypes:
                if file.lower().endswith("." + ext):
                    result.append(os.path.join(root, file))
                    break
    return result


def get_imgs_recursive(folder):
    img_types = IMG_TYPES
    return get_files_recursive(folder, img_types)


def get_dxfs_recursive(folder):
    return get_files_recursive(folder, CAD_TYPES)


def name(file):
    return file.split("\\")[-1]
