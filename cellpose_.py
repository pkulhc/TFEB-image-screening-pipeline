import numpy as np
import matplotlib.pyplot as plt
import skimage.io
from cellpose import models, io
import os

os.chdir("C:\\Lab\\L1000Library01082021\\Script")
os.listdir()
os.getcwd()

"""
filename = os.path.join('..', 'Output', 'Plate1', 'A01', 'Plate1_A01_1', 'Plate1_A01_1.png')
image = skimage.io.imread(filename)
plt.imshow(image)





os.chdir("C:\\Lab\\L1000Library01082021\\Script")
os.listdir(path)

"""
# segment nuclei
path = "C:\\Lab\\L1000Library01082021\\Output"
def file_select(files):
    results = []
    for file in files:
        if file.endswith("dapi_cp_mask.png") or file.endswith("dapi_cp_output.png"):
            results.append(False)
        else:
            results.append(True)
    return all(results)


files = []
for r, d, f in os.walk(path):
    if file_select(f):
        for file in f:
            if file.endswith(".png") and not file.endswith("masks.png") and not file.endswith('output.png'):
                files.append(os.path.join(r, file))
print(files[0:10])


model = models.Cellpose(model_type='nuclei', gpu=True, torch=True)
channel = [3, 0]
channels = []
for i in range(len(files)):
    channels.append(channel)
"""
diameters = np.array([], dtype=float)
for chan, filename in zip(channels[0:40], files[0:40]):
    img = io.imread(filename)
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan, batch_size=4)
    #io.masks_flows_to_seg(img, masks, flows, diams, filename.replace('.png', '_dapi.png'), chan)
    #io.save_to_png(img, masks, flows, filename.replace('.png', '_dapi.png'))
    print(f"finish {filename}, diameter is {diams}")
    diameters = np.append(diameters, diams)

print(f'mean of diameters : {diameters.mean()}')
"""

for chan, filename in zip(channels, files):
    try:
        img = io.imread(filename)
        masks, flows, styles, diams = model.eval(img, diameter=22.5, channels=chan)
        io.masks_flows_to_seg(img, masks, flows, diams, filename.replace('.png', '_dapi.png'), chan)
        io.save_to_png(img, masks, flows, filename.replace('.png', '_dapi.png'))
        print(f'finished {filename}')
    except:
        pass
"""

# segment cytoplasm
path = "C:\\Lab\\L1000Library01082021\\Output"
os.listdir(path)

def file_select(files):
    results = []
    for file in files:
        if file.endswith("cyto_cp_mask.png") or file.endswith("cyto_cp_output.png"):
            results.append(False)
        else:
            results.append(True)
    return all(results)


files = []
for r, d, f in os.walk(path):
    if file_select(f):
        for file in f:
            if file.endswith(".png") and not file.endswith("masks.png") and not file.endswith('output.png'):
                files.append(os.path.join(r, file))
print(files[0:10])


model = models.Cellpose(model_type='cyto', gpu=True, torch=True)
channel = [[2, 3]]
channels = []
for i in range(len(files)):
    channels.append(channel)


diameters = np.array([], dtype=float)
for chan, filename in zip(channels[0:20], files[0:20]):
    img = io.imread(filename)
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan, batch_size=4)
    #io.masks_flows_to_seg(img, masks, flows, diams, filename.replace('.png', '_dapi.png'), chan)
    #io.save_to_png(img, masks, flows, filename.replace('.png', '_dapi.png'))
    print(f"finish {filename}, diameter is {diams}")
    diameters = np.append(diameters, diams)

print(f'mean of diameters : {diameters.mean()}')



for chan, filename in zip(channels, files):
    try:
        img = io.imread(filename)
        masks, flows, styles, diams = model.eval(img, diameter=36, channels=chan, batch_size=4)
        io.masks_flows_to_seg(img, masks, flows, diams, filename.replace('.png', '_cyto.png'), chan)
        io.save_to_png(img, masks, flows, filename.replace('.png', '_cyto.png'))
        print(f"finish {filename}, diameter is {diams}")
    except:
        pass
"""
