import sys
from pathlib import Path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from scripts.utility.imports import *
from scripts.utility.utils import load_data


train_df,test_df = load_data()

# Feature Engineering
# 1 BMI
train_df["BMI"] = train_df["Weight"]/train_df["Height"]**2 

# 2 