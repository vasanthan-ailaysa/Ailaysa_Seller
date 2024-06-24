from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# validate isbn13 min,max length
isbn13_min_length_validator = MinLengthValidator(13, "ISBN-13 must be exactly 13 characters long.")
isbn13_max_length_validator = MaxLengthValidator(17, "ISBN-13 cannot exceed 17 characters in length.")

# validate isbn10 min,max length
isbn10_min_length_validator = MinLengthValidator(10, "ISBN-10 must be exactly 10 characters long.")
isbn10_max_length_validator = MaxLengthValidator(10, "ISBN-10 cannot exceed 10 characters in length.")


# genre model
class Genre(models.Model):
    genre = models.CharField(max_length=50, null=False, blank=False)


# language model
class Language(models.Model):
    language = models.CharField(max_length=100, null=False, blank=False)


class Author(models.Model):
    """
    Author model class
    """
    name = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """
    Publisher model class
    """
    name = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model class
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False, related_name='books', related_query_name='book')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=False, blank=False, related_name='books', related_query_name='book')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, blank=False)  # dropdown list
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False, blank=False)  # dropdownList
    isbn10 = models.CharField(max_length=10, unique=True, validators=[isbn10_min_length_validator,
                                                                      isbn10_max_length_validator])  # International Standard Book NUmber
    isbn13 = models.CharField(max_length=17, unique=True, validators=[isbn13_min_length_validator,
                                                                      isbn13_max_length_validator])  # International Standard Book NUmber
    date_of_publication = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    book_cover = models.ImageField(upload_to='profile_pictures/', blank=False, null=False)
    author_bio = models.TextField(null=True, blank=True)
    summary_of_book = models.TextField()
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords")
    # format = models.ForeignKey(FormatType, on_delete=models.CASCADE)  # uses choices

    # non-mandatory fields
    unit_weight = models.IntegerField(null=True, blank=True)
    title_in_original_language = models.CharField(max_length=50, null=True)
    co_publisher = models.CharField(max_length=100, null=True)
    winner = models.TextField(null=True)
    country_of_publication = models.CharField(max_length=100, help_text="Country of publication", null=True)
    designed_by = models.CharField(max_length=50, blank=True, null=True)
    edited_by = models.CharField(max_length=50, blank=True, null=True)
    translated_by = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
