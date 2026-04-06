import netCDF4 as nc
import numpy as np

path = r'C:\Users\Abajinn1\opm-data\norne\NORNE_PORTFOLIO.e'
ds = nc.Dataset(path)

actnum = np.array(ds.variables['vals_elem_var1eb1'][:]).astype(float).ravel()
poro = np.array(ds.variables['vals_elem_var2eb1'][:]).astype(float).ravel()
permx = np.array(ds.variables['vals_elem_var3eb1'][:]).astype(float).ravel()

active_mask = actnum > 0.5
poro_active = poro[active_mask]
permx_active = permx[active_mask]

print("Active cell count:", int(active_mask.sum()))
print()

print("poro summary")
print("min:", float(np.min(poro_active)))
print("max:", float(np.max(poro_active)))
print("mean:", float(np.mean(poro_active)))
print("median:", float(np.median(poro_active)))
print()

print("permx summary")
print("min:", float(np.min(permx_active)))
print("max:", float(np.max(permx_active)))
print("mean:", float(np.mean(permx_active)))
print("median:", float(np.median(permx_active)))
