from django.contrib import admin

from .models import RollNo


class RollNoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Student Info',               {'fields': ['rollno_text' ,'name_text','cpi','category' , 'current_branch'],'classes': ['collapse']}),
        #('Name', {'fields': ['name_text'], 'classes': ['collapse']}),
        #('CPI',               {'fields': ['cpi'], 'classes': ['collapse']}),
        #('Category', {'fields': ['category'], 'classes': ['collapse']}),
        #('Current Branch', {'fields': ['current_branch'], 'classes': ['collapse']}),
        ('Choices', {'fields': ['choice_1','choice_2','choice_3','choice_4'], 'classes': ['collapse']}),
        #('Choice2', {'fields': ['choice_2'], 'classes': ['collapse']}),
        #('Choice3', {'fields': ['choice_3'], 'classes': ['collapse']}),
        #('Choice4', {'fields': ['choice_4'], 'classes': ['collapse']}),
    ]

admin.site.register(RollNo, RollNoAdmin)