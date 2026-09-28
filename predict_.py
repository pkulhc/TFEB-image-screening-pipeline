import os
from fastai.vision.all import *
import pandas as pd

path = "C:\\Lab\\L1000Library01082021\\Output"
plates = ["Plate" + str(i) for i in range(1, 29)]
num = range(1, 97)
wells = []
for i in num:
    wells.append('ABCDEFGH'[(i - 1) // 12] + '%02d' % ((i - 1) % 12 + 1))
repeats = ['1', '2', '3', '4']
learn = load_learner('export.pkl', cpu=False)
result = {}

for plate in plates:
    for well in wells:
        for repeat in repeats:
            id = plate + '_' + well + '_' + repeat
            image_dir = os.path.join(path, plate, well, id, 'segment_images')
            temp = []
            try:
                for file in os.listdir(image_dir):
                    if file.endswith(".png"):
                        cate, tensor, prob = learn.predict(os.path.join(image_dir, file))
                        temp.append(cate)
                cyto = temp.count('Cyto')
                nuc = temp.count('Nuc')
                result[id] = [id, cyto, nuc]
                print(f'finish {id}')
            except:
                pass
    results_df = pd.DataFrame.from_dict(result, orient='index', columns=['id', 'cyto', 'nuc'])
    results_df.to_pickle("./nuc_count.pkl")
    results_df.to_csv("./nuc_count.csv")





