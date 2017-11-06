import sqlite3
import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean

# -------------------- User Preferences
# State - NC
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

def hard_filters(db_loc, state, disease):
    conn, c = create_connection(db_loc)
    print(("%" + disease + "%").title())
    results = c.execute("SELECT * FROM PLAN_ATTRIBUTES where STATECODE = ? AND DISEASEMANAGEMENTPROGRAMSOFFERED LIKE ?",
                        (state, "%" + disease + "%"))
    if not results:
        print("No plans are available in your area covering your condition. Checking for closest match..")
        results = c.execute("SELECT * FROM PLAN_ATTRIBUTES where STATECODE = ?" , (state,))

    df = pd.DataFrame(results.fetchall())
    print(results.description)
    df.columns = [description[0] for description in results.description]
    close_connection(conn, c)
    return df


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


df = hard_filters("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db", "NC", "DIAbetes")
print(len(df))
soft_filters(df, 0, 1, 0)