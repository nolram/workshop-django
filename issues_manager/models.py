from django.db import models

from django.contrib.auth import get_user_model

USERMODEL = get_user_model()

# Create your models here.
class Issue(models.Model):
    pk_db = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(USERMODEL, on_delete=models.DO_NOTHING, related_name="user_issue")
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pk} - {self.user} - {self.is_open} - {self.date_creation} - {self.description}'
