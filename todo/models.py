from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    subject = models.CharField(max_length=128)
    note = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    deadline_date = models.DateTimeField(null=True, blank=True)
    finished_date = models.DateTimeField(null=True, blank=True)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
    def finish_task(self):
        self.finished_date = timezone.now()
        self.save()
    
    def delete_task(self):
        self.delete_flag = True
        self.save()