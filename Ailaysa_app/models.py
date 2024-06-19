from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator

# Create your models here.
class Book(models.Model):
    #mandatory feilds
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)   #dropdown list
    isbn13 = models.CharField(max_length=13, unique=True , validators=[MinLengthValidator(13), MaxLengthValidator(13)])
    isbn10 = models.BigIntegerField(max_length=10 , unique=True, validators=[MinLengthValidator(10),MaxLengthValidator(10)])
    genre = models.CharField(max_length=50)     #dropdown list
    date_of_publication = models.DateField()
    number_of_pages = models.IntegerField()
    book_cover = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    about_author = models.TextField()
    summary_of_book = models.TextField()
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords")
    format = models.CharField(max_length=50)   #dropdown list
    
    #non mandatory feilds
    unit_weight = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    title_in_original_language = models.CharField(max_length=50,null=True)
    co_publisher = models.CharField(max_length=100 ,null=True) 
    winner = models.TextField(null=True)   
    short_listed = models.TextField(null=True)
    status = models.CharField(max_length=100 , null=True)  #dropdown list
    overall_height = models.FloatField(verbose_name="Overall Height (cm)",null=True)
    overall_width = models.FloatField(verbose_name="Overall Width (cm)",null=True)
    overall_thickness = models.FloatField(verbose_name="Overall Thickness (cm)", null=True)
    page_trim_height = models.FloatField(verbose_name="Page Trim Height (cm)", null=True)
    page_trim_width = models.FloatField(verbose_name="Page Trim Width (cm)", null=True)
    publisher_website = models.URLField(max_length=200, blank=True, null=True, help_text="Publisher's website URL")
    country_of_publication = models.CharField(max_length=100, help_text="Country of publication",null=True) #dropdownlist
    designed_by = models.CharField(max_length=50, blank=True, null=True)
    edited_by = models.CharField(max_length=50, blank=True, null=True)
    illustrated_by = models.CharField(max_length=50, blank=True, null=True)
    translated_by = models.CharField(max_length=50, blank=True, null=True)
    
    
    
    # LANGUAGE_CHOICES = [
    #     ('en', 'English'),
    #     ('es', 'Spanish'),
    #     ('fr', 'French'),
    #     ('de', 'German'),
    #     # Add more languages as needed
    # ]

    # language = models.CharField( max_length=2, choices=LANGUAGE_CHOICES,default='en',)