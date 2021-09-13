
# from bot_pdf_download import run_bot_pdf_download
import csv
from os import close

'''
1. read csv file and store each row data in a dictionary variable
2. for each row, check if the file already exists in the download folder
    3. If it does not, run the bot to downloand
    4. If ir does, 

'''

def read_csv_file(pathToFile):
    csvFile = open(pathToFile, newline='', mode='r+')
    data = csv.DictReader(csvFile)
    # csvFile.close()
    return data



# Single test case
fileToRead = 'C:\\Users\\danilo.bezerra\\Data Source\\Cleaned\\doc_manager_download_control.csv'
csvReaderObject = read_csv_file(fileToRead)

csvDataset = list(csvReaderObject)

print(csvDataset[0]['document_id'])

csvDataset[0]['document_id'] = 'foo'

print(csvDataset[0]['document_id'])
print(csvDataset[0])



# print(controlData[0]['document_type'], controlData[0]['document_id'], controlData[0]['url_link_to_document'])