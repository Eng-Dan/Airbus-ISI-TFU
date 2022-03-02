# Automated Airbus ISI and TFU documents download
This is a script to automate the browsing and download of Airbus ISI and TFU documents from AirbusWorld portal.

It aims the following public:
* Airline personnel in charge of reliability and maintenance engineering.
* Airline data scientists.

# Disclaimer
Airbus documents are proprietary, thus any downloaded document from AirbusWorld portal is subjected to export control.

# Requirements
1. Access to AirbusWorld portal at [w3.airbus.com](w3.airbus.com) is required in order to access the documents.
2. Download of chromedriver.exe is required for the automated brownsing in Google Chrome. 
   1. **ATTENTION!** Check the correct Google Chrome Driver version in accordance with your Chrome browser version.

# How it works
It uses a .csv control file [see schema](#Schema-of-the-.csv-control-file) containing the metadata of the documents to be downloaded.
The script will manage the download of all documents listed in the .csv control file.

1. Open the user_command.py file.
2. Pass to the `execute_downloads()` function the following parameters:
   1. The number o documents to download.
   2. A time interval to wait for complete download of the document.
      1. Adjust it as required depending on connexion speed.
   3. The path to the `path_variables.txt` file.
      1. Edit the correct path to the .csv control file, download folder and chromedriver.exe file.
3. Run the `user_command.py` file.
4. When prompted, enter your AirbusWorld login and password.
5. The automated browsing and download will be executed with Google Chrome.
6. Messages of successful or failed download will be listed in the python terminal.

## Schema of the .csv control file
    file_name.csv
        |- document_id: e.g.: 00.00.00016
        |- document_type: e.g.: ISI or TFU
        |- document_status: e.g.: CLOSE or OPEN or N/A
        |- first_issue_date: e.g.: 2011-10-26
        |- last_revision_date: e.g.: 2018-12-07
        |- url_link_to_document: e.g.: https://w3.airbus.com...html
        |- pdf_downloaded: e.g.: True or False