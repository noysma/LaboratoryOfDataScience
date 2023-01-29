import csv

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
        data = csv.DictReader(answer_csv)
        Date_Id, Date, day, month, year, quarter = ([] for _ in range(6))
        set_check = set()
        id = 0

        for row in data:
            y = row["DateOfBirth"].split("-")[0]
            m = row["DateOfBirth"].split("-")[1]
            d = row["DateOfBirth"].split("-")[2]
            """ 
            We don't want separator between the values of the date
            so we split it and concatenate as a string
            """
            temp = str(y+m+d)
            # Using Sets the duplicates check is faster
            if(temp not in set_check):
                id +=1
                Date_Id.append(id)
                Date.append(y+m+d)
                day.append(d)
                month.append(m)
                year.append(y)
                set_check.add(temp)
                # Divided the months in quarters
                if(1 <= int(m) <= 3):
                    quarter.append(1)
                elif(4 <= int(m) <= 6):
                    quarter.append(2)
                elif(7 <= int(m) <= 9):
                    quarter.append(3)
                elif(10 <= int(m) <= 12):
                    quarter.append(4)

            """
            DateAnswered has a different format rexported to DateOfBirth
            so we splitted in another way and checked for duplicate with
            Set.
            """
            
            ADate = row["DateAnswered"].split(" ")
            ADate = ADate[0].split("-")
            y = ADate[0]
            m = ADate[1]
            d = ADate[2]
            temp = str(y+m+d)
            # Using Sets the duplicates check is faster
            if(temp not in set_check):
                id += 1
                Date_Id.append(id)
                Date.append(y+m+d)
                day.append(d)
                month.append(m)
                year.append(y)
                set_check.add(temp)
                if(1 <= int(m) <= 3):
                    quarter.append(1)
                elif(4 <= int(m) <= 6):
                    quarter.append(2)
                elif(7 <= int(m) <= 9):
                    quarter.append(3)
                elif(10 <= int(m) <= 12):
                    quarter.append(4)

# Opened a new file in wrtite mode and put there all the information extracted
with open("answerdatasetnew/Date.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["DateId", "Date", "Day", "Month", "Year", "Quarter"])
    # Used Zip() for parallel iteration
    for item in zip(Date_Id, Date, day, month, year, quarter):
        writer.writerow(item)