import pandas as pd
import re
import json
import requests

# Function to split to small subset the list of reasons
def chunk_list(lst, chunk_size):
    """Split a list into chunks of a specified size."""
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Reading the content of the file
df = pd.read_excel('thesis-data.xlsx')
reasons = df['reasonsOriginal'].tolist()

# Fill NaN to not receive error
reasons = [re.sub(r'\n', ' ', str(reason)) if isinstance(reason, str) else reason for reason in reasons]

# Split the list into chunks of 100 elements each
reasons_chunks = chunk_list(reasons, 100)

project_number_or_id = "add your project number or id here"


# Get the Bearer token from gcloud
access_token = "add your access token here" 

# Set the API endpoint
url = f"https://translation.googleapis.com/v3/projects/{project_number_or_id}:translateText"

# Set the headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "x-goog-user-project": project_number_or_id,
    "Content-Type": "application/json; charset=utf-8",
}

sentences_translated = []

for i, reasons_chunk in enumerate(reasons_chunks):
    json_data = {
        "sourceLanguageCode": "is",
        "targetLanguageCode": "en",
        "contents": reasons_chunk
    }

    j_data = json.dumps(json_data, ensure_ascii = False)
    with open(f"ToTranslate/data-Part{i+1}.json", 'w') as file:
        json.dump(json_data, file, ensure_ascii=False)
    
    # Make the POST request
    response = requests.post(url, headers=headers, data=j_data.encode('utf-8'))

    # Print the response
    print(response.status_code)
    print(response.json())
    
    # Save the JSON response content in a File
    file_name = f"Translated/EnglishData-Part{i + 1}.json"
    response_data = response.json()
    
    for i in range(len(response_data["translations"])):
        sentences_translated.append(response_data["translations"][i]["translatedText"])

    with open(file_name, "w") as file:
        json.dump(response_data, file, ensure_ascii=False)

df['reasonsEnglish'] = sentences_translated

# Save the new df in the file
df.to_excel('thesis-data-translated.xlsx', index=False)
