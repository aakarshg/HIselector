import sqlite3
import csv

def create_db(db_loc, file_loc, tablename):
    conn = sqlite3.connect(db_loc)
    c = conn.cursor()

    with open(file_loc , "r") as f:
        reader = csv.reader(f)

        header = True
        for row in reader:
            if header:
                header = False

                sql = "DROP TABLE IF EXISTS %s" % tablename
                c.execute(sql)
                sql = "CREATE TABLE %s (%s)" % (tablename, ", ".join(["%s text" % column for column in row]))
                c.execute(sql)

                for column in row:
                    if column.lower().endswith("_id"):
                        index = "%s__%s" % (tablename, column)
                        sql = "CREATE INDEX %s on %s (%s)" % (index, tablename, column)
                        c.execute(sql)

                insertsql = "INSERT INTO %s VALUES (%s)" % (tablename, ", ".join(["?" for column in row]))

                rowlen = len(row)
            else:
                # skip lines that don't have the right number of columns
                if len(row) == rowlen:
                    c.execute(insertsql, row)

        conn.commit()
    c.close()
    conn.close()


# Table for Plan Attributes
# create_db("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db",
#           "C:\\Users\\satvi\\Documents\\DDDM\\Project\\Plan_Attributes_PP2.csv",
#           "Plan_Attributes")

# Table for Issuer ID Mapping
# create_db("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db",
#           "C:\\Users\\satvi\\Documents\\DDDM\\Project\\IssuerID_Name_Updated.csv",
#           "IssuerID_Name_Mapping")

# Table for Ratings
# create_db("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db",
#           "C:\\Users\\satvi\\Documents\\DDDM\\Project\\Quality_Ratings_PP1.csv",
#           "Ratings")

# Table for Reviews
# create_db("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db",
#           "C:\\Users\\satvi\\Documents\\DDDM\\Project\\Review_Table.csv",
#           "Reviews")

# Table for BBB Ratings
create_db("C:\\Users\\satvi\\Documents\\GitHub\\HIselector\\preprocessing\\sample.db",
          "C:\\Users\\satvi\\Documents\\DDDM\\Project\\BBBRatings.csv",
          "BBBRatings")