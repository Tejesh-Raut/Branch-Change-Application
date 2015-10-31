import sys, csv

table_input = []
with open('input_options.csv', 'r') as f1:
    csv_f1 = csv.reader(f1)
    table_input = list(csv_f1)
num_rows = len(table_input)
num_cols = 0
for i in range (0, num_rows):
	if num_cols < len(table_input[i]):
		num_cols = len(table_input[i])
table_preprocessed = []
table_unalloted = []
temp_list = []
str_unalloted = "Ineligible"
for i in range (0, num_rows):
	if float(table_input[i][3]) >= 8.00:
		table_preprocessed.append(table_input[i])
	else:
		if ((float(table_input[i][3]) >= 7.00) and ( ( ( table_input[i][4] == "SC" ) | ( table_input[i][4] == "ST" ) ) | ( table_input[i][4] == "PwD" ) ) ):
			table_preprocessed.append(table_input[i])
		else:
			temp_list.append(table_input[i][0])
			temp_list.append(table_input[i][1])
			temp_list.append(table_input[i][2])
			temp_list.append(str_unalloted)
			table_unalloted.append(temp_list)
			temp_list = []
