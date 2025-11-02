import urllib.request
import csv

urllib.request.urlretrieve('https://data.geo.admin.ch/ch.meteoschweiz.messwerte-niederschlag-1d/ch.meteoschweiz.messwerte-niederschlag-1d_de.csv', '/tmp/meteoswiss.csv')

with open('/tmp/meteoswiss.csv', encoding='ISO-8859-1') as csvfile:
 reader = csv.reader(csvfile, delimiter=';')
 for row in reader:
  for field in row:
   if field in ('SMA', 'REH', 'KLO'):
    f = open("/root/meteoschweiz_niederschlag_sma.txt", "a")
    f.write(row[1] + ';' + row[4] + ';' + row[3] + "\n")
    f.close()
exit()
