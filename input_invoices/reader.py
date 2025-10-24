import os
import csv

# Folder where all invoices are kept
input_folder = "input_invoices"

def read_invoices(folder_path):
    print(f"Reading all invoices from folder: {folder_path}")
    print("=" * 50)

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            print(f"\nNow reading file: {file}")
            print("-" * 40)

            with open(file_path, "r", encoding="utf-8") as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    name = row.get("Name", "")
                    vendor = row.get("Vendor", "")
                    date = row.get("Date", "")
                    amount = row.get("Amount", "")
                    print(f"Name: {name}")
                    print(f"Vendor: {vendor}")
                    print(f"Date: {date}")
                    print(f"Amount: ₹{amount}")
                    print("-" * 40)

# call the function
read_invoices(input_folder)

