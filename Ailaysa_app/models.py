from django.db import models
from django.core.validators import MinLengthValidator , MaxLengthValidator
from seller_auth.models import SellerUser


#validate isbn13 min,max length
isbn13_min_length_validator = MinLengthValidator(13, "ISBN-13 must be exactly 13 characters long.") 
isbn13_max_length_validator = MaxLengthValidator(17, "ISBN-13 cannot exceed 17 characters in length.")

#genre model
class Genre(models.Model):
    genre_type = models.CharField(max_length=50,null=False,blank=False)

#language model 
class Language(models.Model):
    language = models.CharField(max_length=100,null=False,blank=False)

#format model
class FormatType(models.Model):
    format_name = models.CharField(max_length=100,unique=True)


class Book(models.Model):
    #mandatory feilds
    
    title = models.CharField(max_length=200)
    genre_id = models.ForeignKey(Genre,on_delete=models.CASCADE,null=False,blank=False) #dropdownList
    language_id = models.ForeignKey(Language,on_delete=models.CASCADE,null=False,blank=False)   #dropdown list
    publisher_id  = models.ForeignKey(SellerUser,on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    isbn10 = models.CharField(max_length=50,unique=True) #International Standard Book NUmber
    isbn13 = models.CharField(max_length=17, validators=[isbn13_min_length_validator, isbn13_max_length_validator])#International Standard Book NUmber
    date_of_publication = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    book_cover = models.ImageField(upload_to='profile_pictures/', blank=False, null=False)
    author_bio = models.TextField(null=True,blank=True)
    summary_of_book = models.TextField()
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords")
    format_id  = models.ForeignKey(FormatType,on_delete=models.CASCADE)  #dropdown list
    
    #non mandatory feilds`
    unit_weight = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True)
    title_in_original_language = models.CharField(max_length=50,null=True)
    co_publisher = models.CharField(max_length=100 ,null=True) 
    winner = models.TextField(null=True)   
    country_of_publication = models.CharField(max_length=100, help_text="Country of publication",null=True) #dropdownlist
    designed_by = models.CharField(max_length=50, blank=True, null=True)
    edited_by = models.CharField(max_length=50, blank=True, null=True)
    translated_by = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.title
    


