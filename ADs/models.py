from django.db import models

# Create your models here.


class ADs(models.Model):

    """

    for store website ad image and send it to front-End

    """

    id = models.CharField(max_length=75, primary_key=True)

    title = models.CharField(max_length=50)
    description = models.TextField()

    date = models.DateTimeField()
    expire_date = models.DateTimeField()

    image = models.ImageField()

    visualize_status = models.BooleanField(default=True)

    def __str__(self):

        return self.title
