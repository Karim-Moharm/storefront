from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # generic items
    # we need the content type and id
    # the model_id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # any object in the model
    object_id = models.PositiveIntegerField()
    # the original objct that being refrenced
    """doesn't created in database, it's proberty that join contnet_type_id with 
    object_id and became an object
    """
    object_name = GenericForeignKey()
