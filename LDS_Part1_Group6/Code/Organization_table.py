import csv

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
        data = csv.DictReader(answer_csv)
        Organization_Id, Group_Id, Quiz_Id, Scheme_Work = ([] for _ in range(4))
        set_check = set()
        id = 0

        """
        If this loop doesn't find any duplicate will append all the Ids in different lists
        """

        for row in data:
            Qui_Id = row["QuizId"]
            Geo_Id = row["GroupId"]
            Scheme_Id = row["SchemeOfWorkId"]
            # Temporary stirng where we concatenate values for the check
            temp = str(str(Qui_Id) + "," + str(Geo_Id) + "," + str(Scheme_Id))
            # Using Sets the duplicates check is faster
            if(temp not in set_check):
                id += 1            
                Organization_Id.append(id)
                Group_Id.append(Geo_Id)
                Quiz_Id.append(Qui_Id)
                Scheme_Work.append(Scheme_Id)
                set_check.add(temp)
            else:
                continue

# Opened a new file in wrtite mode and put there all the information extracted
with open("answerdatasetnew/Organization.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["OrganizationId", "GroupId", "QuizId", "SchemeOfWorkId"])
    # Used Zip() for parallel iteration
    for item in zip(Organization_Id, Group_Id, Quiz_Id, Scheme_Work):
        writer.writerow(item)