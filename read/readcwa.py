import numpy as np
import os
from os.path import isfile
from datetime import datetime as dd

def read_sounding_fix(filename):
    var = {}
    var['time_offset'], var['z'], var['p'], var['T'], var['rh'], var['Td'], var['ws'], var['wd'] = np.loadtxt(filename, delimiter=',', skiprows=2, unpack=True, usecols=(0,1,2,3,4,5,6,7))
    return var

def read_sounding_edt(filename):
    if "edt" not in filename:
        filename[-7:-4] = "edt"
    var = {}
    tempname = "temp"
    try:
        asc = np.loadtxt(filename, delimiter=',', skiprows=3)[:,-1]
    except:
        f  = open(filename)
        fo = open(tempname,"w")
        lines = f.readlines()
        newlines = []
        for i_line, line in enumerate(lines):
            if "//" in line:
                print("row {:d} is invalid".format(i_line))
                continue
            newlines.append(line)
        fo.writelines(newlines)
        filename = tempname
        asc = np.loadtxt(filename, delimiter=',', skiprows=3)[:,-1]
    
    ind = np.arange(np.shape(asc)[0])
    if np.any(asc<0):
        ind = np.min(ind[asc<0])
    else:
        ind = 99999
    print("asc<0 at",ind)
    var['time_offset'], var['alt'], var['pres'], var['tdry'], var['rh'], var['wspd'], var['deg'], var['asc'] = np.loadtxt(filename, delimiter=',', skiprows=3, max_rows=ind, unpack=True, usecols=(0,1,2,3,4,5,6,7))
    if isfile(tempname):
        os.system("rm " + tempname)
        
    var['asc'] = var['asc']/60
    # var['dp'] = mpcalc.dewpoint_from_relative_humidity(var['tdry'] * units.degC, var['rh'] * units.percent).magnitude
    var['u_wind'] = -np.sin(var['deg']/180*np.pi)*var['wspd']
    var['v_wind'] = -np.cos(var['deg']/180*np.pi)*var['wspd']
    return var
    
def read_offsettime_edt(filename):
    f = open(filename, 'r')
    line = f.readline()
    line_split = line.split()
    print(line_split)
    if "46699" in filename or "46692" in filename:
        time_str = line_split[2] + line_split[3] + line_split[4]
        m = time_str.split("/")[0]
        d = time_str.split("/")[1]
        if len(m)==1:
            m = "0" + m 
        if len(d)==1:
            d = "0" + d 
        time_str = m + d + time_str.split("/")[2]
        time = dd.strptime(time_str+"+0000", "%m%d%Y%I:%M:%S%p%z")
    else:
        time_str = line_split[2] + line_split[3]
        time = dd.strptime(time_str+"+0000", "%d/%m/%Y%H:%M:%S%z")
    f.close()
    
    return time