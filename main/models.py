
from django.db import models
from django.utils import timezone


# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Статус')
    
    def __str__(self):
        return self.name

class TransactionType(models.Model):
    name = models.CharField(max_length=150, unigue=True, verbose_name='Переводы')
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name='categories', verbose_name='категории')
    
    def __str__(self):
        return f'{self.name} ({self.transaction_type.name})'
    

class SubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', verbose_name='подкатегории')
    
    def __str__(self):
        return f'{self.name} {self.category.name} '
    
class Transaction(models.Model):
    date = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='transactions', verbose_name='Переводы')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, related_name='transactions', verbose_name='Переводы')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions', verbose_name='Переводы')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='transactions', verbose_name='Переводы')
    summa = models.DecimalField(max_digits=14, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.date} | {self.transaction_type.name} | {self.summa}'
    