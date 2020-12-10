from django.urls import path
from .views import indexPageView, joblistingPageView, joblistingdetailsPageView, editjoblistingPageView, registerJobListingView, deleteJobListingView, applyView, jobSkillsView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("joblisting/", joblistingPageView, name="job_listing"),
    path("joblistingdetails/<int:joblistingID>/", joblistingdetailsPageView, name="job_listing_details"),
    path("editjoblisting/<int:joblistingID>/", editjoblistingPageView, name="edit_job_listing"),
    path("register/job_listing/", registerJobListingView, name='register_job_listing'),
    path("deletejoblisting/<int:joblistingID>/", deleteJobListingView, name="delete_job_listing"),
    path('apply/', applyView, name='apply'),
    path("jobskills/", jobSkillsView, name='job_skills')
]   