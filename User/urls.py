from django.urls import path
from .views import indexPageView, choiceView, register_applicantView, register_org_adminView, profileView, editprofileView
from .views import viewApplicantsView, viewOrgAdminView, dreamJobView, viewDreamJobView, logoutrequestView, viewOrganizationsView, addOrganizationsView

urlpatterns = [
    path("", indexPageView, name="landing"),
    path("register/", choiceView, name="register"),
    path("register/applicant", register_applicantView, name="register_applicant"),
    path("register/orgadmin", register_org_adminView, name="register_org_admin"), 
    path('profile/', profileView, name='profile'),
    path('editprofile/', editprofileView, name='edit'),
    path('applicants/', viewApplicantsView, name='applicants'),
    path('organizationadmin/', viewOrgAdminView, name='orgadmin'),
    path('logout/', logoutrequestView, name='logout'), 
    path('organizations/', viewOrganizationsView, name='organizations'),
    path('addorganization/', addOrganizationsView, name='addorganization') 
] 