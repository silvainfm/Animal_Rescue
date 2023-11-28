import pandas as pd
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client.rescue_portal
collection = db.pet_information

# CSV file path
csv_file = "/Users/hunterdawley/Documents/DSI_Fall_2023/NOSQL/finalproject/final_data.csv"

# Print the header of the CSV file
header = pd.read_csv(csv_file, sep='\t', nrows=0).columns.tolist()
print("CSV Header:", header)

# Read data from CSV file
df = pd.read_csv(csv_file, sep='\t')

# Replace NaN values with an empty string
df = df.fillna('')

# Convert DataFrame to a list of dictionaries
entries = df.to_dict(orient='records')

# Insert the data into the "pet_information" collection
collection.insert_many(entries)

print("Data successfully inserted into the rescue_portal database.")

