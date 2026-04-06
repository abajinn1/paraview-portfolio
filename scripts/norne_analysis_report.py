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

poro_min = float(np.min(poro_active))
poro_max = float(np.max(poro_active))
poro_mean = float(np.mean(poro_active))
poro_median = float(np.median(poro_active))

permx_min = float(np.min(permx_active))
permx_max = float(np.max(permx_active))
permx_mean = float(np.mean(permx_active))
permx_median = float(np.median(permx_active))

print("NORNE PORTFOLIO MODEL | CONSOLE-ASSISTED ANALYSIS")
print("=" * 55)
print(f"Active cell count: {int(active_mask.sum()):,}")
print()

print("Porosity (poro)")
print(f"  Min:    {poro_min:.4f}")
print(f"  Max:    {poro_max:.4f}")
print(f"  Mean:   {poro_mean:.4f}")
print(f"  Median: {poro_median:.4f}")
print("  Interpretation: porosity is comparatively balanced and visually readable across the active model.")
print()

print("Permeability X (permx)")
print(f"  Min:    {permx_min:.4f}")
print(f"  Max:    {permx_max:.4f}")
print(f"  Mean:   {permx_mean:.4f}")
print(f"  Median: {permx_median:.4f}")
print("  Interpretation: permeability spans a much wider and more skewed range, making it a stronger technical comparison view.")
