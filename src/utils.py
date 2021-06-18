import numpy as np

def chlorine_decay_time_given(c_init, k, t):
    c_out = c_init * np.exp(-k * t)
    return c_out


def chlorine_decay_in_tube(c_init, k, u):
    c_out = c_init * np.exp(-k * 2000 / u)
    return c_out

def chlorine_decay_in_lake(c_init_lake, c_wastewater, c_from_runoff, volume_lake, volume_wastewater_production, volume_from_runoff, k, t_max): # time series
    c_out = np.zeros(t_max)
    sigma_temp = c_wastewater * volume_wastewater_production + c_from_runoff * volume_from_runoff
    for t in range(1, t_max + 1):
        c_out[t - 1] = (sigma_temp / volume_lake - (sigma_temp / volume_lake - k * c_init_lake) * np.exp(-k * t)) / k
    return c_out


def residual_chlorine_in_lake(c_init_lake, c1, c2, cr, k1, k2, kt, kr, kl, tau1, tau2, taur, t_max, volume_lake, volume_wastewater_production, volume_from_runoff, WWTP_proportion = 0.8, u = 0.45 * 3600):
    c3 = chlorine_decay_time_given(c1 * WWTP_proportion + c2, k1, tau1)
    c_into_lake_1 = chlorine_decay_in_tube(c3, kt, u)
    c_into_lake_2 = chlorine_decay_time_given(c1 * (1 - WWTP_proportion), k2, tau2)
    c_into_lake_3 = chlorine_decay_time_given(cr, kr, taur)
    c_wastewater = c_into_lake_1 * WWTP_proportion + c_into_lake_2 * (1 - WWTP_proportion)
    c_in_lake_residual = chlorine_decay_in_lake(c_init_lake, c_wastewater, c_into_lake_3, volume_lake, volume_wastewater_production, volume_from_runoff, kl, t_max)
    return c_in_lake_residual, c_into_lake_1, c_into_lake_2, c_into_lake_3, c_wastewater, c3    

