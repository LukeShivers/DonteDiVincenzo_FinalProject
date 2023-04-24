#main.py

# Name: Shirin Jain. Patrick Roote, Luke Shivers
# email: jain2ss@mail.uc.edu.edu, rootepr@mail.uc.edu, shiverld@mail.uc.edu.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: In this project, we found a UC location, went there and took a picture and late we show the picture
# Citations:https://www.geeksforgeeks.org/python-pil-image-open-method/#
# Anything else that's relevant:

from functionsPackage.functions import *

# Read data from json file
data = read_json_file('../EncryptedGroupHints Spring 2023 Section 002.json')


# Access just our groups info:
# print(data['Donte DiVincenzo'])


# plug the data for our team into the convert function
string_list = data['Donte DiVincenzo']


# Call the function to convert the string list to an int list
int_list = convert_strings_to_ints(string_list)


# Fix issue where the first line in .txt is 0 instead of 1 in the list
int_list = [x - 1 for x in int_list]
#print(int_list)


# Define the filename and index_list
filename = '../english.txt'
index_list = int_list


# Call the function to get the corresponding values as a string
value_string = get_values_from_txt_file(filename, index_list)
print(value_string)


# Call the function to display the image
imagefunc('../results.jpeg')
