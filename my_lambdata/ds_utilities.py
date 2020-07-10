def train_val_test_split(df):
  """
  Function will split the data set into train=80, val=10, test=10.
  Note that this is a random split and will not take certain parameters such as date into consideration.
  """
  train, val, test = np.split(df.sample(frac=1), [int(.8*len(df)), int(.9*len(df))])
  return train, val, test
def remove_outliers(df):
  """
  Function will remove 1.5 IQR outliers from data set
  """
  q1 = df.quantile(0.25)
  q3 = df.quantile(0.75)
  iqr = q3 - Q1
  df = df[~((df < (q1 - 1.5 * iqr))|(df > (q3 + 1.5 * iqr))).any(axis=1)]
  return df_o