"# XML to DataFrame App" 
I have built this small application which reads an XML file and converts it to a dataframe and this can be downloaded as a CSV file. 

I used the xml.etree.ElementTree package to parse the xml file that is uploaded.

I have used a recursive function which iterates through the element of the root of the xml file and further iterates through its subchilds if its present in the parent element.

After iterating, the tags and its corresponding texts are stored in dictionary as key value pairs.

Finally, the dictionay is converted to a dataframe and to a CSV file.

Click the following link to view the app:https://python-projects-bjt52xrqtkbb6tdjniadnd.streamlit.app/
