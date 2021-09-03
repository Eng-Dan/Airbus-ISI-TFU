import csv

def manage_file_opening(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        csvFile.close()
    
    return wrapper


@manage_file_opening
def read_csv_file(csvFileToRead):
    csvFile = open(csvFileToRead, newline='')
    data = csv.DictReader(csvFile)
    return data



# Single test case
fileToRead = 'C:\\Users\\danilo.bezerra\\Data Source\\Cleaned\\doc_manager_download_control.csv'
controlData = read_csv_file(fileToRead)

for row in controlData:
    print(row)