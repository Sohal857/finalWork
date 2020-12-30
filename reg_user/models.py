from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
# Create your models here.
class UserProfileInfo(models.Model):
    CHOICES = (
        ('Australia', (
            ('A1', 'Australian Capital Territory'),
            ('A2', 'Northern Territory'),
            ('A3', 'State of New South Wales'),
            ('A4', 'State of Queensland'),
            ('A5', 'State of South Australia'),
            ('A6', 'State of Tasmania'),
            ('A7', 'State of Victoria'),
            ('A8', 'State of Western Australia'),
        )),
        ('Bangladesh', (
            ('B1', 'Barisal Division'),
            ('B2', 'Chittagong Division'),
            ('B3', 'Dhaka Division'),
            ('B4', 'Khulna Division'),
            ('B5', 'Mymensingh Division'),
            ('B6', 'Rajshahi Division'),
            ('B7', 'Rangpur Division'),
            ('B8', 'Sylhet Division'),
        )),
        ('Canada', (
            ('C1', 'Alberta'),
            ('C2', 'British Columbia'),
            ('C3', 'Manitoba'),
            ('C4', 'New Brunswick/Nouveau-Brunswick'),
            ('C5', 'Newfoundland and Labrador'),
            ('C6', 'Northwest Territories'),
            ('C7', 'Nova Scotia'),
            ('C8', 'Nunavut'),
            ('C9', 'Ontario'),
            ('C10', 'Prince Edward Island'),
            ('C11', 'Quebec'),
            ('C12', 'Saskatchewan'),
            ('C13', 'Yukon'),
        )),
        ('USA', (
            ('US1',"Alabama"),
            ('US2',"Alaska"),
            ('US3',"Arizona"),
            ('US4',"Arkansas"),
            ('US5',"California"),
            ('US6',"Colorado"),
            ('US7',"Connecticut"),
            ('US8',"Delaware"),
            ('US9',"District of Columbia"),
            ('US10',"Florida"),
            ('US11',"Georgia"),
            ('US12',"Hawaii"),
            ('US13',"Idaho"),
            ('US14',"Illinois"),
            ('US15',"Indiana"),
            ('US16',"Iowa"),
            ('US17',"Kansas"),
            ('US18',"Kentucky"),
            ('US19',"Louisiana"),
            ('US20',"Maine"),
            ('US21',"Maryland"),
            ('US22',"Massachusetts"),
            ('US23',"Michigan"),
            ('US24',"Minnesota"),
            ('US25',"Mississippi"),
            ('US26',"Missouri"),
            ('US27',"Montana"),
            ('US28',"Nebraska"),
            ('US29',"Nevada"),
            ('US30',"New Hampshire"),
            ('US31',"New Jersey"),
            ('US32',"New Mexico"),
            ('US33',"New York"),
            ('US34',"North Carolina"),
            ('US35',"North Dakota"),
            ('US36',"Ohio"),
            ('US37',"Oklahoma"),
            ('US38',"Oregon"),
            ('US39',"Pennsylvania"),
            ('US40',"Rhode Island"),
            ('US41',"South Carolina"),
            ('US42',"South Dakota"),
            ('US43',"Tennessee"),
            ('US44',"Texas"),
            ('US45',"Utah"),
            ('US46',"Vermont"),
            ('US47',"Virginia"),
            ('US48',"Washington"),
            ('US49',"West Virginia"),
            ('US50',"Wisconsin"),
            ('US51',"Wyoming"),

        )),
    )

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, default = '')
    first_name = models.CharField(max_length=50, default = '')
    last_name = models.CharField(max_length=50, default = '')
    email = models.EmailField(max_length=70, default = '')
    website = models.URLField(max_length = 200, default = '', blank=True, null= True)
    company = models.CharField(max_length = 200, default = '')
    phone_number = PhoneNumberField(default = '')
    unit = models.CharField(max_length = 100,  default = '')
    street_number = models.CharField(max_length = 50,  default = '')
    street_name = models.CharField(max_length = 50, default = '')
    city = models.CharField(max_length = 50, default = '')
    state = models.CharField(max_length = 50, choices = CHOICES)
    zip_code = models.CharField(max_length = 50, default = '')
    country = CountryField()
    def __str__(self):
        return self.user.username
