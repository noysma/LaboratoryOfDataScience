import pyodbc
import csv

# Connect to data source, using userName and userPWD
server = 'tcp:131.114.72.230'
database = 'Group_6_DB'
username = 'Group_6'
password = 'E8IT2V6N'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

with open("Dataset/Subject.csv") as csvfile:
        file = csv.DictReader(csvfile)

        for row in file:
            cursor.execute("""INSERT INTO Group_6.Subject (SubjectId,Descriptions) values(?,?)  """, row["SubjectId"], row["Description"])
        cnxn.commit()
        cursor.close()