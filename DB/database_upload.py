import pandas as pd
import mysql.connector

#Should be run on a server
def ncrdb():
    df = pd.read_csv('DB/COVID-19 Data 20204030.csv', encoding = "ISO-8859-1")
    is_NCR = df['RegionRes']=='NCR'

    cases_NCR = df[is_NCR]

    cases_NCR = cases_NCR.drop('RegionRes', 1)
    cases_NCR = cases_NCR.fillna('')


    #print(cases_NCR)

    mydb = mysql.connector.connect(
        host = 'myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com',
        user = 'myrds',
        passwd = 'admin123',
        database = 'myrds1'
    )

    mycursor = mydb.cursor()


    sql = 'INSERT INTO casesByNCR(case_code, age, age_group, sex, date_rep_conf, removal_type, admitted, city_mun_res, health_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
    cases_NCR = cases_NCR.values.tolist()
    mycursor.executemany(sql, cases_NCR)

    mydb.commit()

def ph_DB():
    df = pd.read_csv('DB/COVID-19 Data 20204030.csv', encoding = "ISO-8859-1")

    cases_ph = df.fillna('')

    #print(cases_NCR)

    mydb = mysql.connector.connect(
        host = 'myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com',
        user = 'myrds',
        passwd = 'admin123',
        database = 'myrds1'
    )

    mycursor = mydb.cursor()


    sql = 'INSERT INTO casesByPH(case_code, age, age_group, sex, date_rep_conf, removal_type, admitted, region_res, city_mun_res, health_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    cases_ph = cases_ph.values.tolist()
    mycursor.executemany(sql, cases_ph)

    mydb.commit()

ph_DB()




