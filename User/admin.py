from django.contrib import admin
from .models import Person, State, Ethnicity, Organization, Organization_Admin, Applicant


# Register your models here.
admin.site.register(Person)
admin.site.register(State)
admin.site.register(Ethnicity)
admin.site.register(Organization)
admin.site.register(Organization_Admin)
admin.site.register(Applicant)