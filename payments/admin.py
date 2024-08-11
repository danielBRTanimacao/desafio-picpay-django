from django.contrib import admin
from .models import Transactions

# Register your models here.
@admin.register(Transactions)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'payer', 'payee',)
    list_display_links = ('id', 'payer',)
    ordering = '-id',
    search_fields = ('id', 'payer',)
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'payer',