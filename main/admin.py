from django.contrib import admin

from main.models import Category, Status, SubCategory, Transaction, TransactionType




                #++++++ административная панель ++++
@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display =( 'id', 'name')
    search_fields = ('name')
           
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display =( 'id', 'name')
    search_fields = ('name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =( 'id', 'name', 'transaction_type')
    list_filter = ('transaction_type')
    search_fields = ('name')


@admin.register(SubCategory)
class SubCategotyAdmin(admin.ModelAdmin):
    list_filter = ('transaction_type')
    list_display =( 'id', 'name', 'category')
    search_fields = ('name')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = ('status', 'category', 'subcategory', 'transaction_type')
    list_display =( 'id', 'date', 'status', 'transaction_type', 'subcategory', 'category', 'summa')
    search_fields = ('comment', 'name')