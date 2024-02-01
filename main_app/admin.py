from django.contrib import admin
from .models import Finch, Feeding, Food
# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Food)