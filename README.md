# LaboratoryOfDataScience

## Project Assignment - Part 1

### Introduction
In Part 1 of the project we are required to create and populate a database starting from .csv files and perform different operations on it. In the following we can find a set of incremental assignments, each one with a brief description of what you are required to produce and what tools you can use for the task.

### Build the datawarehouse
answers full.csv contains the main body of data: a table with data about answers given by students to various multiple-choice questions. In the same table, there are several data regarding the questions, the students and the subject of the questions.\
The file subject metadata.csv contains informations about the subject of each ques- tion. The subject is given by a list of integers in the main data that can be used to index the answers full.csv to retrieve the topic of the question.\
The goal of the following assignments is to build the schema and deploy it on server lds.di.unipi.it. Beware that, just as in real-life scenario, files may contain missing values and/or useless data.

### Assignment 0
Create the database schema using SQL Server Management Studio. The name of the database must be GroupID DB (example: Group 01 DB).

### Assignment 1
Write a python program that splits the content of answers full.csv into the six separate tables: answers, organization, date, subject, user and geography. You will also have to write several functions to perform integration of the main data body.\
In particular:
- generate some missing ids, like organizationid and geoid. Use the data that you have available in a suitable way to infer or generate these ids.
- the iscorrect attribute is the main measure of the datawarehouse. You can compute its values by comparing the variables answer value and correct answer
- the description in the subject table should be a string describing the various topics of the question in subject level order (explore the subject metadata.csv to learn more about that)
- find a way of integrating the continent into the Geography table. You can retrieve the information somewhere, or find a way of providing it yourself
- the Data table should accommodate for both dates of birth of users and for dates of answers. You can clip dates to the day, discarding hours and minutes.

All the above operations must be done WITHOUT using the pandas library.

### Assignment 2
Write a Python program that populates the database GroupID DB with all teh data you prepared in Assignment 1, establishing schema relations as appropriate.

---

## Project Assignment - Part 2

### Introduction
In Part 2 of the project we are required to solve some problems on the database you created in Part 1. Solve the exercises using Sequel Server Integration Services (SSIS) with computation on client side (i.e., do not use any sql command in the nodes, only standard SSIS nodes).

### Assignment 0
For every year, the users ordered by total number of answers

### Assignment 1
For every subject, the correctness confidence index is defined as the ratio between correct answers and wrong answers multiplied by the average confidence. Provide such index for every subject, considering only German and English students.

### Assignment 2
For each region, the percentage of correct answers with respect to the country of origin.

---

## Project Assignment - Part 3

### Introduction
In Part 3 of the project we are required to answer some business questions on a datacube that we will create on the database we prepared. Document how we build your datacube in our report and solve the business questions using MultiDimensional eXpressions (MDX) in SQL management studio.

### Assignment 0
Build a datacube from the data of the tables in your database, defining the appropriate hierarchies for time and geography. Create the needed measures based on the queries you need to answer.

### Assignment 1
Show the total correct answers for each country and the grand total with respect to the continent.

### Assignment 2
Show the total confidence for each year and the running yearly for European students.

### Assignment 3
Show the ratio between the total correct answers of each year w.r.t the previous year.

### Assignment 4
Create a dashboard that shows the geographical distribution of correct answers and incorrect answers

### Assignment 5
Create a plot/dashboard of your choosing, that you deem interesting w.r.t. the data available in your cube               
