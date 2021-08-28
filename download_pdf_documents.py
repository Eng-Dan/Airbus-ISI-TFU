from bot_pdf_download import activate_bot

urlLinktoDocument = [
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MjguNTEuMDAuMDA0/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MjMuMTMuMDAuMDIx/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzYuMTEuMDAxMDY=/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzIuNTEuMDAuMDI4/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzMuNDkuMDAuMDAz/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/NDkuMDAuMDAuMDYx/article.html'
]

for url in urlLinktoDocument:
    activate_bot(url, 'SAO_danilobs', 'Aib20211')