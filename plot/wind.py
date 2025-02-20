
import numpy as np
from mypkgs.atmos_function import wswd_to_uv
from mypkgs.plotter.plotter import Plotter

figsize = [7, 8]
def uvplot_z(var, ylim = [250, 5000], xlim = [-5, 30], figsize = figsize):
    Pt = Plotter(figsize = figsize)#figsize = [6, 8])
    # Pt.title(site + time.strftime(' %Y-%m-%d %H UTC') + "\n", loc = "left")
    plotwindline(Pt, var, yname="z")
    Pt.set_ylabel("height (m)")
    setting(Pt, xlim, ylim)
    return Pt

def uvplot_p(var, ylim = [1000, 600], xlim = [-5, 30], figsize = figsize):
    Pt = Plotter(figsize = figsize)#figsize = [6, 8])
    # Pt.title(site + time.strftime(' %Y-%m-%d %H UTC') + "\n", loc = "left")
    plotwindline(Pt, var, yname="p")
    Pt.ax.invert_yaxis()
    Pt.set_ylabel("pressure (hPa)")
    setting(Pt, xlim, ylim)
    
    return Pt

def plotwindline(Pt, var, yname, uvline = True, wsline = True):
    y = var[yname]
    u, v = wswd_to_uv(var['ws'], var['wd'])
    if uvline:
        Pt.ax.plot(u, y, "r", label = "u")
        Pt.ax.plot(v, y, "b", label = "v")
    if wsline:
        Pt.ax.plot(np.sqrt(u**2+v**2), y, "k", label = "ws")

def setting(Pt, xlim, ylim):
    Pt.set_ylim(ylim)
    Pt.set_xlim(xlim)
    Pt.ax.grid()
    Pt.set_xlabel("m/s")
    Pt.legend()
    Pt.fig.tight_layout()

