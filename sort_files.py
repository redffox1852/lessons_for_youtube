import os
import shutil

os.chdir("E:/Downloads")

files = os.listdir()


extentions = {
    "images": [".jpg", ".png", ".jpeg", ".gif", ".PNG", ".GIF", ".JPG", ".svg", ".HEIC", ".ico"],
    "videos": [".mp4", ".mkv", ".mov", ".MOV", ".MP4", ".m4a"],
    "musics": [".mp3", ".wav"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "docs": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".doc", ".xls", ".rtf"],
    "setup": [".msi", ".exe", ".iso"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP", ".txt", ".json"],
    "design": [".psd", ".xd"],
    "torrents": [".torrent"],
    "packages for Sims4": [".package"],
    "books": [".fb2"]
}


def sorting(file):
    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            if file.endswith(ext):
                return key


for file in files:
    dist = sorting(file)
    path = "../Downloads/" + dist
    if dist:
        try:
            os.mkdir(path)
        except:
            print("Folder is already exist")
        try:
            shutil.move(file, path)
        except:
            print("file is already exist")
    else:
        try:
            os.mkdir("../Downloads/other")
        except:
            print("Folder is already exist")
        try:
            shutil.move(file, "../Downloads/other")
        except:
            print("file is already exist")