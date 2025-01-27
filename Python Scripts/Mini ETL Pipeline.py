# This is an ETL (Extract, Transform, Load) pipeline script.
import csv #The essential python library for this script that adds csv functionalities
import pytest

file_name = 'student_test_scores_extended.csv' #Declaring file name - this can be changed!

# This function opens the file and returns "csv_reader",
def open_file(file_name):
    try:
        with open(file_name, newline='') as file:
            csv_reader = list(csv.DictReader(file)) #Method that produces the list of dicts
            return csv_reader
    except FileNotFoundError:
        print("File name not found")
        return None

# This function transforms the file by removing column headings we don't want, as well as creating a new column with an average score
def transform_file(csv_reader):
    data_list = [] #Initialising our list

    for row in csv_reader:
        data_list.append(row)
        # We now have a list of dictionaries where each dict is a row of the csv and the keys in each dict are the column headings

    for data in data_list:
        titles = ('Number of Siblings', 'Lunch Type', 'Test Preparation', 'Study Time (hours)', 'Favorite Subject', 'Main Teacher')
        for i in titles:
            data.pop(i)
            # Iterating over the list, removing each of these keys (and corresponding values) from each dict

    for data in data_list:
        avg = (int(data['Math Score']) + int(data['English Score']) + int(data['Science Score']) + int(data['Art Score']) + int(data['History Score']))/5
        data['Average Score'] = avg
        # Each dict in the list now has an extra key:value - 'Average Score':average of scores

    for data in data_list:
        print(data)
        # Have a look to see if it's worked
    return data_list

# This function writes the list of dicts to a new file using the DictWriter object
def write_file(data_list):
    with open('average_student_scores.csv', 'w') as newfile:
        writer = csv.DictWriter(newfile, fieldnames=data_list[0].keys())
        writer.writeheader() #Making the first row the column titles
        writer.writerows(data_list) #Adding each row to the table
# 'with' automatically saves and closes the file when you're finished

write_file(transform_file(open_file(file_name)))

#Running unit tests with pytest

"""
def test_open_file():
    result = open_file(file_name)
    assert result is not None
"""