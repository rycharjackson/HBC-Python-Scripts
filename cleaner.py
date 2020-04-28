import glob
import os
import shutil

source_dir = "C:/Users/rnelson2/Downloads"

files = glob.iglob(os.path.join(source_dir, "*"))
app_dst = "C:/Users/rnelson2/Downloads/applications"
doc_dst = "C:/Users/rnelson2/Downloads/_docs_"
config_destinations = "C:/Users/rnelson2/Downloads/configs"


for items in files:
    if items.endswith(".config"):
        print("Moving Configuration files")
        shutil.move(items, config_destinations)
        print("Move complete!")
    if items.endswith(".txt") or items.endswith(".pdf"):
        print("Moving documents.")
        shutil.move(items, doc_dst)
    if items.endswith(".exe"):
        print("Moving apps")
        shutil.move(items, app_dst)
