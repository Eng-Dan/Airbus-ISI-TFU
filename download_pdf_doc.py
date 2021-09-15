import os.path
import csv
from bot_pdf_download import run_bot_pdf_download

def execute_download(numDownloads, AirbusUserName, AirbusUserPass):
    pathToControlFile = 'C:\\Users\\danilo.bezerra\\Data Source\\Cleaned\\doc_manager_download_control.csv'
    pathToDownloadFolder = 'C:\\Users\\danilo.bezerra\\Downloads\\'

    with open(pathToControlFile, newline='', mode='r+') as csvFile:
        csvReaderObject = csv.DictReader(csvFile)
        dataset = list(csvReaderObject)

        downloads = 0
        try:
            for rowDict in dataset:
                fileName = rowDict['document_id'] + '_' + rowDict['document_type'] + '.pdf'

                if not os.path.isfile(pathToDownloadFolder + fileName):
                    downloadWait = 5

                    for attempt in range(1, 4):
                        run_bot_pdf_download(rowDict['document_id'], rowDict['document_type'], rowDict['url_link_to_document'], AirbusUserName, AirbusUserPass, waitToDownload=downloadWait)
                        
                        if not os.path.isfile(pathToDownloadFolder + fileName):
                            print('Attempt', attempt, 'FAILED for', fileName)
                            downloadWait += 10
                        else:
                            print('Downloaded:', fileName)
                            downloads += 1
                            break

                if downloads == numDownloads:
                    print('Full batch download complete.')
                    break

            if downloads == 0:
                print('It seems that all documents from DOWNLOAD CONTROL file have been already downloaded.')
            elif downloads > 0:
                print(downloads, 'new documents downloaded.')

        except:
            print('>> Error or none documents to download.')