from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
import csv
programme_list = []
string = ""
programme_strength = []
with open('./bc/input_programmes.csv' , 'r') as csvfile :
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader :
		

		programme_list.append(row)

kuchbhi = ()
for x in range(len(programme_list)):
    kuchbhi = ( (programme_list[x][0],programme_list[x][0]) , ) + kuchbhi
		
'''
class Programme(models.Model):
    
    kuchbhi = ()
    for x in range(len(programme_list)):
    	kuchbhi = ( (programme_list[x][0],programme_list[x][0]) , ) + kuchbhi
    programme_text = models.CharField(max_length=50,
                                      choices=kuchbhi,
                                      )

'''
category_choices =(
		('1','General'),
		('2','OBC'),
		('3','SC'),
		('4','ST'),
		('5','General-PD'),
		('6','OBC-PD'),
		('7','SC-PD'),
		('8','ST-PD'),
		)

class RollNo(models.Model):
    rollno_text = models.CharField(max_length=9)
    name_text = models.CharField(max_length=200)

    current_branch =  models.CharField(max_length=50,
                                      choices=kuchbhi
                                      )
    cpi = models.DecimalField('CPI', max_digits=4, decimal_places=2)
    category = models.CharField('CATEGORY',max_length=50,
                                choices= category_choices
                                )
    
    choice_1 = models.CharField('Choice1',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_2 = models.CharField('Choice2',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_3 = models.CharField('Choice3',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_4 = models.CharField('Choice4',max_length=50,
                                      choices=kuchbhi
                                      )
	
    def __str__(self):              # __unicode__ on Python 2
        return self.rollno_text+" "+self.name_text 
'''
class Choice(models.Model):
	roll_no = models.ForeignKey(RollNo)
    choice = models.CharField(max_length=50,
                                      choices=kuchbhi
                                      )
'''
'''
class afterAllotment(models.Model):
'''
'''
class finalStats(models.Model): 
 
'''

