from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import re
import json

#define our congos search settings
service_name = 'gptmodel'
index_name = 'mydata-index'
admin_key = 'FSjMkmcS5rkzUSjWMSnCVG2gODa9Pf4zrVBhBgTgHqAzSeBI3QID'
endpoint = f"https://{service_name}.search.windows.net/"
credential = AzureKeyCredential(admin_key)

file_path = "C:\\Users\\Apoorv\\OneDrive\\Desktop\\ict\\data\\ticket_data.csv"
df = pd.read_csv(file_path)

search_client = SearchClient(endpoint=endpoint, index_name = index_name, credential= credential)

data = []

for _, row in df.iterrows():
    data.append({
        "@search.action":"upload",
        "TicketID": str(row["Ticket ID"]),
        "TicketType" : row["Ticket Type"],
        "TicketSubject":row["Ticket Subject"],
        "TicketDescription":row["Ticket Description"],
        "TicketStatus":row["Ticket Status"],
        "TicketPriority":row["Ticket Priority"],
        "TicketChannel":row["Ticket Channel"]
    })

result = search_client.upload_documents(data)
print("upload result: ", result)