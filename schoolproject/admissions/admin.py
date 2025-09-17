from django.contrib import admin
from admissions.models import student

# Register your models here.


class studentadmin(admin.ModelAdmin):
 list_display=['name','fathername','classname','contact']
admin.site.register(student,studentadmin)

 
