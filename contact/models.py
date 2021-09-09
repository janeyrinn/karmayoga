from django.db import models
from django.contrib.auth.models import User


SUBJECT_MENU = (
    ('general_query', 'GENERAL QUERY'),
    ('where_is_my_order', 'WHERE IS MY ORDER?'),
    ('complaint', 'COMPLAINT'),
    ('collaboration', 'COLLABORATION'),
)


class Contact(models.Model):
    """
    A Contact model for admin to view users queries
    """
    class Meta:
        verbose_name_plural = 'Queries'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=False, blank=False)
    subject = models.CharField(max_length=100, choices=SUBJECT_MENU,
                               default='general_query',
                               null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
