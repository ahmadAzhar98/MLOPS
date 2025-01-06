import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging

log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'data_ingestion.log')

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

# console
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

#file 
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)