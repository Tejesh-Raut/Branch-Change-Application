from django import forms

from .models import RollNo

class RollForm(forms.ModelForm):

    class Meta:
        model = RollNo
        fields = ('rollno_text', 'name_text','cpi','category' , 'current_branch','choice_1','choice_2','choice_3','choice_4')