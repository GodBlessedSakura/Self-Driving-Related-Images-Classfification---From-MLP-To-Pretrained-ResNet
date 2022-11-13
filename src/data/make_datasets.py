import os
import time
import requests
import pandas as pd
from tqdm import tqdm


def define_path_to_file(path_to_file):
    os.chdir(path_to_file)
    print(os.getcwd())

define_path_to_file(path_to_file="../../data")
# os.getcwd()