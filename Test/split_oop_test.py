import unittest
import numpy as np
import pandas as pd
from my_lambdata.split_oop import MyDataSplitter


class TestDsUtilities(unittest.TestCase):
    def test_remove_outliers(self):
        df = pd.DataFrame({'a': np.random.randint(1, 200, 20),
                           'b': np.random.randint(1, 200, 20),
                           'c': np.random.randint(1, 200, 20)})
        df[df > 150] *= 10
        current_shape = df.shape[0]
        expected_shape = current_shape - 7
        splitter = MyDataSplitter(df)
        remove_df = splitter.remove_outliers(df)
        self.assertEqual(expected_shape, remove_df.shape[0])


if __name__ == '__main__':
    unittest.main()
