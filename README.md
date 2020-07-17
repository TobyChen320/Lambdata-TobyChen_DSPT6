# Lambdata-TobyChen_DSPT6
A collection of data science utility functions.

## Installation

```py
pip install -i https://test.pypi.org/simple/ lambdata-dspt6
```

## Usage

```py
from my_lambdata.ds_utilities import train_val_test_split, remove_outliers

train
val
test
df = ...
remove_outliers(df)
```

```py
from my_lambdata.split_oop import MyDataSplitter

MyDataSplitter.train_validation_test_split(df)
MyDataSplitter.remove_outliers(df)
```