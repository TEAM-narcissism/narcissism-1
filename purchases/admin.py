from django.contrib import admin
from . import models
# Register your models here.

class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
   
   inlines = (PhotoInline,)

   fieldsets = (("Custom Profile", {"fields": ("closed", "title", "host", "explain", "price", "max_people", "participants", )}),)

   list_display = (
      "closed",
      "title",
      "host",
      "max_people",
      "price"
   )

   filter_horizontal = (
      "participants",
   )