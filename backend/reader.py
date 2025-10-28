import os
import csv
from flask import Flask, jsonify
from flask_cors import CORS

input_folder = os.path.join("Data", "Files", "Input")

def read_invoices():
    invoices = []
    if not os.path.exists(input_folder):
        print("Input folder not found!")
        return invoices
    
    for file in os.listdir(input_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(input_folder, file)
            try:
                with open(file_path, "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        invoice = {
                            "Name": row.get("Name", ""),
                            "Vendor": row.get("Vendor", ""),
                            "Date": row.get("Date", ""),
                            "Amount": row.get("Amount", "")
                        }
                        invoices.append(invoice)
            except Exception as e:
                print(f"Error reading {file}: {e}")
    
    return invoices

app = Flask(__name__)
CORS(app)

@app.route("/invoices", methods=["GET"])
def get_invoices():
    data = read_invoices()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
