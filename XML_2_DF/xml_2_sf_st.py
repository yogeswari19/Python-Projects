import streamlit as st
import xml.etree.ElementTree as ET
import pandas as pd

def parse_xml(element,parent_key=""):
    data={}
    for subelement in element:
        key=f"{parent_key}.{subelement.tag}" if parent_key else subelement.tag
        if list(subelement):
            data.update(parse_xml(subelement,key))
        else:
            data[key]=subelement.text
    return data

st.title("GENERIC XML TO CSV CONVERTER")
uploaded_file = st.file_uploader("Upload an XML file", type="xml")

if uploaded_file:
    xml_data=uploaded_file.read()
    root=ET.XML(xml_data)

    data=[parse_xml(child) for child in root]

    df=pd.DataFrame(data)

    st.subheader("Extracted Data")
    st.dataframe(df)

    csv_data=df.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV",csv_data,"extracted_data.csv")
