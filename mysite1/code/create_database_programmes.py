import sys, csv

table_input_programme = []
with open('input_programmes.csv', 'r') as fp:
    csv_fp = csv.reader(fp)
    table_input_programme = list(csv_fp)

num_rows_programme = len(table_input_programme)
table_programme = []
temp_list = []
beta = 0.25
alpha = 0.10
beta1 = 0
alpha1 =0
sanctioned_strength = 0
for i in range (0, num_rows_programme):
	temp_list.append(table_input_programme[i][0])
	sanctioned_strength = float(table_input_programme[i][1])
	beta1 = round( (1.0 - beta)*sanctioned_strength )
	alpha1 = round( (1.0 + alpha)*sanctioned_strength )
	temp_list.append(beta1)
	temp_list.append(alpha1)
	temp_list.append(table_input_programme[i][2])
	table_programme.append(temp_list)
	temp_list = []

#created a database for programmes with column 1 representing name, column 2 the minimun strength,
#column 3 the max strentgth and colmn 4 the current strength of the department
'''
fl = open('output.csv', 'w')
writer = csv.writer(fl)
for values in table_programme:
	writer.writerow(values)
fl.close()
'''
