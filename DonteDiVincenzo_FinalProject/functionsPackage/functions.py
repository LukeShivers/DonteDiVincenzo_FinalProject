# functions.py

# Name: Shirin Jain. Patrick Roote, Luke Shivers
# email: jain2ss@mail.uc.edu.edu, rootepr@mail.uc.edu, shiverld@mail.uc.edu.edu
# Assignment Title: Final Project
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: In this project, we found a UC location, went there and took a picture and late we show the picture
# Citations:https://www.geeksforgeeks.org/python-pil-image-open-method/#
# Anything else that's relevant:

import json

# This function reads the contents of the json file and parses it into a Python object
def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


# This function converts the list of strings into a list of ints
def convert_strings_to_ints(string_list):
    int_list = []
    for string in string_list:
        try:
            int_value = int(string)
            int_list.append(int_value)
        except ValueError:
            print(f"String '{string}' is not a valid integer.")
    return int_list


# This function takes the list of ints and index's into the .txt file 
def get_values_from_txt_file(filename, index_list):
    # Read the contents of the .txt file and store it in a variable
    with open(filename, 'r') as file:
        contents = file.read()

    # Convert the contents of the .txt file into a list
    data_list = contents.split()

    # Iterate over the list of integers and use them as indices to access the corresponding values in the list obtained from the .txt file
    value_list = []
    for index in index_list:
        if index < 0 or index >= len(data_list):
            # Check if the index is out of bounds
            print(f"Index {index} is out of bounds.")
        else:
            value = data_list[index]
            value_list.append(value)

    # Return the values obtained as a single string
    return ' '.join(value_list)


# This function shows the picture
from PIL import Image

def imagefunc(image_filename):
    im = Image.open(image_filename)
    im.show()