from django.db import models
from uuid import uuid4

# Create your models here.

class Category(models.Model):
    name        = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model) :
    uuid        = models.UUIDField(default=uuid4, editable=False, db_index= True)
    category    = models.ForeignKey(Category, on_delete=models.PROTECT) #default는models.CASCADE(자동삭제)
    title       = models.CharField(max_length=100, db_index=True)
    content     = models.TextField()

    # tags        = models.ManyToManyField('Tag', blank=True)
    origin_url  = models.URLField(blank=True)
    ip          = models.GenericIPAddressField(blank=True, null=True)
    is_public   = models.BooleanField(default=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
