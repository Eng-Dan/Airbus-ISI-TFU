import os.path
import csv
from bot_pdf_download import run_bot_pdf_download

def execute_download(numDownloads, AirbusUserName, AirbusUserPass):
    pathToControlFile = 'C:\\Users\\danilo.bezerra\\Data Source\\Cleaned\\doc_manager_download_control.csv'
    pathToDownloadFolder = 'C:\\Users\\danilo.bezerra\\Downloads\\DocManager\\'

    with open(pathToControlFile, newline='', mode='r+') as csvFile:
        csvReaderObject = csv.DictReader(csvFile)
        dataset = list(csvReaderObject)

        downloads = 0
        try:
            for rowDict in dataset:
                fileName = rowDict['document_id'] + '_' + rowDict['document_type'] + '.pdf'
                fileDownloaded = os.path.isfile(pathToDownloadFolder + fileName)

                if not fileDownloaded:
                    downloadWait = 5

                    for attempt in range(3):
                        run_bot_pdf_download(rowDict['document_id'], rowDict['document_type'], rowDict['url_link_to_document'], AirbusUserName, AirbusUserPass, downloadWait)
                        
                        if not fileDownloaded:
                            print('Failed attempt to download:', fileName)
                            downloadWait += 5
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
                print('Downloaded', downloads, 'new documents.')

        except:
            print('>> Error or none documents to download.')