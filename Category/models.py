from django.db import models

# Create your models here.


class CategoryRoot(models.Model):

    """

        category root for define category main root

    """

    id = models.CharField(max_length=75, primary_key=True)

    title = models.CharField(max_length=25)
    visualize_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CategorySubRoot(models.Model):
    """

        category sub root for define category sub root

    """

    id = models.CharField(max_length=75, primary_key=True)

    title = models.CharField(max_length=25)
    visualize_status = models.BooleanField(default=True)

    category_root = models.ForeignKey(CategoryRoot, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

