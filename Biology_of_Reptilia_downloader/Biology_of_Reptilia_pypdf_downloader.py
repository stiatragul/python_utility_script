from PyPDF2 import PdfFileMerger
import os
import requests
from tqdm import tqdm

# Inputs
print('Which volume of Biology of Reptilia?')
volume_no = input(str())

print('Page from: First page you want (note that page in URL might be different than actual page in the book)')
page_start = input(str())

print('Page to: ')
page_end = input(str())

# Define base URL
base_url_string = str('https://secureservercdn.net/198.71.233.33/24n.676.myftpupload.com/wp-content/bor/' + volume_no.zfill(2) + '/BotR' + volume_no.zfill(2) + '-page')

# List of pages append to url
urls_1 = [base_url_string + str(i) for i in range(int(page_start), int(page_end))]

# Add '.pdf' to end of each url
urls = [s + '.pdf' for s in urls_1]

# Can specify the number manually like this
# urls = [base_url + str(i) for i in range(349,390) + extension]

merger = PdfFileMerger()

# Loop through the lists

for url in tqdm(urls, desc='Downloading PDFs...'):
    response = requests.get(url)
    title = url.split("/")[-1]
    with open(title, 'wb') as f:
        f.write(response.content)
    merger.append(title)
    # Remove merged pdf
    os.remove(title)

# Write name of the merger
result_pdf_name = 'Biology_of_Reptilia' + '_Volume' + '_' + volume_no + '_' + page_start + '_' + page_end + '.pdf'
merger.write(result_pdf_name)
merger.close()

