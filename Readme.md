[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) ![GitHub](https://img.shields.io/github/license/MarioVIdoni/Data-Harvest) ![Website](https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=https%3A%2F%2Fcomunidad.comprasdominicana.gob.do%2FPublic%2FTendering%2FContractNoticeManagement%2FIndex) ![GitHub watchers](https://img.shields.io/github/watchers/MarioVidoni/Data-harvest?style=social)[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/marioVidoni) 

# Data Harvest

## Introduction

Throughout the project, the primary objective revolved around the extraction and processing of data using web scraping techniques from a specific website. The goal was to retrieve relevant information and consolidate it into a Pandas DataFrame, providing a structured and organized representation of the collected data. By utilizing web scraping, we were able to gather data from the website in an automated manner, saving significant time and effort.

By leveraging the extracted data, performing thorough analyses, and drawing meaningful conclusions, the project aimed to acquire valuable knowledge and actionable insights. This knowledge could inform decision-making processes, drive improvements, and contribute to a broader understanding of the domain or subject matter being explored. Ultimately, the project sought to unlock the potential of the collected data and harness it for informed decision-making and strategic planning.

### Image of the website in question

![website in question](images\website.jpg)

## Describing the program

### How to run the program

All of the previous libraries are contained in a `requirements.txt` with their respective versions, you can install you can install this with the following command: `pip install -r requirements.txt`.

### Code examples

In the following code, we utilize a ternary operator. If an existing *Parquet* file is found, it is loaded. If not, a new DataFrame is created with the corresponding columns.

```
df = pd.read_parquet(export_dir) if os.exists(export_dir) else pd.DataFrame(columns=['Unidad de compras', 'Descripcion', 'Fecha de publicacion', 'Monto total'])
```

Furthermore, in this case, if the description of the element does not exist in the DataFrame, insert it at the last position of the DataFrame.

```
if not any(df['Descripcion'] == element[1]):
#insert element in dataframe's last position
    df.loc[len(df)] = element    
```

### Challenges

The main development challenge was excluding already inserted values. This occurred due to the consideration of numerous variables, where not every column could be considered a determining factor.
Another challenge involved the dense and repetitive use of ID attributes on the specific website. This emphasizes the importance of using readable names for variables and IDs, as advised by teachers.

### Future implementations

* Usage of selenium to extract the whole data from the table
* ETL process to a Data warehouse
* Upgrade of code 




