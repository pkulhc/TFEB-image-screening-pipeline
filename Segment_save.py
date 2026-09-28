from skimage import io, transform, util
import os
import imageio
import numpy as np
from skimage.measure import regionprops

"""
path = os.path.join('C:\\Lab\\NGP107Screen01012020\\Output', 'Plate1', 'A01', 'Plate1_A01_1')
os.listdir(path)

image = imageio.imread(os.path.join(path, 'Plate1_A01_1.png'))
image = util.img_as_float32(image)
image[:, :, 2] /= 3

cyto_mask = np.load(os.path.join(path, 'Plate1_A01_1_cyto_seg.npy'), allow_pickle=True).item()
pad = 0
area = np.array([], dtype=float)
cropped_images = []
for region_index, region in enumerate(regionprops(cyto_mask['masks'])):
    area = np.append(area, region.area)
    if region.area < 500:
        continue
    minr, minc, maxr, maxc = region.bbox
    print(minr - pad , minc - pad , maxr + pad , maxc + pad)
    cropped_images.append(image[minr - pad:maxr + pad, minc - pad:maxc + pad, :])

out_dir = os.path.join(path, 'segment_images')
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# save each cropped image by its index number
for c, cropped_image in enumerate(cropped_images):
    image_save = transform.rescale(cropped_image, scale=2, multichannel=True)
    image_save = util.img_as_ubyte(image_save)
    imageio.imsave(os.path.join(out_dir, str(c) + ".png"), image_save)
"""
path = "C:\\Lab\\L1000Library01082021\\Output"
plates = ["Plate" + str(i) for i in range(1, 29)]
num = range(1, 97)
wells = []
for i in num:
    wells.append('ABCDEFGH'[(i - 1) // 12] + '%02d' % ((i - 1) % 12 + 1))
repeats = ['1', '2', '3', '4']


for plate in plates:
    for well in wells:
        for repeat in repeats:
            try:
                id = plate + '_' + well + '_' + repeat
                image = imageio.imread(os.path.join(path, plate, well, id, id + '.png'))
                image = util.img_as_float32(image)
                image[:, :, 2] /= 3
                cyto_mask = np.load(os.path.join(path, plate, well, id, id + '_cyto_seg.npy'), allow_pickle=True).item()
                cropped_images = []
                for region_index, region in enumerate(regionprops(cyto_mask['masks'])):
                    if region.area < 500:
                        continue
                    minr, minc, maxr, maxc = region.bbox
                    mask = (cyto_mask['masks'] == region.label)
                    mask = np.asarray(mask, dtype=int)
                    mask = mask[:, :, np.newaxis]
                    image_crop = image * mask
                    cropped_images.append(image_crop[minr:maxr, minc:maxc, :])

                out_dir = os.path.join(path, plate, well, id, 'segment_images')
                if not os.path.exists(out_dir):
                    os.makedirs(out_dir)

                # save each cropped image by its index number
                for c, cropped_image in enumerate(cropped_images):
                    image_save = transform.rescale(cropped_image, scale=2, multichannel=True)
                    image_save = util.img_as_ubyte(image_save)
                    imageio.imsave(os.path.join(out_dir, id + '_' + str(c) + ".png"), image_save)

                print(f'finish {id}')
            except:
                print(f"error processing {id}")

"""
plate = plates[0]
well = wells[0]
repeat = repeats[0]

id = plate + '_' + well + '_' + repeat
image = imageio.imread(os.path.join(path, plate, well, id, id + '.png'))
image = util.img_as_float32(image)
image[:, :, 2] /= 3
cyto_mask = np.load(os.path.join(path, plate, well, id, id + '_cyto_seg.npy'), allow_pickle=True).item()
cropped_images = []
mask_list = []
for region_index, region in enumerate(regionprops(cyto_mask['masks'])):
    print(region_index, region.label)
    if region.area < 500:
        continue
    minr, minc, maxr, maxc = region.bbox
    mask = (cyto_mask['masks'] == region.label)
    mask =  np.asarray(mask, dtype=int)
    mask = mask[:, :, np.newaxis]
    image_crop = image * mask
    cropped_images.append(image_crop[minr:maxr, minc:maxc, :])
    mask_list.append(mask)

    out_dir = os.path.join(path, plate, well, id, 'segment_images')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

print(len(mask_list))
print(region_index)
print(cyto_mask['masks'].max())


# save each cropped image by its index number
for c, cropped_image in enumerate(cropped_images):
    image_save = transform.rescale(cropped_image, scale=2, multichannel=True)
    image_save = util.img_as_ubyte(image_save)
    imageio.imsave(os.path.join(out_dir, id + '_' + str(c) + ".png"), image_save)
"""