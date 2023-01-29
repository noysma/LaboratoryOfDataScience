import csv

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
    data = csv.DictReader(answer_csv)
    Date_Id, Geo_Id, Gender, User_Id = ([] for _ in range(4))
    date_dict_check, geo_dict_check = ({} for _ in range(2))
    id_set_check = set()
    d_id = 0
    r_id = 0

    for row in data:
        id = row["UserId"]
        gend = row["Gender"]
        reg = row["Region"]

        # Check for duplicate Id in our csv defining a set.
        if(id not in id_set_check):
            User_Id.append(id)
            Gender.append(gend)
            id_set_check.add(id)

        """ 
        We don't want separator between the values of the date
        so we split it and concatenate as a string
        """
        y = row["DateOfBirth"].split("-")[0]
        m = row["DateOfBirth"].split("-")[1]
        d = row["DateOfBirth"].split("-")[2]
        birth_date = str(y+m+d)
        
        # check duplicates in DateOfBirth
        if(birth_date not in date_dict_check):
            d_id += 1
            date_dict_check[birth_date] = d_id
        """
        DateAnswered has a different format rexported to DateOfBirth
        so we splitted in another way and checked for duplicate with
        dictionaries.
        """
        ADate = row["DateAnswered"].split(" ")
        ADate = ADate[0].split("-")
        y = ADate[0]
        m = ADate[1]
        d = ADate[2]
        Date_answ = str(y+m+d)
        # check duplicates in DateAnswered
        if(Date_answ not in date_dict_check):
            d_id += 1
            date_dict_check[Date_answ] = d_id
        # Saving the unique dates in a list
        for key, value in date_dict_check.items():
            if(birth_date==key):
                Date_Id.append(value)
                break

        # Check duplicates for Geography
        if(reg not in geo_dict_check):
            r_id += 1
            geo_dict_check[reg] = r_id
        for key, value in geo_dict_check.items():
            if(reg == key):
                Geo_Id.append(value)
                break

# Opened a new file in wrtite mode and put there all the information extracted
with open("answerdatasetnew/User.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["UserId", "DateId", "GeoId", "Gender"])
    # Used Zip() for parallel iteration
    for item in zip(User_Id, Date_Id, Geo_Id, Gender):
        writer.writerow(item)