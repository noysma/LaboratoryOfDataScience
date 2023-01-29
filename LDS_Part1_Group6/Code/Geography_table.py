import csv
import pycountry
import pycountry_convert as pc

# This function will return the name of the continent based on the code of the country that we have in our csv
def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Opened csv in read mode
with open("Dataset/answerdatacorrect.csv") as answer_csv:
        data = csv.DictReader(answer_csv)
        Geo_Id, Region, Country_Name, Region_Id, CountryCode, Continent = ([] for i in range(6))
        set_check = set()
        id = 0

        for row in data:
            Code = row["CountryCode"]

            """
            Due to some library issue we have to modify "uk" code into "gb" otherwise we couldn't
            find "United Kingdom as "Country Name"
            """

            if Code == "uk":
                Code = "gb"
            Single_Region = row["Region"]
            Region_Id = row["RegionId"]
            Single_Country = row["CountryCode"]
            country_codes = pycountry.countries.get(alpha_2=Code)
            Country_Check = country_codes.name
            Cont_Check = country_to_continent(Country_Check)
            # Here we had the same problem as before for Continent name
            if(Cont_Check == "North America"):
                    Cont_Check="America"

            """
            Check for duplicates in our csv defining a set.
            We choose Sets because are faster than lists.
            """

            temp = str(str(Region_Id) + "," + Single_Region + "," + Single_Country) 
            if(temp not in set_check):
                    id += 1
                    Geo_Id.append(id)
                    Region.append(Single_Region)
                    Country_Name.append(Country_Check)
                    set_check.add(temp)
                    Continent.append(Cont_Check)

# Opened a new file in wrtite mode and put there all the information extracted
with open("answerdatasetnew/Geography.csv", "w", newline="") as outputfile:
    writer = csv.writer(outputfile)    
    writer.writerow(["GeoId", "Region", "CountryName", "Continent"])
    # Used Zip() for parallel iteration
    for item in zip(Geo_Id, Region, Country_Name, Continent):
        writer.writerow(item)