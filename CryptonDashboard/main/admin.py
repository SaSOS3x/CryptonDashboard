from django.contrib import admin
from .models import Node, World, VPS, Country

# Register your models here.
admin.site.register(Node)
admin.site.register(World)
admin.site.register(VPS)
admin.site.register(Country)