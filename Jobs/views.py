from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Job_Listing, Job_Offer, Job_Application
from User.models import Person, Applicant, Organization_Admin
from .forms import JobListingForm, ApplicationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def indexPageView(request) :
    return HttpResponse("Hello")

def joblistingPageView(request) :
    data = Job_Listing.objects.all()

    context = {
        "joblisting" : data
    }
    return render(request, "Jobs/job_listing.html", context)

def joblistingdetailsPageView(request, joblistingID) :
    data = Job_Listing.objects.get(id=joblistingID)

    context = {
        "joblisting" : data
    }

    return render(request, 'Jobs/job_listing_details.html', context)

def editjoblistingPageView(request, joblistingID) :
    data = Job_Listing.objects.get(id=joblistingID)

    context = {
        "joblisting" : data
    }

    return render(request, 'Jobs/edit_job_listing.html', context)

def registerJobListingView(request) :
    form = JobListingForm(request.POST or None)
    if request.method == 'POST' :
        form = JobListingForm(request.POST)
        if form.is_valid() :
            form.save()
            data = Job_Listing.objects.all
            context = {
                "joblisting" : data
            }
            return render(request, 'Jobs/job_listing.html', context)
    context = {
        'form': form
    }
    return render(request, 'Jobs/add_job_listing.html', context)

def deleteJobListingView(request, joblistingID) :
    joblisting = Job_Listing.objects.get(id=joblistingID)
    joblisting.delete()
    data = Job_Listing.objects.all()

    context = {
        "joblisting" : data
    }

    return render(request, "jobs/job_listing.html", context)

def applyView(request):
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST' :
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid() :
            #handle_uploaded_file(request.FILES['resume'])
            form.save()
            currentuser = request.user
            user = authenticate(request, credentials=currentuser)
            person = Person.objects.get(username=currentuser.username)
            if person.type=='applicant':
                applicant = Applicant.objects.get(id = currentuser.id)
                context = {
                    'user' : applicant,
                }
            else:
                orgadmin = Organization_Admin.objects.get(id = currentuser.id)
                context = {
                    'user' : orgadmin,
                }
            return render(request, 'User/profile.html', context)
    context = {
        'form': form
    }
    return render(request, "Jobs/apply.html", context)

def jobSkillsView(request):
    return render(request, "User/job_skills.html")