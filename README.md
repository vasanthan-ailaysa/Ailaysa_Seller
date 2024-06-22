
class Author(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField(null=True, blank=True)


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    


class Staff(models.Model):
    pass