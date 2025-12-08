from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # type - id - object_name
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    objects_name = GenericForeignKey()
