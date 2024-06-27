from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# validate isbn13 min,max length
isbn13_min_length_validator = MinLengthValidator(13, "ISBN-13 must be exactly 13 characters long.")
isbn13_max_length_validator = MaxLengthValidator(17, "ISBN-13 cannot exceed 17 characters in length.")

# validate isbn10 min,max length
isbn10_min_length_validator = MinLengthValidator(10, "ISBN-10 must be exactly 10 characters long.")
isbn10_max_length_validator = MaxLengthValidator(10, "ISBN-10 cannot exceed 10 characters in length.")


class Language(models.Model):
    """
    Language model class
    """
    language = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.language


class Genre(models.Model):
    """
    Genre model class
    """
    genre = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.genre


class Format(models.Model):
    """
    Genre model class
    """
    format = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.format


class Book(models.Model):
    """
    Book model class
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=False, blank=False)
    isbn10 = models.CharField(max_length=10, unique=True, null=False, validators=[isbn10_min_length_validator,
                                                                                  isbn10_max_length_validator])
    isbn13 = models.CharField(max_length=17, unique=True, null=False, validators=[isbn13_min_length_validator,
                                                                                  isbn13_max_length_validator])
    date_of_publication = models.DateField()
    number_of_pages = models.PositiveIntegerField()
    book_cover = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    summary_of_book = models.TextField()
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords")
    format = models.ForeignKey(Format, on_delete=models.CASCADE, null=False, blank=False)
    price = models.IntegerField(default=0)
    author_bio = models.TextField(blank=True, null=True)
    unit_weight = models.IntegerField(null=True, blank=True)
    title_in_original_language = models.CharField(max_length=50, null=True)
    co_publisher = models.CharField(max_length=100, null=True)
    winner = models.TextField(null=True, blank=True)
    country_of_publication = models.CharField(max_length=100, help_text="Country of publication", null=True)
    designed_by = models.CharField(max_length=50, blank=True, null=True)
    edited_by = models.CharField(max_length=50, blank=True, null=True)
    translated_by = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
