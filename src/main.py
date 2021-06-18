import numpy as np
import matplotlib.pyplot as plt
from utils import residual_chlorine_in_lake

# Chlorine
c1 = 2  # 城市污水浓度，mg/L
c2 = 0  # 消毒池投放
cr = 1  # runoff
c_init_lake = 0.08

# Chlorine decay params
k1 = 0.05  # WWTP氯衰减系数，1/h
k2 = 0.05  # 直排
kr = 0.05  # runoff
kt = 0.05  # 排水管道
kl = 0.01  # 湖泊

tau1 = 0.6 # WWTP停留时间，h
tau2 = 0 # 自然水体停留时间
taur = 0 # 雨水管网停留时间
t_max = 120

# city params
pop = 100000

# lake params
volume_lake = 10000000 # m3
volume_wastewater_production = 3.56 # m3 per day per person
volume_from_runoff = 0

c_in_lake_residual, c_into_lake_1, c_into_lake_2, c_into_lake_3, c_wastewater, c3 = \
residual_chlorine_in_lake(c_init_lake, c1, c2, cr, 
                          k1, k2, kt, kr, kl * 24,
                          tau1, tau2, taur, t_max, 
                          volume_lake = volume_lake, 
                          volume_wastewater_production = volume_wastewater_production * pop, 
                          volume_from_runoff = volume_from_runoff, 
                          WWTP_proportion = 0.8, u = 0.45 * 3600)
plt.figure(figsize=(10, 5))
x = [i for i in range(1, 121)]
print("c_into_lake_1: %f" % c_into_lake_1)
print("c_into_lake_2: %f" % c_into_lake_2)
print("c_into_lake_3: %f" % c_into_lake_3)
print("c_wastewater: %f" % c_wastewater)
print("c3: %f" % c3)
plt.plot(x, c_in_lake_residual, label="c_in_lake_residual")
# plt.plot(x, c_into_lake_1, abel="c_into_lake_1")
# plt.plot(x, c_into_lake_2, label="c_into_lake_2")
# plt.plot(x, c_into_lake_3, label="c_into_lake_3")
# plt.plot(x, c_wastewater, label="c_wastewater")
# plt.plot(x, c3, label="c3")
plt.legend()
plt.show()