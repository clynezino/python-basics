from django.db import models
from datetime import datetime

class SiteCategory(models.Model):
    site_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.site_category


class SiteSeries(models.Model):
    site_series = models.CharField(max_length=200)
    site_category = models.ForeignKey(SiteCategory, default=1, verbose_name="Categories", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.site_series    
# Create your models here.
class Site(models.Model):
    site_title = models.CharField(max_length=250)
    site_content = models.TextField()
    site_published = models.DateTimeField("date published", default=datetime.now( ))

    site_series = models.ForeignKey(SiteSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    site_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.site_title
        