from nornir import InitNornir
from nornir.core.filter import F
from nornir_netmiko.tasks import netmiko_send_command
import pathlib
from datetime import date
import os


class Backupconfig_nornir_netmiko:
    
    config_dir = "config-archive"
    #config_date_dir = "config-archive" + '/' + str(date.today())

    def __init__(self, date_dir, site_name, config_yaml):
        
        
        self.date_dir = date_dir
        self.site_name = site_name
        self.config_date_dir = Backupconfig_nornir_netmiko.config_dir + '/' + self.date_dir
        self.config_date_site_dir = Backupconfig_nornir_netmiko.config_dir + '/' + self.date_dir + '/' + self.site_name + '/'
        
        pathlib.Path(Backupconfig_nornir_netmiko.config_dir).mkdir(exist_ok=True)
        pathlib.Path(self.config_date_dir).mkdir(exist_ok=True)
        pathlib.Path(self.config_date_site_dir).mkdir(exist_ok=True)
        
        self.devices = InitNornir(config_file=config_yaml, logging={"log_file": self.config_date_dir + "/" +"nornir.log", "level": "DEBUG"})
        self.ios_nxos_device = self.devices.filter(F(platform = 'cisco_ios') | F(platform = 'cisco_nxos'))
        self.forti_device = self.devices.filter(F(platform = 'fortinet'))
        

        
    def save_config_to_file(self, method, hostname, config):
        filename =  f"{hostname}.cfg"
        with open(os.path.join(self.config_date_site_dir, filename), "w") as f:
            f.write(config)

    def get_netmiko_backups(self):

        ios_nxos_backup_results = self.ios_nxos_device.run(
            task=netmiko_send_command, 
            command_string="show run"
            )
        
        for hostname in ios_nxos_backup_results:
            if ios_nxos_backup_results[hostname][0].failed == True:
                continue
            else:
                
                self.save_config_to_file(
                    method="netmiko",
                    hostname=hostname,
                    config=ios_nxos_backup_results[hostname][0].result,
                )
            
        forti_backup_results = self.forti_device.run(
            task=netmiko_send_command, 
            command_string="show"
            )

        for hostname in forti_backup_results:
            if forti_backup_results[hostname][0].failed == True:
                continue
            else:
                self.save_config_to_file(
                    method="netmiko",
                    hostname=hostname,
                    config=forti_backup_results[hostname][0].result,
                )

def main():
    nr = InitNornir(config_file="config.yaml")
    DATE_FOLDER = str(date.today())
    backup = Backupconfig_nornir_netmiko(DATE_FOLDER, 'Asite', "config.yaml")
    backup.get_netmiko_backups()


if __name__ == "__main__":
    main()