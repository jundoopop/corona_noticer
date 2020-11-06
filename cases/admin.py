from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.SumCorona)
class SumAdmin(admin.ModelAdmin):
    pass

@admin.register(models.DailyCorona)
class DailyAdmin(admin.ModelAdmin):
    pass