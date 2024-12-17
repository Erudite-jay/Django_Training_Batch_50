from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','username', 'age', 'mobile_number', 'email')
#     search_fields = ('username'),
#     list_filter = ('age', 'email')