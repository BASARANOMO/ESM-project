def growth_rate_TP(concentration_total_p, k_p, niu_max):
    return niu_max * concentration_total_p / (concentration_total_p + k_p)