import csv

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
    with open("Dataset/subject_metadata.csv") as metadata_csv:
        data = csv.DictReader(answer_csv)
        metadata = csv.DictReader(metadata_csv)
        Subject_id, list_subject, description = ([] for _ in range(3))
        subjects_dict, level_dict, final_dict = ({} for _ in range(3))
        set_check = set()
        dict_id = 0
        
        for row in data:
            tmp = row["SubjectId"]
            if (tmp not in set_check):
                set_check.add(tmp)
                Subject_id.append(row["SubjectId"])
        # Replaced unneeded characters
        for row in Subject_id:
            new_row = str(row.replace("]", "").replace("[", ""))
            list_subject.append([int(x) for x in new_row.split(", ")])
        
        # Create a dictionary that corresponds SubjectId to Levels
        for row in metadata:
            level_dict[row["\ufeffSubjectId"]] = row["Level"]
    
        """
        We have to swap that item because we have to respect the levels of every 
        subject.
        """
        for single_list in list_subject:
            for subj_id in single_list:
                for key, value in level_dict.items():               
                    if(subj_id == int(key)):
                        subjects_dict[key] = value
            # Temporary dictionary used to sort values by level
            subjects_dict = dict(sorted(subjects_dict.items(), key = lambda kv: kv[1]))
            # Dictionary creation with id as key and ordered SubjectId as value
            final_dict[dict_id] = list(subjects_dict.keys())
            dict_id += 1
            subjects_dict = {}

        # Initialization of the pointer
        metadata_csv.seek(0)
        metadata = csv.DictReader(metadata_csv)

        # Declare separator for the final string
        hyphen_sep = " - "
        str_final = ""

        """
        Checked if there is some SubjectId corrisponding to the SubjectId in metadata file. 
        If there is the loop insert the string concatenating all the metadata informations
        in a list.
        """
        for items in final_dict.values():
            for id in items:
               for row in metadata:
                    """
                    "\ufeff" this is needed because in the csv the column start with it.
                    We didn't want modify the initial file (I use Mac, for Windows there
                    will be "ï»¿").
                    """
                    if(row["\ufeffSubjectId"] == id):
                        col_merge = str(row["Name"] + hyphen_sep)
                        str_final += col_merge
                        metadata_csv.seek(0)
                        break
            description.append(str_final[:-2]) # with this we remove the last " - "
            str_final=""       

# Opened a new file in wrtite mode and put there all the information extracted
with open("answerdatasetnew/Subject.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["SubjectId", "Description"])
    # Used Zip() for parallel iteration
    for item in zip(range(1,len(Subject_id)+1), description):
        writer.writerow(item)