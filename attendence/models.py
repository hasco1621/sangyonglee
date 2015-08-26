from django.db import models
#from datetime import datetime

# Create your models here.
class Attendence(models.Model):

    student_name = models.CharField(max_length=100)
    attend_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name

    #정렬순서 지정
    class Meta:
        ordering = ['-created_at', 'id']