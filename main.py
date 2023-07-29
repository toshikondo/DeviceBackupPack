from CsvFolderToNornir_hostsYaml import Csv2NornirSimple
from pathlib import Path
from Backupconfig_nornir_netmiko import Backupconfig_nornir_netmiko
import os 
#from nornir import InitNornir
from datetime import date


# Reading all csv files in CSVfolder and making a list(csv_filepath_list) of path of the csv files.

p = Path('./CSVfolder')
csv_filepath_list = list(p.glob('*.csv'))
DATE_FOLDER = str(date.today())

for csv_filepath in  csv_filepath_list:
    
    #Picking up a csv filename without extension. => filename_no_extension
                                         
    filename = os.path.basename(csv_filepath)
    filename_no_extension = os.path.splitext(filename)[0]

     #Creating hosts.yaml from a CSV file with Csv2NornirSimple class.

    csv2n = Csv2NornirSimple(csv_filepath)
    csv2n.inventory_converter()
    csv2n.make_nornir_inventory()

    #Backuping configuration by each csv file.

    #nr = InitNornir(config_file=)
    backup = Backupconfig_nornir_netmiko(DATE_FOLDER, filename_no_extension, "config.yaml")
    backup.get_netmiko_backups()