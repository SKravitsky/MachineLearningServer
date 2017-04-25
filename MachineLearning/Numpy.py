import numpy as np

def make_csv():
    Weeks = 104
    week_array = np.arange(Weeks)

    m_array = np.ones((Weeks,), dtype=np.int)
    t_array = np.full_like(m_array, 2, dtype=np.int)
    w_array = np.full_like(m_array, 3, dtype=np.int)
    r_array = np.full_like(m_array, 4, dtype=np.int)
    f_array = np.full_like(m_array, 5, dtype=np.int)

    thirty_array = np.full_like(m_array, 77, dtype=np.int)
    fifteen_array = np.full_like(m_array, 176, dtype=np.int)
    spring_array = np.full_like(m_array, 206, dtype=np.int)

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


    mm_feature = np.array((week_array, m_array, mon_morning, thirty_array)).T
    mm_target = np.vstack(fifteen_array)

    mn_feature = np.array((week_array, m_array, mon_night, fifteen_array)).T
    mn_target = np.vstack(thirty_array)

    mon_feature_final = np.vstack((mm_feature, mn_feature))
    mon_target_final = np.vstack((mm_target, mn_target))


    tm_feature = np.array((week_array, t_array, tue_morning, thirty_array)).T
    tm_target = np.vstack(spring_array)

    tn_feature = np.array((week_array, t_array, tue_night, spring_array)).T
    tn_target = np.vstack(thirty_array)

    tue_feature_final = np.vstack((tm_feature, tn_feature))
    tue_target_final = np.vstack((tm_target, tn_target))


    wm_feature = np.array((week_array, w_array, wed_morning, thirty_array)).T
    wm_target = np.vstack(fifteen_array)

    wn_feature = np.array((week_array, w_array, wed_night, fifteen_array)).T
    wn_target = np.vstack(thirty_array)

    wed_feature_final = np.vstack((wm_feature, wn_feature))
    wed_target_final = np.vstack((wm_target, wn_target))


    rm_feature = np.array((week_array, r_array, thu_morning, thirty_array)).T
    rm_target = np.vstack(spring_array)

    rn_feature = np.array((week_array, r_array, thu_night, spring_array)).T
    rn_target = np.vstack(thirty_array)

    thu_feature_final = np.vstack((rm_feature, rn_feature))
    thu_target_final = np.vstack((rm_target, rn_target))


    fm_feature = np.array((week_array, f_array, fri_morning, thirty_array)).T
    fm_target = np.vstack(fifteen_array)

    fn_feature = np.array((week_array, f_array, fri_night, fifteen_array)).T
    fn_target = np.vstack(thirty_array)

    fri_feature_final = np.vstack((fm_feature, fn_feature))
    fri_target_final = np.vstack((fm_target, fn_target))


    mt_feature = np.vstack((mon_feature_final, tue_feature_final))
    mt_target = np.vstack((mon_target_final, tue_target_final))

    tw_feature = np.vstack((mt_feature, wed_feature_final))
    tw_target = np.vstack((mt_target, wed_target_final))

    wr_feature = np.vstack((tw_feature, thu_feature_final))
    wr_target = np.vstack((tw_target, thu_target_final))

    final_feature = np.vstack((wr_feature, fri_feature_final))
    final_target = np.vstack((wr_target, fri_target_final))

    np.savetxt("feature.csv", final_feature, delimiter=",", fmt='%i')
    np.savetxt("target.csv", final_target, delimiter=",", fmt='%i')


if __name__ == "__main__":
    make_csv()
    print 'hello'
