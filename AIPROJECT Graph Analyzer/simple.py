import fitz  # PyMuPDF
import pandas as pd
import re

# Step 1: Extract text from PDF
pdf_path = r"C:\Users\Administrator\Downloads\Downloads_uni\72k Quote Revised.PDF"
document = fitz.open(pdf_path)
text = ""
for page_num in range(len(document)):
    page = document.load_page(page_num)
    text += page.get_text()

# Step 2: Parse the text to extract codes and quantities
pattern = re.compile(r'(\d{6})\n\w+\nPAAE111202\nW18V46\n[\d\.,]+\/\n[\d\.,]+\s+\w+\n\s+(\d+)\s+PC')
matches = pattern.findall(text)

# Step 3: Organize the data into a DataFrame and group by code
data = []
for match in matches:
    code = match[0]
    qty = int(match[1].replace(',', ''))
    data.append((code, qty))

df = pd.DataFrame(data, columns=['Code', 'Quantity'])

# Group by code and sum the quantities
grouped_df = df.groupby('Code').sum().reset_index()

print(grouped_df)
