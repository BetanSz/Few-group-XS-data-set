from __future__ import division # you should use this
from IPython import embed # this can be very usefull try embed()
import pickle # cPickle could be considered
# import numpy as np # you should defenetly use this
# from collections import OrderedDict # this may be nice, but you shouldn't trust it so much, a dict is a dict
# import pandas as df # you can use this if you feel fancy

# to run me! python xsdata_ready.py
folder='/data/tmplca/eszames/xs_analysis/Bench_PWR_UO2_HFP/std_xs_data2/D3/'
name="XY_alld3.pkle" # name of the file
pickle_in = open(folder+name,"rb")
print 'loading...'
loaded_object = pickle.load(pickle_in)
X=loaded_object['x'] # X coordinate of data points, i.e. X={(x_1,x_2,x_3)_1,(x_1,x_2,x_3)_2,...,(x_1,x_2,x_3)_N} being N=len(X)
Y=loaded_object['y'] # Cross section (called "xs") data dict of dicts in the form xs=Y[isotope][reaction][group] being N_isotopes=len(Y)=30, N_reaction=len(Y.values()[0])=3 or 4, N_group=1-2
x_label=loaded_object['labels'] #Name of X variables
N_dim=len(x_label) # number of dimensions, here 3


## You can start by analyzing some parts of the domain, for example:
embed()
import matplotlib.pyplot as plt # never imports in the middle of the file
x_1,x_2,x_3=zip(*X) # very pythonic this line
lim_m=0
lim_M=70
plt.plot(x_1[lim_m:lim_M],Y['U235nufi2'][lim_m:lim_M])
plt.show()

