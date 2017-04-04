import numpy as np

Weeks = 104
week_array = np.arange(Weeks)

m_array = np.ones((Weeks,), dtype=np.int)
t_array = np.full_like(m_array, 2, dtype=np.int)
w_array = np.full_like(m_array, 3, dtype=np.int)
r_array = np.full_like(m_array, 4, dtype=np.int)
f_array = np.full_like(m_array, 5, dtype=np.int)


mwf_morning = [800, 815,830,845,900,915,930,945,1000]
tr_morning = [1200, 1215,1230,1245,1300,1315,1330,1345,1400]

mw_night = [1600, 1615, 1630, 1645, 1700, 1715, 1730, 1745, 1800]
f_night = [1500, 1515,1530,1545,1600,1615,1630,1645,1700]
tr_night = [2000, 2015,2030,2045,2100,2115,2130,2145,2100]

mon_morning = np.random.choice(mwf_morning, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
wed_morning = np.random.choice(mwf_morning, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
fri_morning = np.random.choice(mwf_morning, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
tue_morning = np.random.choice(tr_morning, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
thu_morning = np.random.choice(tr_morning, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])

mon_night = np.random.choice(mw_night, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
wed_night = np.random.choice(mw_night, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
fri_night = np.random.choice(f_night, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
tue_night = np.random.choice(tr_night, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])
thu_night = np.random.choice(tr_night, Weeks, p=[0.05,0.05,0.1,0.1,0.4,0.1,0.1,0.05,0.05])

mm_temp = np.array((week_array, m_array, mon_morning)).T
mn_temp = np.array((week_array, m_array, mon_night)).T

print mm_temp

mon_final = np.vstack((mm_temp, mn_temp))
print mon_final
