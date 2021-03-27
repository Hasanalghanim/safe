from django.contrib import admin
from .models import walkrequest

# Register your models here.


class walkrequestAdmin(admin.ModelAdmin):
    readonly_fields = ('timerecived', )


admin.site.register(walkrequest, walkrequestAdmin)
