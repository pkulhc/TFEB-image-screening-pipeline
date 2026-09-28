from PIL import Image
import win32com.client
import os


os.chdir(r"C:\Lab\L1000Library01082021\Script")
os.listdir()
os.getcwd()

shell = win32com.client.Dispatch("WScript.Shell")

""""
# test
well = "A02"
shortcut = shell.CreateShortCut("../Plate1/Group/A02.lnk")
id = str(shortcut.Targetpath)
id = id[-4:]
path = os.path.join("../Plate1/Group", id)
images = []
for r, d, f in os.walk(path):
    for file in f:
        if file.endswith("Overlay.tif"):
            images.append(os.path.join(r, file))
print(images)
plate = "Plate1"
for i, image in enumerate(images):
    path_save = os.path.join("../Output", plate, well)
    if not os.path.exists("../Output/" + plate):
        os.mkdir("../Output/" + plate)
    path_save = os.path.join("../Output", plate, well)
    if not os.path.exists(path_save):
        os.mkdir(path_save)
    im = Image.open(image)
    path = os.path.join(path_save, plate + '_' + well + '_' + str(i + 1))
    if not os.path.exists(path):
        os.mkdir(path)
    im.save(path + "/" + plate + '_' + well + '_' + str(i + 1) + ".png")
    print(f'finished image {path + plate + "_" + well + "_" + str(i + 1) + ".png"}')
"""


# generate well id
num = range(1, 97)
wells = []
for i in num:
    wells.append('ABCDEFGH'[(i - 1) // 12] + '%02d' % ((i - 1) % 12 + 1))

plates = ["Plate" + str(i) for i in range(11, 29)]
plates
# convert all images

for plate in plates:
    for well in wells:
        shortcut = shell.CreateShortCut(os.path.join("..", plate, 'Group', well + '.lnk'))
        id = str(shortcut.Targetpath)
        id = id[-4:]
        path = os.path.join("..", plate, "Group", id)
        images = []
        for r, d, f in os.walk(path):
            for file in f:
                if file.endswith("Overlay.tif"):
                    images.append(os.path.join(r, file))
        if not os.path.exists("../Output/" + plate):
            os.mkdir("../Output/" + plate)
        path_save = os.path.join("../Output", plate, well)
        if not os.path.exists(path_save):
            os.mkdir(path_save)
        for i, image in enumerate(images):
            im = Image.open(image)
            path = os.path.join(path_save, plate + '_' + well + '_' + str(i + 1))
            if not os.path.exists(path):
                os.mkdir(path)
            im.save(path + "/" + plate + '_' + well + '_' + str(i + 1) + ".png")
            print(f'finished image {plate + "_" + well + "_" + str(i + 1) + ".png"}')




