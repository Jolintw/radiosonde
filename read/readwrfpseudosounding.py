import numpy as np

def read_sounding_pseudo(filepath):
    var = {}
    var['p'], var['T'], var['rh'], var['u'], var['v'], var['z'], var['ws'], var['wd'] = np.loadtxt(filepath, delimiter=',', skiprows=6, unpack=True, usecols=(0,1,2,3,4,5,6,7))
    file = open(filepath)
    lines = file.readlines()
    var["project_name"] = lines[1].split()[-1]
    var["domain_name"]  = lines[2].split()[-1]
    file.close()
    return var