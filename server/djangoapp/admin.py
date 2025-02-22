from django.contrib import admin

# from .models import related models
from .models import CarMake, CarModel


# Register your models here.
class CarModelInline(admin.TabularInline): 
    model = CarModel
    extra = 1


# CarModelInline class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')


# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    inlines = [CarModelInline]


# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
