import os
import shutil
import time
days = 30
seconds = time.time()
path = "C:/Users/SaraanshChakrabortty/Downloads"
list_of_files = os.listdir(path)
if os.path.exists(path+'/'+ext):
    os.walk(path)
    for file in list_of_files:
        name, ext = os.path.splitext(file)
        os.path.join()
        ext = ext[1:]
        if days > 30:
            os.remove(path)
            shutil.rmtree(path)
        else:
            print("Not found")
            break
