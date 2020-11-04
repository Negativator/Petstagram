from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like


class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'age')


admin.site.register(Pet, PetsAdmin)
admin.site.register(Like)
