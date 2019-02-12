from lotto_modules import lotto_numbers
from datetime import date, timedelta
import time
import csv

if __name__ == '__main__':

    d1 = date(2008, 8, 25)
    d2 = date(2008, 9, 5)

    delta = d2 - d1

    with open('lotto.csv', 'w', newline='') as csvfile:
        lotto_writer = csv.writer(csvfile, delimiter='|')
        lotto_writer.writerow(['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'date'])

        for i in range(delta.days + 1):
            lotto_date = (d1 + timedelta(i)).strftime('%Y-%m-%d')
            lotto_row = lotto_numbers(lotto_date)
            if lotto_row is None:
                #respect robots.txt
                time.sleep(10)
            else:
                lotto_row.append(lotto_date)
                lotto_writer.writerow(lotto_row)
                #respect robots.txt
                time.sleep(10)

    csvfile.close()
