from dotenv import dotenv_values
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Enter your Azure Text Analytics subscription key and endpoint
env_vars = dotenv_values('D:\BriefWise\Text-Summerizer\Text_Summarizer\.env')

print(env_vars)

endpoint = env_vars["endpoint"]
key = env_vars["key"]

def create_sublists(original_list, sublist_size):
    sublists = []
    sublist = []

    for element in original_list:
        sublist.append(element)

        if len(sublist) == sublist_size:
            sublists.append(sublist)
            sublist = []

    # Add the remaining elements if the original list length is not divisible by sublist_size
    if sublist:
        sublists.append(sublist)

    return sublists

def generate_summary(file_path):
    # [START extract_summary]
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )

    # Read the file
    with open(file_path, 'r') as file:
        text = file.read()

     # Split the text into smaller chunks
    lines = text.split("\n")
    chunks = create_sublists(lines, 5)
    summaries = []
    for chunk in chunks:
        poller = text_analytics_client.begin_extract_summary(chunk)
        extract_summary_results = poller.result()
        for result in extract_summary_results:
            if result.kind == "ExtractiveSummarization":
                return(" ".join([sentence.text for sentence in result.sentences]))
    
    print(summaries)
    return ' '.join(summaries)
            
    # [END extract_summary]

