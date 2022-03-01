import os.path
import csv
from selenium_bot import run_bot


def get_path_variables(file):
    in_file = open(file, newline='', mode='r')
    variables = in_file.readlines()
    in_file.close()
    return variables


def execute_downloads(num_downloads, path_variables_file, wait_to_download=5):
    """
    Manages and executes the orders to run the Selenium bot as a functions of the documents pending to be downloaded in
    the destination folder.

    :param num_downloads: the number of documents to download.
    :param path_variables_file: path to file in .csv format containing the documents meta data.
    :param wait_to_download: an initial time interval in seconds to wait for complete download of the document, default = 5 seconds.
    :return: None.

    file_name.csv
        |- document_id: e.g.: 00.00.00016
        |- document_type: e.g.: ISI or TFU
        |- document_status: e.g.: CLOSE or OPEN or N/A
        |- first_issue_date: e.g.: 2011-10-26
        |- last_revision_date: e.g.: 2018-12-07
        |- url_link_to_document: e.g.: https://w3.airbus.com/1H43/MEFO_AW/ISI/MDAuMDAuMDAwMTY=/article.html
        |- pdf_downloaded: e.g.: True or False
    """

    airbus_login = input('Enter your Airbus World user name:')
    airbus_password = input('Enter your Airbus World password:')

    path_variables = get_path_variables(path_variables_file)
    # [0] path to .csv download control file
    # [1] path to download folder
    # [2] path to chromedriver.exe

    # documents_list_file = 'C:\\Users\\danilo.bezerra\\Data Source\\Cleaned\\doc_manager_download_control.csv'
    # download_folder_path = 'C:\\Users\\danilo.bezerra\\Downloads\\'

    with open(path_variables[0], newline='', mode='r+') as csvFile:
        csv_reader_obj = csv.DictReader(csvFile)
        dataset = list(csv_reader_obj)

        downloads = 0
        try:
            for row in dataset:
                file_name = row['document_id'] + '_' + row['document_type'] + '.pdf'

                if not os.path.isfile(path_variables[1] + file_name):
                    download_wait = wait_to_download

                    for attempt in range(1, 4):
                        run_bot(row['document_id'],
                                row['document_type'],
                                row['url_link_to_document'],
                                airbus_login,
                                airbus_password,
                                download_wait,
                                path_variables[2])

                        if not os.path.isfile(path_variables[1] + file_name):
                            print('Bot manager message: Attempt', attempt, 'FAILED to download', file_name)
                            download_wait += 10
                        else:
                            downloads += 1
                            print('Bot manager message: Downloaded', downloads, 'of', num_downloads, file_name, '\n')
                            break

                if downloads == num_downloads:
                    print('Bot manager message: Full batch download complete.')
                    break

            if downloads == 0:
                print('Bot manager message: All documents from DOCUMENT LIST FILE have been downloaded already.')
            elif downloads > 0:
                print('Bot manager message:', downloads, 'new documents downloaded.')

        except:
            print('Bot manager message: Error or none documents to download.')
