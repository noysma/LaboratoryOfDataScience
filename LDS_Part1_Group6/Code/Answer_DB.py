import pyodbc
import csv
#connect to data source, using userName and userPWD

server = 'tcp:131.114.72.230'
database = 'Group_6_DB'
username = 'Group_6'
password = 'E8IT2V6N'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

with open("../LDS_Project/Dataset/Answers.csv") as csvfile:
    file = csv.DictReader(csvfile)

    for row in file:
        cursor.execute("""INSERT INTO Group_6.Answers (AnswerId,QuestionId,UserId,OrganizationId,DateId, SubjectId, AnswerValue,
        CorrectAnswer,IsCorrect,Confidence) values(?,?,?,?,?,?,?,?,?,?) """, row["AnswerId"], row["QuestionId"], row["UserId"],  row["OrganizationId"], 
        row["DateId"],row["SubjectId"], row["AnswerValue"], row["CorrectAnswer"],  row["IsCorrect"], row["Confidence"])
    cnxn.commit()
    cursor.close()