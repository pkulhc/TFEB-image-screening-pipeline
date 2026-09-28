import numpy as np
import os
from PIL import Image
import pandas as pd

"""
path = os.path.join('C:\\Lab\\NGP107Screen01012020\\Output', 'Plate1', 'A01', 'Plate1_A01_1')
os.listdir(path)

image = Image.open(os.path.join(path, 'Plate1_A01_1.png'))
image.show()
image = np.asarray(image)
image.shape

# channel 0, 1, 2, indicate R, G, B

dapi_mask = np.load(os.path.join(path, 'Plate1_A01_1_dapi_seg.npy'), allow_pickle=True).item()
dapi_area = dapi_mask['masks'] > 0
signal_nuc = (image[:, :, 1] * dapi_area).sum()
print(signal_nuc)

cyto_mask = np.load(os.path.join(path, 'Plate1_A01_1_cyto_seg.npy'), allow_pickle=True).item()
cyto_area = np.logical_and(cyto_mask['masks'] > 0, dapi_mask['masks'] == 0)
signal_cyto = (image[:, :, 1] * cyto_area).sum()

ratio = signal_nuc / signal_cyto

####
path = os.path.join('C:\\Lab\\NGP107Screen01012020\\Output', 'Plate1', 'H12', 'Plate1_H12_1')
os.listdir(path)

image = Image.open(os.path.join(path, 'Plate1_H12_1.png'))
image.show()
image = np.asarray(image)
image.shape

# channel 0, 1, 2, indicate R, G, B

dapi_mask = np.load(os.path.join(path, 'Plate1_H12_1_dapi_seg.npy'), allow_pickle=True).item()
dapi_area = dapi_mask['masks'] > 0
signal_nuc = (image[:, :, 1] * dapi_area).sum()
print(signal_nuc)

cyto_mask = np.load(os.path.join(path, 'Plate1_H12_1_cyto_seg.npy'), allow_pickle=True).item()
cyto_area = np.logical_and(cyto_mask['masks'] > 0, dapi_mask['masks'] == 0)
signal_cyto = (image[:, :, 1] * cyto_area).sum()

ratio = signal_nuc / signal_cyto
ratio
"""

path = "C:\\Lab\\L1000Library01082021\\Output"
plates = ["Plate" + str(i) for i in range(1, 29)]

num = range(1, 97)
wells = []
for i in num:
    wells.append('ABCDEFGH'[(i - 1) // 12] + '%02d' % ((i - 1) % 12 + 1))
repeats = ['1', '2', '3', '4']

results_dict = {}
for plate in plates:
    for well in wells:
        for repeat in repeats:
            try:
                id = plate + '_' + well + '_' + repeat
                image = Image.open(os.path.join(path, plate, well, id, id + '.png'))
                image = np.asarray(image)
                dapi_mask = np.load(os.path.join(path, plate, well, id, id + '_dapi_seg.npy'), allow_pickle=True).item()
                cell_num = dapi_mask['masks'].max()
                dapi_area = dapi_mask['masks'] > 0
                signal_nuc = (image[:, :, 1] * dapi_area).sum()
                cyto_mask = np.load(os.path.join(path, plate, well, id, id + '_cyto_seg.npy'), allow_pickle=True).item()
                cyto_area = np.logical_and(cyto_mask['masks'] > 0, dapi_mask['masks'] == 0)
                signal_cyto = (image[:, :, 1] * cyto_area).sum()
                ratio = signal_nuc / signal_cyto
                print(f"finish image {id}, nuc signal is {signal_nuc:.2f}, cyto signal is { signal_cyto:.2f}, +"
                  f"ratio is {ratio:.2f}")
                results_dict[id] = [id, cell_num, signal_nuc, signal_cyto, ratio]
            except:
                print(f"error processing {id}")

print(len(results_dict))

results_df = pd.DataFrame.from_dict(results_dict, orient='index', columns=['id', 'cell_number', 'signal_nuc',
                                                                           'signal_cyto', 'ratio'])
results_df.to_pickle("./ratio.pkl")
results_df.to_csv("./ratio.csv")

results_df = pd.read_pickle("./ratio.pkl")
results_df.head(10)

results_df[(results_df['ratio'] > 1.2) & (results_df['cell_number'] > 10)].head(100)

