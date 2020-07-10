import numpy as np


def train_val_test_split(df):
    """Summary Line.

    Extended description of function.

    Args:
      arg1: Function will split the data set into train=80, val=10, test=10.
      Note that this is a random split only.

    Returns:
      Will return a data set split 3 ways randomly
      with 80% being in train data set, 10% for val, and 10% in test.
    """
    train, val, test = np.split(
        df.sample(frac=1), [int(.8 * len(df)), int(.9 * len(df))])
    return train, val, test


def remove_outliers(df):
    """Summary Line.

    Extended description of function.

    Args:
      arg1: Function will remove 1.5 IQR outliers from data set.

    Returns:
      Will return a data set with outliers within the 1.5 IQR range removed.
    """
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    df = df[~((df < (q1 - 1.5 * iqr)) | (df > (q3 + 1.5 * iqr))).any(axis=1)]
    return df


class Shoe():
    def __init__(self, color, size, style=None):
        self.color = color
        self.size = size
        self.style = style

if __name__ == "__main__":
    shoe1 = Shoe(color="Black", size="11")
