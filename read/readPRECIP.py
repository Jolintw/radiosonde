import numpy as np

def read_sounding_L2(filepath):
    var = {}
    var['time_offset'], var['p'], var['T'], var['rh'], var['ws'], var['wd'], var['z'], var['Td'], var['u'], var['v'] = np.loadtxt(filepath, delimiter=',', skiprows=46, unpack=True, usecols=(1,2,3,4,5,6,9,11,12,13))
    return var