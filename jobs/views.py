from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def jobs(request):
    #Render the jobs.html template
    return render(request, "jobs.html")  
