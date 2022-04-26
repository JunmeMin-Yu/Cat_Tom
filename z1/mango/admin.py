from django.contrib import admin
from .models import Mango

# Register your models here.

class mangoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Mango, mangoAdmin)
