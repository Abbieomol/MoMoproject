import xml.etree.ElementTree as ET
import json

def parse_sms(xml_file, json_file):
    # Load XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    transactions = []

    # Loop through every <sms> element
    for sms in root.findall("sms"):
        record = {
            "id": sms.get("id"),
            "address": sms.get("address"),
            "date": sms.get("date"),
            "body": sms.get("body")
        }
        transactions.append(record)

    # Save to JSON
    with open(json_file, "w") as f:
        json.dump(transactions, f, indent=2)

    print(f"Saved {len(transactions)} transactions to {json_file}")

if __name__ == "__main__":
    # Input XML file
    xml_path = "modified_sms_v2.xml"
    # Output JSON file with your preferred name
    json_path = "dashboard.json"
    parse_sms(xml_path, json_path)
