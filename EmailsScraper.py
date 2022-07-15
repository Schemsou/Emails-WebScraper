from bs4 import BeautifulSoup as btsp
import requests, re
import pandas as pd


email_id = re.compile("\w+@\w+.\w+.")
html = requests.get('https://webspotter.io/blackrock-email-format-hn8a5n').text
soup = btsp(html, "html.parser")

emails = soup.find_all(text=email_id)

#creating an empty list to add emails into it
emails_list = []

for email in emails:
    emails_list.append(email)

#creating a dataframe with pandas and pass our data to it
data = pd.DataFrame(emails_list)

#storing data in an excel file
data.to_excel("emails_list.xlsx")

