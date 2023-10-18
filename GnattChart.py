# Create a Gnatt Chart from using the Google Sheets API and Importing Data from Basecamp

# Import Libraries
import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


engine = create_engine("basecamp:///?User=test@northwind.db&Password=test123")
df = pandas.read_sql("SELECT Name, DocumentsCount FROM Projects WHERE Drafts = 'True'", engine)
 
df.plot(kind="bar", x="Name", y="DocumentsCount")
plt.show()