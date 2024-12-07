from django.contrib import admin
from testapp.models import HydJobs
# Register your models here.
class HYDJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HYDJobsAdmin)