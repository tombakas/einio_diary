from django.contrib import admin
from einio_diary.models import Irasas

class IrasasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Irasas, IrasasAdmin)
