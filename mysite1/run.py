from bc.admin import RollNoResource

dataset = RollNoResource().export()
text_file=open("output.csv", "w")
text_file.write(dataset.csv)
text_file.close()
