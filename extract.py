import re

# Module to get the details of a research paper using doi.
from habanero import Crossref

# Module to extract text from pdf
from pdfminer.high_level import extract_text

# Azure related modules
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


from datetime import datetime


def extract_text_from_pdf(pdf_file_path: str) -> str:
    text = extract_text(pdf_file_path)
    return text

def asadadq

def extract_doi(text: str) -> str:
    regexDOI = re.compile("[https://?doi|DOI][\s\.\:]{0,2}(10\.\d{4}[\w\:\.\-\/a-z]+)[A-Z\s]")
    doi = regexDOI.findall(text)
    return doi

# Exract text here.
pdf_file_path = './Azure Papers/Fluoxetine-Hollander.pdf'
text = extract_text_from_pdf(pdf_file_path)

# Regex to match doi from text
regexDOI = re.compile('[https://?doi|DOI][\s\.\:]{0,2}(10\.\d{4}[\w\:\.\-\/a-z]+)[A-Z\s]')
doi = regexDOI.findall(text)

# Get paper details using DOI.
cr = Crossref