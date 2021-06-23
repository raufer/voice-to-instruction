import os

import numpy as np

import logging
import warnings


warnings.filterwarnings("ignore")

logging.getLogger("transformers.tokenization_utils_base").setLevel(logging.ERROR)

file_format ='%(asctime)s, %(name)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
console_format ='%(asctime)s, %(name)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'

logging.basicConfig(
    format=file_format,
    datefmt=console_format,
    level=logging.INFO,
    filename='training-job.log',
    filemode='w'
)

formatter = logging.Formatter(console_format)
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)

ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
