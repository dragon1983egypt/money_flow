
from django.db import models
from django.utils import timezone

 
            #++++++создаем модели++++ 
            #++++++ модель статус++++ 
class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name='Статус')
    
    def __str__(self):
        return self.name
    
            #++++++ модель тип транзакции++++ 
class TransactionType(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тип транзакции')
    
    def __str__(self):
        return self.name
    
            #++++++ модель категория++++ 
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Категория')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} ({self.transaction_type.name})'
    
            #++++++ модель подкатегория++++ 
class SubCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Подкатегория')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.category.name} '
    
    
                    #++++++ модель транзакция++++
class Transaction(models.Model):
    date = models.DateField(default=timezone.now, verbose_name='Дата')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, verbose_name='Тип транзакции')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name='Подкатегория')
    summa = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Сумма')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарии')
    
    def __str__(self):
        return f'{self.date} | {self.transaction_type.name} | {self.summa}'
    