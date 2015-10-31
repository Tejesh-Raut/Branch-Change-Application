from django import forms
from .models import RollNo

class RollForm(forms.ModelForm):

    class Meta:
        model = RollNo
        fields = ('rollno_text', 'name_text','cpi','category' , 'current_branch','choice_1','choice_2','choice_3','choice_4','choice_5','choice_6','choice_7','choice_8','choice_9','choice_10','choice_11','choice_12','choice_13','choice_14','choice_15','choice_16','choice_17')

    

    
        