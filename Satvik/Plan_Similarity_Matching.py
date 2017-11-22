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
    print(disease is None)
    print(benefit is None)
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

    hard_df.columns = [description[0] for description in results.description]
    print(hard_df.columns)
    close_connection(conn, c)
    return hard_df


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


def hard_filters_pg2(db_loc, hard_df1, med_condition = None, benefit = None):
    if med_condition == None and benefit == None:
        return hard_df1
    conn, c = create_connection(db_loc)
    plan_id = hard_df1['plan_id'].tolist()
    if med_condition != None:
        results =0


def soft_filters(df, coin = None, ded_in = None, moop_in = None, ded_oon = None, moop_oon = None, international = None):
    filters = [coin, ded_in, moop_in, ded_oon, moop_oon, international]
    cols = ['']

    df['distance'] = df.apply(lambda x: euclidean(np.array([int(x['TEHBDedInnTier1Coinsurance_R']),
                                                            int(x['TEHBDedInnTier1Individual_R']),
                                                            int(x['TEHBInnTier1IndividualMOOP_R'])]),
                                                  np.array([coin, ded_in, moop_in])), axis=1)
    # df['distance'] = np.linalg.norm(df[['TEHBDedInnTier1Coinsurance_R', 'TEHBDedInnTier1Individual_R',
    #                                     'TEHBInnTier1IndividualMOOP_R']].sub(np.array(coin, ded, moop)), axis=1)
    print(df.sort('distance').head())


df = hard_filters_pg1("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db", zip=27606, age=26,
                      tobacco_usage='Yes', premium=400)
df2 = get_plan_names("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db", df)
df2
print(len(df))
soft_filters(df, 0, 1, 0)