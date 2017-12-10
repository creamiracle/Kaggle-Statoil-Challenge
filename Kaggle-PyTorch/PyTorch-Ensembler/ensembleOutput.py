from __future__ import print_function, absolute_import

import errno
import time

import matplotlib
import torch.nn as nn
import torch.nn.init as init

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import datetime
import pandas as pd
from torch.utils.data import TensorDataset

import torch.nn.parallel
from sklearn.utils import shuffle
from torch.autograd import Variable
from torch.utils.data import TensorDataset
from torchvision.transforms import *
import numpy as np

import nnmodels as nnmodels

from os import listdir
import sys

'/home/adodd202/train.json'

/Kaggle-Statoil-Challenge/Kaggle-PyTorch/PyTorch-Ensembler/log/statoil/IceResNet/pth

input_folder = '/home/adodd202/Kaggle-Statoil-Challenge/Kaggle-PyTorch/PyTorch-Ensembler/log/statoil/IceResNet/pth'
best_base = '/home/adodd202/Kaggle-Statoil-Challenge/Kaggle-PyTorch/PyTorch-Ensembler/log/statoil/IceResNet/pth/XXXXXXX'
output_path = 'home/adodd202/Kaggle-Statoil-Challenge/Kaggle-PyTorch/PyTorch-Ensembler/log/statoil/IceResNet/pth/bestModel.csv'
MinMaxBestBaseStacking(input_folder, best_base, output_path)