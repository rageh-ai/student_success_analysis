import json

with open('predict-students-dropout-and-academic-success-metadata.json', "r") as json_file:
    data = json.load(json_file)

i = 0

record = data['recordSet'][0]
record = record['field']

with open('encoded_descriptions.txt', "w") as output_file:
    for rec in record:
        column_name = rec['source']['extract']['column']
        desc = rec['description']
        output_file.write(f'Column: {column_name} \n Description: {desc} \n')

        