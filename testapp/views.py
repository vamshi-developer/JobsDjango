from django.shortcuts import render
from testapp.models import HydJobs
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/index.html')

def hyd_jobs_view(request):
    jobs_list=HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})