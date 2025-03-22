
import pandas as pd
from langchain_core.documents import Document

####data is read from the location
def dataconverter():
    product_data =pd.read_csv("../data/flipkart_product_review.csv")

    data = product_data [["product_title","reveiw"]]

    product_list =[]

    ######to get json inside the productlist

    #iterate the row from dataframe
    for index, rows in data.iterrows():
        ##construct json object with productname and reveiw
        obj = {
            'product_name': row['product_title'],
            'reveiw' : row['reveiw']
        }

        #now append the above json object to prdt list

        product_list.append(obj)

        #### we require langchain_core.documents we need Document to convert data into document format
        ### so this docs store the data in page_content which is used for converting into embedding

        docs =[]
        for entry in product_list:
            metadata ={"product_name": entry['product_name']}
            doc = Document(page_content=entry['reveiw'], metadata =metadata)
            docs.append(doc)

        return docs    
