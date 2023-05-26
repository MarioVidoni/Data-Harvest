from bs4 import BeautifulSoup
import os.path as os
import requests
import pandas as pd
import re
from datetime import datetime


#Obtain de directory where the python file is located
dirname = os.dirname(__file__)

#Format to define th date input strinf
input_format = "%d/%m/%Y %H:%M"

try:
    #Site URL
    url='https://comunidad.comprasdominicana.gob.do/Public/Tendering/ContractNoticeManagement/Index'
    html_content = requests.get(url).content

    #Create an export directory for the csv file 
    export_dir = os.join(dirname, 'exported_data.parquet')

    #Using a ternary operator, if there's an already existing data storage, load it and concatenate both dataframes
    df = pd.read_parquet(export_dir) if os.exists(export_dir) else pd.DataFrame(columns=['Unidad de compras', 'Descripcion', 'Fecha de publicacion', 'Monto total'])

    #Start the spider 
    soup = BeautifulSoup(html_content, 'html.parser')

    #Obtain all the values that comply with the tags from the html content
    rows = soup.find_all(attrs={"class": ['gridLineDark', 'gridLineLight']})

    #For each row in all the rows
    for row in rows:
        #Extract the wanted elements from the selected row
        element = [
            row.find(attrs={"id": 'tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultListtd_thAuthorityNameCol'}).get_text().lower(),
            row.find(attrs={"id": 'tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultListtd_thDescriptionCol'}).get_text().lower(),
            datetime.strptime(row.find(attrs={"id": 'tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultListtd_thOfficialPublishDateCol'}).get_text().split(' (')[0], input_format),
            float(re.sub('[a-z, A-Z]', '', row.find(attrs={"class": 'VortalNumericSpan DecimalValue'}).get_text()))
        ]
        #If the description exists in the dataframe do not insert the element
        if not any(df['Descripcion'] == element[1]):
            #insert element in dataframe's last position
            df.loc[len(df)] = element    

    #Export the dataframe to a parquet file (Faster and lighter compared to csv)
    df.to_parquet(export_dir, engine='fastparquet', index=False)
    #df.to_csv(export_dir, index=False)

# Exception in case the provided file doesn't have the required structure
except pd.errors.EmptyDataError:
    print("The file doesn't have the required structure. Please delete it and perform the operation again.")
# Exception in case the website is couldn't be reached
except requests.exceptions.RequestException:
    print("We couldn't establish a successful connection to the page. Please check your network connection or try again later.")


