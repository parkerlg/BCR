from django import forms
from .models import Applicant, State, Ethnicity, Organization, Organization_Admin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

TYPE = {
    ('organization_admin', 'Organization Admin'),
    ('applicant', 'Applicant')
}

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
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'test', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'test',
            'id': 'hi',
        }
))

class ApplicantUserForm(UserCreationForm):
    phone = forms.CharField(max_length=10)
    city = forms.CharField(max_length=20)
    zip = forms.CharField(max_length=5)
    state = forms.ModelChoiceField(queryset=State.objects.all())
    ethnicity = forms.ModelChoiceField(queryset=Ethnicity.objects.all())
    country = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20, widget=forms.Select(choices=TYPE))
    bio = forms.CharField(max_length=100)
    #profile_picture = forms.ImageField()
    skills = forms.MultipleChoiceField(choices=SKILLS, widget=forms.SelectMultiple(),)
    website = forms.URLField(max_length=300)
    

    class Meta:
        model = Applicant
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2', 'phone', 'city', 'zip', 'state', 'ethnicity', 'country', 'type', 'bio', 'skills', 'website')

class OrgAdminUserForm(UserCreationForm):
    phone = forms.CharField(max_length=10)
    city = forms.CharField(max_length=20)
    zip = forms.CharField(max_length=5)
    state = forms.ModelChoiceField(queryset=State.objects.all(), initial=0)
    ethnicity = forms.ModelChoiceField(queryset=Ethnicity.objects.all(), initial=0)
    country = forms.CharField(max_length=20)
    type = forms.CharField(max_length=20, widget=forms.Select(choices=TYPE))
    bio = forms.CharField(max_length=20)
    #profile_picture = forms.ImageField()  add a media folder
    title = forms.CharField(max_length=50)
    organization_id = forms.ModelChoiceField(queryset=Organization.objects.all(), initial=0)

    class Meta:
        model = Organization_Admin
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2', 'phone', 'city', 'zip', 'state', 'ethnicity', 'title', 'organization_id', 'type')


class OrganizationForm(forms.ModelForm):
    organization_name = forms.CharField(max_length=40)
    city = forms.CharField(max_length=20)
    state = forms.ModelChoiceField(queryset=State.objects.all(), initial=0)
    email = forms.EmailField(max_length=40)
    size = forms.CharField(max_length=20)
    sector = forms.CharField(max_length=20)

    class Meta:
        model = Organization
        fields = ('organization_name', 'city', 'state', 'email', 'size', 'sector')
