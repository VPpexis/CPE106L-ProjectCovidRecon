import pandas as pd
import mysql.connector

#Should be run on a AWS EC2 Instance.
#Link of DOH Covid-19 Data: https://drive.google.com/drive/folders/1w_O-vweBFbqCgzgmCpux2F0HVB4P6ni2
#Need to be a streamlistener using GDrive API to automatically get data in GDrive.
def ncrdb(databaseloc):
    df = pd.read_csv(databaseloc, encoding = "ISO-8859-1")
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


    sql = 'INSERT IGNORE INTO casesByNCR(case_code, age, age_group, sex, date_rep_conf, removal_type, admitted, city_mun_res, health_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
    cases_NCR = cases_NCR.values.tolist()
    mycursor.executemany(sql, cases_NCR)

    mydb.commit()

def ph_DB(databaseloc):
    df = pd.read_csv(databaseloc, encoding = "ISO-8859-1")

    cases_ph = df.fillna('')

    print(cases_ph)

    mydb = mysql.connector.connect(
        host = 'myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com',
        user = 'myrds',
        passwd = 'admin123',
        database = 'myrds1'
    )

    mycursor = mydb.cursor()


    sql = 'INSERT IGNORE INTO casesByPH(case_code, age, age_group, sex, date_rep_conf, removal_type, admitted, region_res, city_mun_res, health_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
    cases_ph = cases_ph.values.tolist()
    print(cases_ph)
    mycursor.executemany(sql, cases_ph)

    mydb.commit()
    mydb.close()

ph_DB('DB/DOH Data Drop 20200430.csv')
ncrdb('DB/DOH Data Drop 20200430.csv')




