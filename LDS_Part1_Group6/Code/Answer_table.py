import csv

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
    data = csv.DictReader(answer_csv)
    Answer_Id, Question_Id, User_Id, Organization_Id, Date_Id, Answer_Value, \
    Correct_Answ, Is_corr, Confidence, Subject_Id = ([] for _ in range(10))
    subject_dict_check, org_dict_check, Date_dict = ({} for _ in range(3))
    count_org = 0
    sub_idx = 0
    date_count_id=0

    # SUBJECT ID
    """
    Checked for duplicates in SubjectId; if there are not we can append the value
    """

    for row in data:
        sub_id = row["SubjectId"]
        if sub_id not in subject_dict_check:
            sub_idx += 1
            subject_dict_check[sub_id] = sub_idx          
        for key, value in subject_dict_check.items():
            if(row["SubjectId"] == key):
                Subject_Id.append(value)
                break 
    
    # The pointer after this two lines will point to the first row of the csv 
    # (without considering the header)
    answer_csv.seek(0)
    data = csv.DictReader(answer_csv)

    # All the values that don't need a check will be just added into lists
    for row in data:
        Answer_Id.append(row["AnswerId"])
        Question_Id.append(row["QuestionId"])
        User_Id.append(row["UserId"])
        Answer_Value.append(row["AnswerValue"])
        Correct_Answ.append(row["CorrectAnswer"])
        Confidence.append(row["Confidence"])
        # Createing the True/False row if the answer gives is correct or not
        if(row["CorrectAnswer"] == row["AnswerValue"]):
            Is_corr.append(1)   # True
        else:
            Is_corr.append(0)   # False

    # Initialization of the pointer
    answer_csv.seek(0)
    data = csv.DictReader(answer_csv)

    # ORGANIZATION ID
    for row in data:
        QId = row["QuizId"]
        GId = row["GroupId"]
        Scf = row["SchemeOfWorkId"]
        temp = str(str(QId) + "," + str(GId) + "," + str(Scf))
        
        """
        check for duplicates for OrganizaionId using a dictionary and selected
        only the unique values
        """
        
        if temp not in org_dict_check:
            count_org += 1
            org_dict_check[temp] = count_org
        for key, value in org_dict_check.items():
            if(temp == key):
                Organization_Id.append(value)
                break

    # Initialization of the pointer
    answer_csv.seek(0)
    data = csv.DictReader(answer_csv)

    # DATE ID performing multiple checks for duplicate
    for row in data:
        y = row["DateOfBirth"].split("-")[0]
        m = row["DateOfBirth"].split("-")[1]
        d = row["DateOfBirth"].split("-")[2]
        
        """ 
        We don't want separator between the values of the date
        so we split it and concatenate as a string and checked
        for duplicates using dictionaries
        """

        Date_birth = str(y+m+d)
        if(Date_birth not in Date_dict):
            date_count_id+=1
            Date_dict[Date_birth] = date_count_id
        ADate = row["DateAnswered"].split(" ")
        ADate = ADate[0].split("-")
        y = ADate[0]
        m = ADate[1]
        d = ADate[2]
        Date_answ = str(y+m+d)
        if(Date_answ not in Date_dict):
            date_count_id+=1
            Date_dict[Date_answ] = date_count_id
        for key, value in Date_dict.items():
            if(Date_answ==key):
                Date_Id.append(value)
                break

# Opened a new file in wrtite mode and put there all the information extracted            
with open("answerdatasetnew/Answers.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["AnswerId", "QuestionId", "UserId", "OrganizationId", "DateId", "SubjectId", "AnswerValue", "CorrectAnswer", "IsCorrect", "Confidence"])
    # Used Zip() for parallel iteration
    for item in zip(Answer_Id, Question_Id, User_Id, Organization_Id, Date_Id, Subject_Id, Answer_Value, Correct_Answ, Is_corr, Confidence):
        writer.writerow(item)