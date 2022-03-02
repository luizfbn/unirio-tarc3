import tabula

# URL utilizada como exemplo na documentaçao do tabula
pdfURL = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

table = tabula.read_pdf(pdfURL, pages=1, stream=True)

print(table)
