from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class State(models.Model) :
    state_name = models.CharField(max_length=20)
    state_abbrev = models.CharField(max_length =2)

    def __str__ (self) :
        return(self.state_name)

class Ethnicity(models.Model) :
    ethnicity_name = models.CharField(max_length=30)

    def __str__ (self) :
        return(self.ethnicity_name)

class Person (User) :
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=5)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    bio = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='pictures')

    def __str__ (self):
        return(self.first_name + " " +self.last_name)
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Person'

class Organization(models.Model):
    organization_name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    email = models.EmailField(max_length=40)
    size = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)

    def __str__ (self):
        return self.organization_name

class Organization_Admin(Person):
    title = models.CharField(max_length=20)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__ (self):
        return(self.first_name + " " +self.last_name)

    class Meta:
        verbose_name = 'Organization Admin'
        verbose_name_plural = 'Organization Admin'



class Applicant(Person):
    website = models.CharField(max_length=35)
    skills = models.CharField(max_length=1000)

    # skill_ai = models.IntegerField(default=0)
    # skill_ajax = models.IntegerField(default=0)
    # skill_analytical = models.IntegerField(default=0)
    # skill_analytics = models.IntegerField(default=0)
    # skill_android = models.IntegerField(default=0)
    # skill_angular = models.IntegerField(default=0)
    # skill_artificial_neural_network = models.IntegerField(default=0)
    # skill_asp_net = models.IntegerField(default=0)
    # skill_assembleur = models.IntegerField(default=0)
    # skill_assembly = models.IntegerField(default=0)
    # skill_attention_to_detail = models.IntegerField(default=0)
    # skill_backend = models.IntegerField(default=0)
    # skill_big_data = models.IntegerField(default=0)
    # skill_bootstrap = models.IntegerField(default=0)
    # skill_certifications = models.IntegerField(default=0)
    # skill_cloud_computing = models.IntegerField(default=0)
    # skill_coaching = models.IntegerField(default=0)
    # skill_coding = models.IntegerField(default=0)
    # skill_collaboration = models.IntegerField(default=0)
    # skill_communication = models.IntegerField(default=0)
    # skill_communication_technologies = models.IntegerField(default=0)
    # skill_consulting = models.IntegerField(default=0)
    # skill_content_marketing = models.IntegerField(default=0)
    # skill_control_systems = models.IntegerField(default=0)
    # skill_critical_thinking = models.IntegerField(default=0)
    # skill_customer_service = models.IntegerField(default=0)
    # skill_data_analysis = models.IntegerField(default=0)
    # skill_data_analytics = models.IntegerField(default=0)
    # skill_data_collection = models.IntegerField(default=0)
    # skill_data_management = models.IntegerField(default=0)
    # skill_data_mining = models.IntegerField(default=0)
    # skill_data_processing = models.IntegerField(default=0)
    # skill_databases = models.IntegerField(default=0)
    # skill_debugging = models.IntegerField(default=0)
    # skill_deep_learning = models.IntegerField(default=0)
    # skill_design = models.IntegerField(default=0)
    # skill_design_patterns = models.IntegerField(default=0)
    # skill_designer = models.IntegerField(default=0)
    # skill_desk = models.IntegerField(default=0)
    # skill_diagnostics = models.IntegerField(default=0)
    # skill_digital_marketing = models.IntegerField(default=0)
    # skill_documentation = models.IntegerField(default=0)
    # skill_dom = models.IntegerField(default=0)
    # skill_dos = models.IntegerField(default=0)
    # skill_e_commerce = models.IntegerField(default=0)
    # skill_eclipse = models.IntegerField(default=0)
    # skill_electronics = models.IntegerField(default=0)
    # skill_engineering = models.IntegerField(default=0)
    # skill_ensemble = models.IntegerField(default=0)
    # skill_extjs = models.IntegerField(default=0)
    # skill_fortran = models.IntegerField(default=0)
    # skill_foundation = models.IntegerField(default=0)
    # skill_framework = models.IntegerField(default=0)
    # skill_frontend = models.IntegerField(default=0)
    # skill_git = models.IntegerField(default=0)
    # skill_go = models.IntegerField(default=0)
    # skill_graphic_design = models.IntegerField(default=0)
    # skill_hadoop = models.IntegerField(default=0)
    # skill_hardware = models.IntegerField(default=0)
    # skill_hive = models.IntegerField(default=0)
    # skill_html = models.IntegerField(default=0)
    # skill_http = models.IntegerField(default=0)
    # skill_implementation = models.IntegerField(default=0)
    # skill_innovation = models.IntegerField(default=0)
    # skill_insights = models.IntegerField(default=0)
    # skill_internet = models.IntegerField(default=0)
    # skill_iphone = models.IntegerField(default=0)
    # skill_iptables = models.IntegerField(default=0)
    # skill_javascript = models.IntegerField(default=0)
    # skill_jquery = models.IntegerField(default=0)
    # skill_jsp = models.IntegerField(default=0)
    # skill_leadership = models.IntegerField(default=0)
    # skill_less = models.IntegerField(default=0)
    # skill_linux = models.IntegerField(default=0)
    # skill_lte = models.IntegerField(default=0)
    # skill_machine_learning = models.IntegerField(default=0)
    # skill_mathematics = models.IntegerField(default=0)
    # skill_matlab = models.IntegerField(default=0)
    # skill_maven = models.IntegerField(default=0)
    # skill_mentoring = models.IntegerField(default=0)
    # skill_mobile = models.IntegerField(default=0)
    # skill_modeling = models.IntegerField(default=0)
    # skill_multitasking = models.IntegerField(default=0)
    # skill_network_security = models.IntegerField(default=0)
    # skill_networks = models.IntegerField(default=0)
    # skill_node_js = models.IntegerField(default=0)
    # skill_nodejs = models.IntegerField(default=0)
    # skill_operating_system = models.IntegerField(default=0)
    # skill_organizational = models.IntegerField(default=0)
    # skill_pascal = models.IntegerField(default=0)
    # skill_penetration_testing = models.IntegerField(default=0)
    # skill_phonegap = models.IntegerField(default=0)
    # skill_php = models.IntegerField(default=0)
    # skill_postfix = models.IntegerField(default=0)
    # skill_powershell = models.IntegerField(default=0)
    # skill_presentation = models.IntegerField(default=0)
    # skill_prestashop = models.IntegerField(default=0)
    # skill_priorities = models.IntegerField(default=0)
    # skill_problem_solving = models.IntegerField(default=0)
    # skill_processing = models.IntegerField(default=0)
    # skill_programming = models.IntegerField(default=0)
    # skill_project_management = models.IntegerField(default=0)
    # skill_project_manager = models.IntegerField(default=0)
    # skill_prototyping = models.IntegerField(default=0)
    # skill_python = models.IntegerField(default=0)
    # skill_renewable_energy = models.IntegerField(default=0)
    # skill_reporting = models.IntegerField(default=0)
    # skill_reporting_tools = models.IntegerField(default=0)
    # skill_sas = models.IntegerField(default=0)
    # skill_scrum = models.IntegerField(default=0)
    # skill_sencha_touch = models.IntegerField(default=0)
    # skill_shiny = models.IntegerField(default=0)
    # skill_social_media_marketing = models.IntegerField(default=0)
    # skill_software_development = models.IntegerField(default=0)
    # skill_solution_development = models.IntegerField(default=0)
    # skill_spark = models.IntegerField(default=0)
    # skill_sql = models.IntegerField(default=0)
    # skill_sql_server = models.IntegerField(default=0)
    # skill_statistical_analysis = models.IntegerField(default=0)
    # skill_svg = models.IntegerField(default=0)
    # skill_swing = models.IntegerField(default=0)
    # skill_tableau = models.IntegerField(default=0)
    # skill_teamwork = models.IntegerField(default=0)
    # skill_tech_support = models.IntegerField(default=0)
    # skill_technical = models.IntegerField(default=0)
    # skill_telecom = models.IntegerField(default=0)
    # skill_time_management = models.IntegerField(default=0)
    # skill_training = models.IntegerField(default=0)
    # skill_troubleshooting = models.IntegerField(default=0)
    # skill_vb_net = models.IntegerField(default=0)
    # skill_visio = models.IntegerField(default=0)
    # skill_volleyball = models.IntegerField(default=0)
    # skill_web_analytics = models.IntegerField(default=0)
    # skill_web_development = models.IntegerField(default=0)
    # skill_web_services = models.IntegerField(default=0)
    # skill_website_development = models.IntegerField(default=0)
    # skill_wimax = models.IntegerField(default=0)
    # skill_windows = models.IntegerField(default=0)
    # skill_word = models.IntegerField(default=0)
    # skill_wordpress = models.IntegerField(default=0)

    def __str__ (self):
        return(self.first_name + " " +self.last_name)

    class Meta:
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'


