from django.db import models

choice_age=(
    ("Male","Male"),
    ("female","female")
)
# Create your models here.
class filldetails(models.Model):

    uniq =  models.IntegerField()
    unique_HR =  models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(choices=choice_age, max_length=100, default='Male' )
    country = models.CharField(max_length=100, default='India' )
    state = models.CharField(max_length=100, default='Maharashtra' )
    self_employed = models.CharField(max_length=100, default='Under Investigation' )
    family_history = models.CharField( max_length=100, default='NaN')
    treatment = models.CharField( max_length=100, default='NaN')
    work_interfere = models.CharField( max_length=100, default='NaN')
    no_employees = models.CharField( max_length=100, default='NaN')
    remote_work = models.CharField( max_length=100, default='NaN')
    tech_company = models.CharField( max_length=100, default='NaN')
    benefits = models.CharField( max_length=100, default='NaN')
    care_options = models.CharField( max_length=100, default='NaN')
    wellness_program = models.CharField( max_length=100, default='NaN')
    seek_help = models.CharField( max_length=100, default='NaN')
    anonimity = models.CharField( max_length=100, default='NaN')
    leave = models.CharField( max_length=100, default='NaN')
    mental_health_consequence = models.CharField( max_length=100, default='NaN')
    phys_health_consequence =models.CharField( max_length=100, default='NaN')
    coworkers =models.CharField( max_length=100, default='NaN')
    supervisor =models.CharField( max_length=100, default='NaN')
    mental_health_interview = models.CharField( max_length=100, default='NaN')
    phys_health_interview = models.CharField( max_length=100, default='NaN')
    mental_vs_physical = models.CharField( max_length=100, default='NaN')
    obs_consequence = models.CharField( max_length=100, default='NaN')
    comments = models.TextField()


    def __str__(self):
        return str(self.unique_id)

# Create your models here.
class Document(models.Model):
    csvfile1 = models.FileField(upload_to='documents/%Y/%m/%d')
