import csv
import sys


# Reads the CSV File and returns a list which will be using to create the yaml file

class Csv2NornirSimple:

    def __init__(self, filepath):
        
        self.filepath = filepath
        self.inventory_data = []

    def inventory_converter(self):
        inventory_list = []
        # Currently not in use 
        core_field = ["name", "hostname", "platform", "port", "username", "password"]
        try:
            with open(self.filepath) as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    inventory_list.append([
                        row["name"],
                        row["hostname"],
                        row["platform"],
                        row["port"],
                        row["username"],
                        row["password"],
                        row["groups"]
                        ])
                self.inventory_data = inventory_list
                
        except FileNotFoundError:
            print("Please make sure that" + str(self.filepath) + "is correct and exists...")
            sys.exit(1)


    # Iterates over the list and creates the csv_inventory.yaml based on the Nornir model

    def make_nornir_inventory(self):
        if len(self.inventory_data) < 1:
            print("The list argument doesn't have any records! Cannot create an inventory file out of an empty list!")
            return ValueError
        try:
            
            with open("hosts.yaml", "w") as out_file:
                out_file.write("---\n")
                for host in self.inventory_data:
                    out_file.write(f"{host[0]}:\n")
                    out_file.write(f"  hostname: {host[1]}\n")
                    out_file.write(f"  platform: {host[2]}\n")
                    out_file.write(f"  port: {host[3]}\n")
                    out_file.write(f"  username: {host[4]}\n")
                    out_file.write(f"  password: {host[5]}\n")
                    if len(host[6].split("_")) > 0:
                        out_file.write(f"  groups:\n")
                        for group in host[6].split("__"):
                            out_file.write(f"    - {group}\n")
                    else:
                        out_file.write("\n")
                
                print("Converting " + str(self.filepath) + " to hosts.yaml...")
        except PermissionError:
            print("An error occurred whilst trying to write into the file... Please make sure that there are enough permission assigned to the user executing the script...")
            sys.exit(1)


def main():

    csv_inventory_file_path = "./CSVfolder/site0_inventory.csv"
    c2n = Csv2NornirSimple(csv_inventory_file_path)
    c2n.inventory_converter()
    c2n.make_nornir_inventory()


if __name__ == "__main__":
    main()
