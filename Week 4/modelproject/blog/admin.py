from django.contrib import admin
from .models import Blog 

# Register your models here.
class Blogadmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Blog, Blogadmin) 