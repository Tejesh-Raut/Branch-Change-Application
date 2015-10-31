from django.contrib import admin
from bc.models import RollNo
from import_export import resources
from import_export.admin import ImportExportModelAdmin
'''
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; "filename=hellyo.csv"'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Roll Number"),
        smart_str(u"Name"),
        smart_str(u"CPI"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.rollno_text),
            smart_str(obj.name_text),
            smart_str(obj.cpi),

        ])
    return response
export_csv.short_description = u"Export CSV"
'''


class RollNoResource(resources.ModelResource):

    class Meta:
        model = RollNo
        

class RollAdmin(ImportExportModelAdmin):
    resource_class = RollNoResource
    pass


admin.site.register(RollNo, RollAdmin)
