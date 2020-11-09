from django.contrib import admin
from .models import Site, SiteSeries, SiteCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class SiteAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["site_title", "site_published"]}),
        ("URL", {'fields': ["site_slug"]}),
        ("Series", {'fields': ["site_series"]}),
        ("Content", {"fields": ["site_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(SiteSeries)
admin.site.register(SiteCategory)

admin.site.register(Site, SiteAdmin) 