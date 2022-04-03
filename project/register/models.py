from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    """Model representing an User."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    class Meta:
        ordering = ['last_name', 'first_name']


    def get_absolute_url(self):
        """Returns the url to access a particular user instance."""
        return reverse('user-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'