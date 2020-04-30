import mysql.connector
import datetime

'''
This is a subtractor function that subracts a specific date to the current date and gets the total cases during
the subtracted date'
'''
class getpastdate():
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'myrds1.cijcu6ghykxh.ap-southeast-1.rds.amazonaws.com',
            user = 'myrds',
            passwd = 'admin123',
            database = 'myrds1'
            )

    #Parameter days is for how many days to subract
    def get_past(self, days = 0):
        try:
            mycursor = self.conn.cursor()
            self.days = int(days)
            self.days = str(self.days)

            mycursor.execute('SELECT DATE_FORMAT(DATE_SUB(max(date_rep_conf), INTERVAL '+ self.days +' DAY), \'%Y-%m-%d\') FROM casesByPH;')
            result1 = mycursor.fetchall()
            result1 = result1[0]
            resutl1 = result1[0]
            result1 = result1[0]
            print('Subtracted Date: '+result1)

            mycursor.execute('SELECT date_rep_conf, COUNT(date_rep_conf) FROM casesByPH WHERE date_rep_conf between \'2020-03-06\' and \'' + result1 + '\' GROUP BY date_rep_conf HAVING COUNT(city_mun_res) > 1;')
            myresults = mycursor.fetchall()

            final_results = 0

            for x in myresults:
                final_results += x[1]

            return final_results

        except ValueError:
            print('Not a number!')
            return

if __name__ == '__main__':
    gpd = getpastdate()
    print(gpd.get_past(52))