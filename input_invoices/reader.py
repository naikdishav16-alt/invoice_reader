import os
import csv

input_folder = "input_invoices"

def read_invoices(folder_path):
    print("Reading invoices...\n")  # small touch of personality
    
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            
            with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(f"{row['Name']} - {row['Vendor']} ({row['Date']}): ₹{row['Amount']}")
            print("-" * 40)  # small separator for clarity

read_invoices(input_folder)

