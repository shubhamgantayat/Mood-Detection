import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import shutil
from bs4 import BeautifulSoup


def get_xml_path(image_path):
    image_path = str(image_path)
    return image_path[:-3] + "xml"


def get_class(xml_path):
    try:
        with open(xml_path, 'r') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        return bs_data.find_all("object")[-1].find("name").getText()
    except Exception as e:
        return None


def save_image_and_xml(img_path, xml_path, path):
    try:
        shutil.copy(img_path, path)
        shutil.copy(xml_path, path)
        return True
    except Exception as e:
        return False


def train_test_split_images(src, dest):
    train_path = os.path.join(dest, "train")
    test_path = os.path.join(dest, "test")
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)
    src_path = Path(src)
    image_files = src_path.glob("*.jpg")
    image_df = pd.DataFrame()
    image_df["image_path"] = list(map(lambda x:str(x), image_files))
    image_df["xml_path"] = image_df["image_path"].apply(get_xml_path)
    image_df["class"] = image_df["xml_path"].apply(get_class)
    X = image_df.drop(columns=["class"]).values
    y = image_df["class"].values
    for train_ix, test_ix in StratifiedShuffleSplit(n_splits=1, test_size=0.2).split(X, y):
        X_train = X[train_ix]
        X_test = X[test_ix]
        y_train = y[train_ix]
        y_test = y[test_ix]
    list(map(lambda x: save_image_and_xml(x[0], x[1], train_path), X_train))
    list(map(lambda x: save_image_and_xml(x[0], x[1], test_path), X_test))


def main():
    src = "raw_data/images/"
    dest = "images/"
    train_test_split_images(src, dest)


main()
