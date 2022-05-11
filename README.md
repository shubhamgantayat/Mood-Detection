# Mood-Detection

## Create a Conda env
```bash
conda create --prefix ./env python==3.7 -y
```

## Activate the conda env
```bash
conda activate ./env
```

## Install the requirements file
```bash
pip install -r requirements.txt
```

## Initialization of Object Detection API
```bash
mkdir TensorFlow 
cd TensorFlow
```

## Clone the TensorFlow models folder here
```bash
git clone https://github.com/tensorflow/models.git
```

## Remove .git folder of the models directory


## Add models folder to .gitignore

## Go to TensorFlow/models/research
```bash
protoc object_detection/protos/*.proto --python_out=.
```

## Install the COCO API
```bash
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

## Install Object Detection API
```bash
cp object_detection/packages/tf2/setup.py .
python -m pip install --use-feature=2020-resolver .
```
## Test your Installation
```bash
python object_detection/builders/model_builder_tf2_test.py
```

## Go to project root folder and run the following
```bash
mkdir -p workspace/training_demo
cd workspace/training_demo
mkdir -p annotations exported-models models pre-trained-models images/test images/train
```
