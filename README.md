# TFEB image-screening pipeline

Code and trained model weights for the AI-assisted image-based pipeline used to quantify TFEB nuclear translocation and screen candidate TFEB agonists.

This repository accompanies the manuscript **“AI-assisted image-based screening identifies TFEB agonists that restore adipose angiogenesis and reduce adipose fibrosis.”**

## Contents

- `fastai_.ipynb`: training workflow for the ResNet-18 image classifier using FastAI.
- `export.pkl`: exported trained FastAI classifier, including the trained model weights.
- `cellpose_.py`: Cellpose-based nuclear and cytoplasmic segmentation.
- `Segment_save.py`: extraction and saving of segmented single-cell images.
- `predict_.py`: classification of segmented cells as nuclear or cytoplasmic TFEB localization.
- `Ratio_.py`: calculation of nuclear-to-cytoplasmic fluorescence ratios.
- `image converter.py`: conversion of source microscopy images to PNG on Windows.
- `nuc_count.csv` and `ratio.csv`: example pipeline outputs.

## Requirements

Install the Python dependencies with:

```bash
pip install -r requirements.txt
```

The original analysis was performed with FastAI v2 and PyTorch. GPU acceleration is optional for prediction but is recommended for model training and large-scale Cellpose segmentation.

## Basic use

1. Update the input and output paths near the beginning of the relevant scripts. The archived scripts retain the original Windows directory structure used for the study.
2. Convert microscopy images with `image converter.py` when required.
3. Segment nuclei and cytoplasm with `cellpose_.py`.
4. Extract segmented single-cell images with `Segment_save.py`.
5. Train or inspect the classifier using `fastai_.ipynb`, or load the supplied trained model from `export.pkl`.
6. Classify TFEB localization with `predict_.py` and calculate nuclear-to-cytoplasmic signal ratios with `Ratio_.py`.

Example model loading:

```python
from fastai.vision.all import load_learner

learner = load_learner("export.pkl", cpu=True)
prediction = learner.predict("path/to/single_cell_image.png")
print(prediction[0])
```

## Notes

- The classifier distinguishes `Nuc` and `Cyto` image classes.
- The training notebook uses an 80:20 training-validation split with random seed 813, images resized to 224 × 224 pixels, a pretrained ResNet-18 backbone, and 30 fine-tuning epochs.
- Some scripts contain study-specific plate layouts and Windows paths and should be adapted to the local data organization before use.
- Python pickle files should only be loaded from trusted sources.

## Citation

Please cite the associated Communications Biology article and the archived repository DOI once available.
