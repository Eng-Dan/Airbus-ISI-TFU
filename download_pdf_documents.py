from bot_pdf_download import activate_bot

urlLinktoDocument = [
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MjguNTEuMDAuMDA0/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MjMuMTMuMDAuMDIx/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzYuMTEuMDAxMDY=/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/NzIuNjAuMDAuMDAy/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MzQuMDAuMDAuMTgz/article.html',
    'https://w3.airbus.com/1H43/MEFO_AW/TFU/MjUuMjMuMDAuMDA2/article.html',
]

for url in urlLinktoDocument:
    activate_bot(url, 'SAO_danilobs', 'Aib20211')