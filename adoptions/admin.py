from django.contrib import admin
from .models import Adoption


class AdoptionAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "description")


admin.site.register(Adoption, AdoptionAdmin)