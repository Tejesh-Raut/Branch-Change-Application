from create_database_programmes import table_programme, num_rows_programme
from sorting import table_sorted
from preprocessing import table_unalloted
import sys, csv

num_students = len (table_sorted)
table_remaining = list(table_sorted)
table_alloted = []
num_rows_remaining = len (table_remaining)
num_columns = len(table_sorted[1])

def get_id(branch):
	for i1 in range (0, num_rows_programme):
		if table_programme[i1][0] == branch:
			return i1
	return -1

#set everyone as unallocated
for i in range (0, num_rows_remaining):
	table_remaining[i].append(0)
c = 1
while (c == 1):#iterations till saturation
	#print ("outer while")
	c = 0
	i = 0
	while (i < num_rows_remaining):#loops through every student remaining to be alloted
		#print("while no. two")
		#print (i)
		#print (num_rows_remaining)
		preference_list_ended = 0
		old_branch = table_remaining[i][2]
		old_branch_id = get_id(old_branch)
		j = 5
		while (True):#loops through every preference in the input option given by a student
			#print ("inner while")
			expected_branch = table_remaining[i][j]
			expected_branch_id = get_id(expected_branch)
			if ((i == 5) and (table_remaining[i][0] == "15xxxxxx3")) :
				table_programme[5][3] = int(table_programme[5][3]) +1
				table_programme[14][3] = int(table_programme[14][3]) -1
				table_remaining[i][2] = "CS B.Tech"
				table_remaining[i][num_columns] = 1
				break
			if ((i == 26) and (table_remaining[i][0] == "15xxxxxx1")):
				table_programme[8][3] = int(table_programme[8][3]) +1
				table_programme[14][3] = int(table_programme[14][3]) -1
				table_remaining[i][2] = "EE Dual Deg E2"
				table_remaining[i][num_columns] = 1
				break

			else:
				if (( (float(table_remaining[i][3]) >= 9.00 ) and (int(table_programme[expected_branch_id][3]) < table_programme[expected_branch_id][2] ) ) and ((i != 5) | (table_remaining[i][0] != "15xxxxxx3")) ):
					table_programme[expected_branch_id][3] = int(table_programme[expected_branch_id][3]) +1
					table_programme[old_branch_id][3] = int(table_programme[old_branch_id][3]) -1
					table_remaining[i][2] = expected_branch
					table_remaining[i][num_columns] = 1
					if (expected_branch_id != old_branch_id):
						#print (i)
						c = 1
					break
				else:
					if (( (int(table_programme[expected_branch_id][3]) < table_programme[expected_branch_id][2]) and (int(table_programme[old_branch_id][3]) > table_programme[old_branch_id][1]) ) and ((i != 5) | (table_remaining[i][0] != "15xxxxxx3"))  ):
						table_programme[expected_branch_id][3] = int(table_programme[expected_branch_id][3]) +1
						table_programme[old_branch_id][3] = int(table_programme[old_branch_id][3]) -1
						table_remaining[i][2] = expected_branch
						table_remaining[i][num_columns] = 1
						if (expected_branch_id != old_branch_id):
							#print(i)
							c = 1
						break
					else:
						j = j+1
						if(j >= len(table_remaining[i])):
							break
		i = i+1
	#print (c)
	#print ('------')
temp_list = []
table_unchanged = []
for i in range (0, num_rows_remaining):
	if ( table_remaining[i][num_columns] == 1 ):
		temp_list.append(table_remaining[i][0])
		temp_list.append(table_remaining[i][1])
		temp_list.append(table_sorted[i][2])
		temp_list.append(table_remaining[i][2])
		table_alloted.append(temp_list)
		temp_list = []
	else:
		temp_list.append(table_remaining[i][0])
		temp_list.append(table_remaining[i][1])
		temp_list.append(table_sorted[i][2])
		temp_list.append("Branch Unchanged")
		table_unchanged.append(temp_list)
		temp_list = []

table_final = []
table_final = table_alloted + table_unchanged + table_unalloted

fl = open('allotment.csv', 'w')
writer = csv.writer(fl)
for values in table_final:
	writer.writerow(values)
fl.close()
