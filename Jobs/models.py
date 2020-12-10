from django.db import models
from User.models import Organization, State, Organization_Admin, Applicant
# Create your models here.

class Job_Listing (models.Model):
    city = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=40)
    org_admin_id = models.ForeignKey(Organization_Admin, on_delete=models.CASCADE)
    contracts = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    total_skills = models.IntegerField()
    skill_value_rating = models.IntegerField()
    external_app_link = models.CharField(max_length=50, null=True, blank=True)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return(self.job_title)

class Job_Application (models.Model):
    #figure out where to upload to
    application_name = models.CharField(max_length=30)
    resume = models.FileField(upload_to='Resumes')
    citizen = models.IntegerField(verbose_name='Are you a citizen of the United States?')
    authorized = models.IntegerField(verbose_name='Are you authorized to work in the US?')
    felony = models.IntegerField(verbose_name='Have you been convicted of a felony?')
    felony_desc = models.CharField(max_length=30, verbose_name='Description of Felony')
    start_date = models.DateField(verbose_name='Date available to start working')
    orgization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)

    def __str__(self):
        return(self.application_name)

class Job_Offer (models.Model):
    city = models.CharField(max_length=30)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=30)
    contracts = models.CharField(max_length=30)
    matching_skills = models.IntegerField()
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)
    total_skills = models.IntegerField()

    def __str__(self):
        return(self.job_title)



    