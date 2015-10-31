from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
import csv
programme_list = []
string = ""
with open('./bc/input_programmes.csv' , 'r') as csvfile :
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader :
		

		programme_list.append(row)

kuchbhi = ()
for x in range(len(programme_list)):
    kuchbhi = ( (programme_list[x][0],programme_list[x][0]) , ) + kuchbhi

allotment_list = []
string2 = ""
with open('./bc/allotment.csv' , 'r') as csvfile :
  reader = csv.reader(csvfile, delimiter = ',')
  for row in reader :
    

    allotment_list.append(row)
'''
kuchbhi = ()
for x in range(len(programme_list)):
    kuchbhi = ( (programme_list[x][0],programme_list[x][0]) , ) + kuchbhi
'''		
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

def validate_rollno(value):
    if  ((value <= 150000000) | (value >160000000)):
        raise ValidationError('%s is not an appropriate roll no' % value)
'''
def validate_cpi(value):
    if  ((value < 0)| (value >10)):
        raise ValidationError('%s is not an cpi' % value)
'''
class RollNo(models.Model):
    rollno_text = models.IntegerField(validators=[validate_rollno])
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
    choice_5 = models.CharField('Choice5',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_6 = models.CharField('Choice6',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_7 = models.CharField('Choice7',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_8 = models.CharField('Choice8',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_9 = models.CharField('Choice9',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_10 = models.CharField('Choice10',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_11 = models.CharField('Choice11',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_12 = models.CharField('Choice12',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_13 = models.CharField('Choice13',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_14 = models.CharField('Choice14',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_15 = models.CharField('Choice15',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_16 = models.CharField('Choice16',max_length=50,
                                      choices=kuchbhi
                                      )
    choice_17 = models.CharField('Choice17',max_length=50,
                                      choices=kuchbhi
                                      )
    def __str__(self):              # __unicode__ on Python 2
        return self.name_text 
'''
class Choice(models.Model):
  rollno = models.ForeignKey(RollNo)
  choice_1 = models.CharField('Choice1',max_length=50,
                                      choices=kuchbhi
                                      )
'''
'''
class afterAllotment(models.Model):
'''
'''
class finalStats(models.Model): 
 
'''

