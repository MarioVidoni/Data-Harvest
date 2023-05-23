from bs4 import BeautifulSoup
import os.path as os
import requests
import pandas as pd

#Obtain de directory where the pyhton file is located
dirname = os.dirname(__file__)

try:
    #Site URL
    url='https://comunidad.comprasdominicana.gob.do/Public/Tendering/ContractNoticeManagement/Index'
    html_content = requests.get(url).content

    #Create an export directory for the csv file 
    export_dir = os.join(dirname, 'exported_data.csv')

    #Using a ternary operator, if there's an already existing data storage, load it and concatenate both dataframes
    df = pd.read_csv(export_dir) if os.exists(export_dir) else pd.DataFrame(columns=['Descripciones', 'Monto'])

    #Start the spider 
    soup = BeautifulSoup(html_content, 'lxml')

    #Obtain all the values that comply with the tags from the html content
    filas = soup.find_all(attrs={"class": ['gridLineDark', 'gridLineLight']})

    #For each row in all the rows
    for fila in filas:
        element = [fila.find(attrs={"id": 'tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultListtd_thDescriptionCol'}).get_text().lower(), fila.find(attrs={"class": 'VortalNumericSpan DecimalValue'}).get_text().lower()]
        if ~df.columns.isin([element]).any():
            df = pd.concat([pd.DataFrame(element), df], ignore_index=True)
            #df = df.append(pd.Series(element, index = ["Descripciones","Monto"]), ignore_index=True)
        #insert text from the corresponding column

    #Export the dataframe to a csv (index eliminated)
    df.to_csv(export_dir, index=False)

except pd.errors.EmptyDataError:
    print("El archivo no tiene la estructura aceptada, favor eliminar este y ejecutar nuevamente")
except requests.exceptions.RequestException:
    print("No se pudo establecer la conexion con la pagina de manera exitosa, favor revisar su conexion a la red")

#Displaying array
print(df.to_string())

#En el caso de que se usen los valores monetarios, insertar la siguiente linea de codigo dentro del append de monto
#re.sub(r'[a-zA-Z, ]', '', fila.find(attrs={"class": "VortalNumericSpan DecimalValue"}).get_text().lower())
#tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tr
