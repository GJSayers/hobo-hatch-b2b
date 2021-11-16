from django.db import models


class Faqs(models.Model):

    FAQ_CATEGORIES = (
        ('Delivery', 'Delivery'),
        ('Ordering', 'Ordering'),
        ('Payments', 'Payments'),
        ('Exclusivity', 'Exclusivity'),
        ('Marketing', 'Marketing'),
        )
    faq_category = models.CharField(max_length=14, choices=FAQ_CATEGORIES)
    question = models.TextField(max_length=250, null=False, blank=False)
    answer = models.TextField(max_length=250, null=False, blank=False)

    def __str__(self):
        return '%s %s' % (self.question, self.answer)
