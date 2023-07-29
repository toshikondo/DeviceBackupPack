# DeviceBackupPack
__DeviceBackupPack can backup running-configration of Cisco(IOS/IOS-XE), Nexus(NX-OS) and FortiGate.__

## ファイルの説明

## How to use
1. Download file  
   >git clone https://github.com/toshikondo/DeviceBackupPack.git

2. Install necessary packages
   >pip3 install nornir  
   >pip3 install nornir-netmiko

3. Move to DeviceBackupPack directory  
   >cd DeviceBackupPack

4. Create csv files for inventory under CSVfolder directory    
    
    - Move to CSVfolder  
    >cd CSVfolder  

    - Create csv file for inventory   
      You can create csv files as many as you want(ex:sample1.csv and sample2.csv).  
      hosts.yaml will be created based on csv files.  

      __Stracture of the csv files__  
      This csv file includes information to access devices.  
      
      example:
      | name | hostname | platform | port | username | password | groups |
      | --- | --- | --- | --- | --- | --- | --- |
      | R1 | 192.168.1.150 | cisco_ios | 22 | username_A | password_A | cisco_group |
      | NX1 | 192.168.1.171 | cisco_nxos | 22 | username_B | password_B | nx_group |
      | FortiFW1 | 192.168.1.41 | fortinet | 22 | username_C | username_C | forti_group |
      | R2 | 192.168.1.151 | cisco_ios | 22 | username_D | password_D | cisco_group |

      __*name*__: Device name  
      __*hostname*__: Device IP address 
                      or actual device hostname (If DNS can resolve the hostname to an IP address)  
      __*platform*__: Device platform (cisco_ios, cisco_nxos, fortinet)  
      __*port*__: Access port number. It is usually 22(ssh)  
      __*username*__ Username to login a device with ssh  
      __*password*__: Password to login a device with ssh  
      __*groups*__: Device group (cisco_group, nx_group, forti_group)  

5. Run main.py to back up running config of the devices

    - Move to DeviceBackupPack  
    > cd ..

    -run main.py
    >python3 main.py

6. Check config-archive  
   - A date folder is created.  
   - The date folder has folders based on the csv files you created and logs.
   - The folder has running configurations of each devices.

