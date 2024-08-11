from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('id', 'username',)
    ordering = '-id',
    search_fields = ('id', 'username',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'username',