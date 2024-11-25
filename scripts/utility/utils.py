import sys
from pathlib import Path

# Add the root project directory to the path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))
from scripts.utility.imports import *


def load_data():
    base_path = Path(__file__).resolve().parents[2] / 'dataset'
    train_data_path = base_path / 'train.csv'
    test_data_path = base_path / 'test.csv'
    train_df= pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    return train_df, test_df