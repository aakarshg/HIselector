import sqlite3
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean
import uszipcode

# -------------------- User Preferences
# State - NC
# Zipcode - 27606
# Age - 26
# Tobacco Usage - No
# Disease Management - Diabetes
# Coinsurance - 20% (0)
# Deductible IN - 200 (1)
# MOOP IN - 100 (0)


def create_connection(db_loc):
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()
    return conn, c


def close_connection(conn, c):
    c.close()
    conn.close()


def hard_filters_pg1(db_loc, zip=None, age=None, tobacco_usage=None, disease=None, benefit=None, premium=None):
    if zip is None or str(zip).strip() == "" or age is None or str(age).strip() == "" or tobacco_usage is None:
        return "Enter all inputs"

    search = uszipcode.ZipcodeSearchEngine()
    state = None
    if str(zip).strip() != "":
        if search.by_zipcode(str(zip)):
            state = search.by_zipcode(str(zip))['State']
        else:
            return "Invalid zipcode"
    conn, c = create_connection(db_loc)
    hard_df = pd.DataFrame()
    if disease is not None and benefit is not None:
        print("Disease/Benefit not null")
        if tobacco_usage == "No":
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and indiv_rate <= 1.2 * ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where p.diseasemanagementprogramsoffered like ? and b.benefit_name = ?",
                                (state, age, age, premium, "%"+disease+"%", benefit))
        else:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and smoker_rate <= 1.2 * ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where p.diseasemanagementprogramsoffered like ? and b.benefit_name = ?",
                                (state, age, age, premium, "%"+disease+"%", benefit))
        hard_df = pd.DataFrame(results.fetchall())
        if hard_df.empty:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where p.diseasemanagementprogramsoffered like ? and b.benefit_name = ?",
                                (state, age, age, "%" + disease + "%", benefit))
            hard_df = pd.DataFrame(results.fetchall())
    if disease is None and benefit is not None and hard_df.empty:
        print("Disease null/Benefit not null")
        if tobacco_usage == "No":
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and indiv_rate <= 1.2 * ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where b.benefit_name = ?",
                                (state, age, age, premium, benefit))
        else:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and smoker_rate <= 1.2 * ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where b.benefit_name = ?",
                                (state, age, age, premium, benefit))
        hard_df = pd.DataFrame(results.fetchall())
        if hard_df.empty:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ?) c, benefits b "
                                "on substr(p.planid, 1, 14) = c.plan_id and p.planid = b.plan_id "
                                "where b.benefit_name = ?",
                                (state, age, age, benefit))
            hard_df = pd.DataFrame(results.fetchall())
    if benefit is None and disease is not None and hard_df.empty:
        print("Disease not null/Benefit null")
        if tobacco_usage == "No":
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and indiv_rate <= 1.2 * ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id "
                                "where p.diseasemanagementprogramsoffered like ?",
                                (state, age, age, premium, "%" + disease + "%"))
        else:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and smoker_rate <= 1.2 * ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id "
                                "where p.diseasemanagementprogramsoffered like ?",
                                (state, age, age, premium, "%" + disease + "%"))
        hard_df = pd.DataFrame(results.fetchall())
        if hard_df.empty:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id "
                                "where p.diseasemanagementprogramsoffered like ?",
                                (state, age, age, "%" + disease + "%"))
            hard_df = pd.DataFrame(results.fetchall())
    if disease is None and benefit is None or hard_df.empty:
        print("Disease/Benefit null")
        if tobacco_usage == "No":
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and indiv_rate <= 1.2 * ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id",
                                (state, age, age, premium))
        else:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ? and smoker_rate <= 1.2 * ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id",
                                (state, age, age, premium))
        hard_df = pd.DataFrame(results.fetchall())
        if hard_df.empty:
            results = c.execute("select p.planid from plan_attributes p,"
                                "(select * from cost where state = ? and age_lower <= ? and "
                                "age_higher >= ?) c "
                                "on substr(p.planid, 1, 14) = c.plan_id",
                                (state, age, age))
            hard_df = pd.DataFrame(results.fetchall())
    if hard_df.empty:
        return "No results to show for your area"
    hard_df.columns = [description[0] for description in results.description]
    close_connection(conn, c)
    return hard_df


def soft_filters(df, db_loc, age, smoking='No', benefit='Emergency Room Services',
                 prem=0, coin_in=0, copay_in=0, ded_in=0, moop_in=0, visit=0.5, oo_cntry=0.5):
    conn, c = create_connection(db_loc)
    planid = df['p.planid'].tolist()
    if smoking == 'No':
        rate_norm_col = "c.rate_norm"
        rate_col = "c.indiv_rate"
    else:
        rate_norm_col = "c.smoker_norm"
        rate_col = "c.smoker_rate"
    query = "select distinct p.planId, p.PlanMarketingName, p.CountryCoverage, p.MOOP, p.DedInn, i.Issuer_Name, b.copayin_norm, b.coinsin_norm, " \
            + rate_norm_col + " as premium_norm, " + rate_col + " as premium, v.visits_norm " \
            "from Plan_Attributes p, benefits b, visits v, cost c, IssuerID_Name_Mapping i " \
            "on p.PlanId = b.plan_id and p.IssuerId = v.issuer_id " \
            "and substr(p.planid, 1, 14) = c.plan_id and p.IssuerId = i.IssuerId " \
            "where p.planId in ('" + '\',\''.join(planid) + "') " \
            "and b.benefit_name = '" + str(benefit) + \
            "' and c.age_lower<=" + str(age) + " and c.age_higher>=" + str(age)
    results = c.execute(query)
    soft_df = pd.DataFrame(results.fetchall())
    soft_df.columns = [description[0] for description in results.description]
    # df['distance'] = soft_df.apply(lambda x: euclidean(np.array([float(x['CountryCoverage']),
    #                                                         float(x['MOOP']),
    #                                                         float(x['DedInn']),
    #                                                         float(x['copayin_norm']),
    #                                                         float(x['coinsin_norm']),
    #                                                         float(x['premium']),
    #                                                         float(x['visits_norm'])]),
    #                                               np.array([oo_cntry, moop_in, ded_in, copay_in,
    #                                                         coin_in, prem, visit])),
    #                           axis=1)

    df['distance'] = soft_df.apply(lambda x: sum(np.array([float(x['MOOP']), float(x['DedInn']),
                                                  float(x['copayin_norm']), float(x['coinsin_norm']),
                                                  float(x['premium_norm'])]) -
                                                 np.array([moop_in, ded_in, copay_in, coin_in, prem]),
                                                 ((float(x['CountryCoverage']) - oo_cntry)**2 +
                                                 (float(x['visits_norm']) - visit) ** 2)**0.5),
                                   axis=1)
    df['price'] = soft_df['premium']
    df['Plan_name'] = soft_df['PlanMarketingName']
    df['Issuer_name'] = soft_df['Issuer_Name']
    close_connection(conn, c)
    return df.sort(['distance', 'price'], ascending=[True, True]).head()


def get_plan_names(db_loc, hard_df1):
    conn, c = create_connection(db_loc)
    res = list(set(hard_df1['plan_id'].apply(lambda x: x[0:5])))
    query = "SELECT Issuer_name FROM IssuerID_Name_Mapping where IssuerID IN (" + ','.join(res) + ")"
    results = c.execute(query)
    l = results.fetchall()
    print([c[0] for c in l])
    # names = pd.DataFrame(results.fetchall())
    # names.columns = [description[0] for description in results.description]
    # close_connection(conn, c)
    # return names

df = hard_filters_pg1("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db", zip=32003, age=26,
                      tobacco_usage='No', benefit='Transplant', premium=2000)
final_df = soft_filters(df, "C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db", age=26,
                        prem=0, moop_in=0.3, oo_cntry=1, ded_in=0.3, visit=0.8, coin_in=0.2)
plan_details = get_plan_names(final_df, "C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db")

print(len(df))
soft_filters(df, 0, 1, 0)