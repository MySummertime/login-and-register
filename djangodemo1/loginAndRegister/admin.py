
from django.contrib import admin
from .models import User


# Register your models here.

# Approach1
'''
admin.site.register(User)
'''

# Approach2
'''
# 1. create a sub class of admin.ModelAdmin
class UserAdmin(admin.ModelAdmin):
    pass

# 2. Register the the Model with admin.ModelAdmin
admin.site.register(User, UserAdmin)
'''

# Approach3
#'''
# integrate sub class generation && register that
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['name', 'email']}),
        ('Other Info', {'fields': ['gender']})
    ]
    list_display = ('name', 'gender', 'email', 'create_time')
    list_filter = ['create_time']
    search_fields = ['name']
#'''
