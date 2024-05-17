import re

def extract_data(text):
    pattern = r'[a-zA-Z0-9]+:[a-zA-Z0-9]+'
    return re.findall(pattern, text)

def better_extract_data(text):
    pattern = r'([a-zA-Z0-9]+):([a-zA-Z0-9]+)'
    return re.findall(pattern, text)