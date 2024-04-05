from django.contrib import admin
from .models import *

# Register your models here.
#idhu venum na pottukalmm or else no needd
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name','image','description')
# admin.site.register(Category,CategoryAdmin)
    
    
admin.site.register(Category)
admin.site.register(Product)

