from selenium.webdriver.common.by import By
import pandas as pd
from utils import get_webdriver
import re
import os

driver = get_webdriver()
url = 'https://mvnrepository.com/artifact/org.apache.logging.log4j/log4j-core'
driver.get(url)

table = driver.find_element(By.CLASS_NAME, 'grid.versions')

rows = table.find_elements(By.TAG_NAME, 'tr')

data = []
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if len(cells) > 2:  
        style_text = cells[0].text.strip()  
        version_text = cells[1].text.strip()  
        vulnerabilities_text = cells[2].text.strip()  
        if "vulner" in vulnerabilities_text.lower():
            match = re.search(r'(\d+)\s+vulnerabilities', vulnerabilities_text.lower())
            vulnerabilities_number = match.group(1) if match else "N/A"  
            data.append([style_text, version_text, vulnerabilities_number, vulnerabilities_text])

            
df = pd.DataFrame(data, columns=['Style Data', 'Version', 'Number of Vulnerabilities', 'Vulnerabilities Details'])

data_directory = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(data_directory):
    os.makedirs(data_directory) 

csv_path = os.path.join(data_directory, 'extracted_data.csv')
df.to_csv(csv_path, index=False)

print(df)

driver.quit()
  
## test 