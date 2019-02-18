from lotto_modules import lotto_numbers, print_load_bar
from datetime import date, timedelta, datetime
import time
import csv
import re

def scrap_lotto(startdate, enddate, filename):
    d1 = datetime.strptime(startdate, '%Y%m%d')
    d2 = datetime.strptime(enddate, '%Y%m%d')
    delta = d2 - d1

    with open(filename + '.csv', 'w', newline='') as csvfile:
        lotto_writer = csv.writer(csvfile, delimiter='|')
        lotto_writer.writerow(['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'date'])

        for i in range(delta.days + 1):
            lotto_date = (d1 + timedelta(i)).strftime('%Y-%m-%d')
            lotto_row = lotto_numbers(lotto_date)
            print_load_bar(i, delta.days, prefix = 'Progress: ', suffix = 'Complete')
            if lotto_row is None:
                #respect robots.txt
                time.sleep(10)
            else:
                lotto_row.append(lotto_date)
                lotto_writer.writerow(lotto_row)
                #respect robots.txt
                time.sleep(10)
    print("Results saved!")
    csvfile.close()

if __name__ == '__main__':

   print("Welcome to lottery scraper!")
   
   while True:
       startdate = input("Please provide a start date (YYYYMMDD): ")
       if re.compile('(19|[2-9][0-9])\d{2}([0|1])\d([0-3])\d').match(startdate):
            break
   
   while True:
       enddate = input("Please provide a end date (YYYYMMDD): ")
       if re.compile('(19|[2-9][0-9])\d{2}([0|1])\d([0-3])\d').match(enddate):
            break
   
   filename = input("Please provide a result file name: ")
   
   scrap_lotto(startdate, enddate, filename)
   
   
    
