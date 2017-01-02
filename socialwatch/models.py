from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from .utils.tracker_generator import id_generator
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse


class TwitterDataManager(models.Manager):
    def all(self, user):
        return super(TwitterDataManager, self).get_queryset().filter(tracker_user=user)


class TwitterData(models.Model):
    tracker_user = models.ForeignKey(User, blank=True, default=1)
    keyword = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    tracking_number = models.CharField(max_length=12, unique=True, blank=True)

    class Meta:
        unique_together = (("tracker_user", "keyword"),)

    objects = TwitterDataManager()

    def save(self, *args, **kwargs):
        if self.tracking_number is None or self.tracking_number == "":
            self.tracking_number = id_generator()
        super(TwitterData, self).save(*args, **kwargs)

    def save_clean(self, username, *args, **kwargs):
        if self.tracking_number is None or self.tracking_number == "":
            self.tracking_number = id_generator()
        if (TwitterData.objects.filter(tracker_user=username).filter(keyword=self.keyword).exists()):
            raise ValidationError("Keyword already Exists")
        else:
            if (TwitterData.objects.filter(tracker_user=username).count() > 2 ):
                return True
            else:
                super(TwitterData, self).save(*args, **kwargs)
                return False


    def get_absolut_url(self):
        return reverse("tracker_details",kwargs={"tracking_num":self.tracking_number})

    def __unicode__(self):
        return self.keyword
