from django import forms
from .models import State, Organization, Organization_Admin,  Job_Listing, Job_Application, Applicant

SKILLS = {
    ('ai','Ai'),
    ('ajax','Ajax'),
    ('analytical','Analytical'),
    ('analytics','Analytics'),
    ('android','Android'),
    ('angular','Angular'),
    ('artificial_neural_network','Artificial Neural Network'),
    ('asp_net','Asp Net'),
    ('assembleur','Assembleur'),
    ('assembly','Assembly'),
    ('attention_to_detail','Attention To Detail'),
    ('backend','Backend'),
    ('big_data','Big Data'),
    ('bootstrap','Bootstrap'),
    ('certifications','Certifications'),
    ('cloud_computing','Cloud Computing'),
    ('coaching','Coaching'),
    ('coding','Coding'),
    ('collaboration','Collaboration'),
    ('communication','Communication'),
    ('communication_technologies','Communication Technologies'),
    ('consulting','Consulting'),
    ('content_marketing','Content Marketing'),
    ('control_systems','Control Systems'),
    ('critical_thinking ','Critical Thinking'),
    ('customer_service','Customer Service'),
    ('data_analysis','Data Analysis'),
    ('data_analytics','Data Analytics'),
    ('data_collection','Data Collection'),
    ('data_management','Data Management'),
    ('data_mining','Data Mining'),
    ('data_processing','Data Processing'),
    ('databases','Databases'),
    ('debugging','Debugging'),
    ('deep_learning','Deep Learning'),
    ('design','Design'),
    ('design_patterns','Design Patterns'),
    ('designer','Designer'),
    ('desk','Desk'),
    ('diagnostics','Diagnostics'),
    ('digital_marketing','Digital Marketing'),
    ('documentation','Documentation'),
    ('dom','Dom'),
    ('dos','Dos'),
    ('e_commerce','E Commerce'),
    ('eclipse','Eclipse'),
    ('electronics','Electronics'),
    ('engineering','Engineering'),
    ('ensemble','Ensemble'),
    ('extjs','Extjs'),
    ('fortran','Fortran'),
    ('foundation','Foundation'),
    ('framework','Framework'),
    ('frontend','Frontend'),
    ('git','Git'),
    ('go','Go'),
    ('graphic_design','Graphic Design'),
    ('hadoop','Hadoop'),
    ('hardware','Hardware'),
    ('hive','Hive'),
    ('html','Html'),
    ('http','Http'),
    ('implementation','Implementation'),
    ('innovation','Innovation'),
    ('insights','Insights'),
    ('internet','Internet'),
    ('iphone','Iphone'),
    ('iptables','Iptables'),
    ('javascript','Javascript'),
    ('jquery','Jquery'),
    ('jsp','Jsp'),
    ('leadership','Leadership'),
    ('less','Less'),
    ('linux','Linux'),
    ('lte','Lte'),
    ('machine_learning','Machine Learning'),
    ('mathematics','Mathematics'),
    ('matlab','Matlab'),
    ('maven','Maven'),
    ('mentoring','Mentoring'),
    ('mobile','Mobile'),
    ('modeling','Modeling'),
    ('multitasking','Multitasking'),
    ('network_security','Network Security'),
    ('networks','Networks'),
    ('node_js','Node Js'),
    ('nodejs','Nodejs'),
    ('operating_system','Operating System'),
    ('organizational','Organizational'),
    ('pascal','Pascal'),
    ('penetration_testing','Penetration Testing'),
    ('phonegap','Phonegap'),
    ('php','Php'),
    ('postfix','Postfix'),
    ('powershell','Powershell'),
    ('presentation','Presentation'),
    ('prestashop','Prestashop'),
    ('priorities','Priorities'),
    ('problem_solving','Problem Solving'),
    ('processing','Processing'),
    ('programming','Programming'),
    ('project_management','Project Management'),
    ('project_manager','Project Manager'),
    ('prototyping','Prototyping'),
    ('python','Python'),
    ('renewable_energy','Renewable Energy'),
    ('reporting','Reporting'),
    ('reporting_tools','Reporting Tools'),
    ('sas','Sas'),
    ('scrum','Scrum'),
    ('sencha_touch','Sencha Touch'),
    ('shiny','Shiny'),
    ('social_media_marketing','Social Media Marketing'),
    ('software_development','Software Development'),
    ('solution_development','Solution Development'),
    ('spark','Spark'),
    ('sql','Sql'),
    ('sql_server','Sql Server'),
    ('statistical_analysis','Statistical Analysis'),
    ('svg','Svg'),
    ('swing','Swing'),
    ('tableau','Tableau'),
    ('teamwork','Teamwork'),
    ('tech_support','Tech Support'),
    ('technical','Technical'),
    ('telecom','Telecom'),
    ('time_management','Time Management'),
    ('training','Training'),
    ('troubleshooting','Troubleshooting'),
    ('vb_net','Vb Net'),
    ('visio','Visio'),
    ('volleyball','Volleyball'),
    ('web_analytics','Web Analytics'),
    ('web_development','Web Development'),
    ('web_services','Web Services'),
    ('website_development','Website Development'),
    ('wimax','Wimax'),
    ('windows','Windows'),
    ('word','Word'),
    ('wordpress','Wordpress')
}
class JobListingForm(forms.ModelForm):
    city = forms.CharField(max_length=30)
    state_id = forms.ModelChoiceField(queryset=State.objects.all())
    job_title = forms.CharField(max_length=20)
    org_admin_id = forms.ModelChoiceField(queryset=Organization_Admin.objects.all())
    contracts = forms.CharField(max_length=30)
    description = forms.CharField(max_length=30)
    skills = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SKILLS)
    # total_skills = forms.IntegerField()
    # skill_value_rating = forms.IntegerField()
    skills = forms.MultipleChoiceField(choices=SKILLS, widget=forms.SelectMultiple(),)
    external_app_link = forms.CharField(max_length=50)
    organization_id = forms.ModelChoiceField(queryset=Organization.objects.all())

    class Meta:
        model = Job_Listing
        fields = ['city', 'state_id', 'job_title', 'org_admin_id', 'contracts', 'description', 'skills', 'organization_id']


class ApplicationForm(forms.ModelForm):
    application_name = forms.CharField(max_length=30)
    # resume = forms.FileField()
    # citizen = forms.IntegerField(label='Are you a citizen of the United States?', required=False)
    # authorized = forms.CheckboxInput(required=False)
    # felony = forms.CheckboxInput(required=False)
    # felony_desc = forms.CharField(max_length=30, label='Description of Felony', required=False)
    # start_date = forms.DateTimeField()
    orgization_id = forms.ModelChoiceField(queryset=Organization.objects.all(), label='Organization')
    applicant_id = forms.ModelChoiceField(queryset=Applicant.objects.all())
    job_listing_id = forms.ModelChoiceField(queryset=Job_Listing.objects.all())

    class Meta:
        model = Job_Application
        fields = ['application_name', 'orgization_id', 'applicant_id', 'job_listing_id']

