from django.db import models

from profiles.models import UserProfile

class Testimonial(models.Model):
    """
    Class to define Testimonial for the about page
    """
    class Meta:
        """
        Class to designate plural name
        """
        verbose_name_plural = 'Testimonials'

    stockist = models.ForeignKey(   
        UserProfile, null=True, blank=False, on_delete=models.SET_NULL)
    buyer_name = models.CharField(max_length=90, null=False, blank=False)
    testimonial = models.TextField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.testimonial
