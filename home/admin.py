from django.contrib import admin
from .models import FoodMenu,Contact,Review,Orgainfo


# Register your models here.
admin.site.register(FoodMenu)
admin.site.register(Contact)
admin.site.register(Orgainfo)
admin.site.register(Review)