from ligotools import readligo as rl
import numpy as np
import os

def test_readhdf5_L1():
    l1 = rl.read_hdf5('data/L-L1_LOSC_4_V2-1126259446-32.hdf5')
    assert len(l1) == 7
    
def test_readhdf5_H1():
    h1 = rl.read_hdf5('data/H-H1_LOSC_4_V2-1126259446-32.hdf5')
    assert len(h1) == 7
    
def test_getsegs():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(filepath, 'H1')
    assert(len(strain_H1) == 131072)