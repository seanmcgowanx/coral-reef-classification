# Deep Learning Approaches for Benthic Attribute Detection in Coral Reef Images
This project explores coral reef image classification using deep learning. We use metadata and annotations from the MERMAID project along with underwater survey images stored in the public coral-reef-training S3 bucket. The goal is to compare a few baseline CNN models with a Vision Transformer and evaluate their performance in predicting benthic attributes. This is a multi label classification problem since each image can contain several benthic attributes at the same time rather than just one.<br>
<br>
All images are streamed directly from S3 at runtime and are not stored in this repository.

## Mermaid Open Data
MERMAID provides an open, standardized dataset for coral reef monitoring through underwater images and benthic annotations.
<br>
The image assets are hosted publicly on S3: <br>
<br>
**S3 bucket:**
`s3://coral-reef-training/mermaid/` <br>
<br>
**Example access (no credentials needed):**
```bash
aws s3 ls --no-sign-request s3://coral-reef-training/
```
We use three metadata files locally:
- `coral_multilabel_dataset.csv`
- `metadata_annotations.csv`
- `metadata_regions.csv`
<br>
These files describe image-level and point-level context. They are small enough to include in the repo and support reproducibility.

## Project Goals
1. Build a supervised image classification pipeline for benthic attributes.
2. Compare performance between:
- A few baseline convolutional neural networks (VGG16, ResNet-50, EfficientNet)
- A Vision Transformer
3. Stream all images directly from S3 for scalable training.
4. Explore metadata and perform feature reduction.
5. Produce a written report and final model evaluation.

## Methods Overview
### Models
- CNN baseline models using standard deep learning architecture (VGG16, ResNet-50, EfficientNet).
- Vision Transformer (ViT) using the `timm` library.
### Feature Engineering
- MERMAID benthic attributes include over 170 possible labels.
- We evaluate class frequency and select a feasible subset for training.
### Data Access
- boto3 for streaming image files from S3
- no images stored locally

## Environment Setup
To recreate the environment: 
```bash
conda env create -f environment.yml
conda activate coral-reef-classification
```
Key libraries used: 
- PyTorch + TorchVision
- boto3
- timm
- numpy, pandas, matplotlib, seaborn

## Team Members
- Sean McGowan
- Peng Wang
- Rogelio Aguilar
