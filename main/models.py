
from django.db import models
from django.utils import timezone

 
            #++++++создаем модели++++ 
            #++++++ модель статус++++ 
class Status(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    class Meta:
        # db_table ='status'
        verbose_name ='статус'
        verbose_name_plural = 'статусы'
    
    def __str__(self):
        return self.name
    
            #++++++ модель тип транзакции++++ 
class TransactionType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    
    class Meta:
        # db_table ='transactiontype'
        verbose_name ='тип транзакции'
        verbose_name_plural = 'типы транзакции'
    
    def __str__(self):
        return self.name
    
            #++++++ модель категория++++ 
class Category(models.Model):
    name = models.CharField(max_length=150)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name="categories")
    
    class Meta:
        # db_table ='category'
        verbose_name ='категория'
        verbose_name_plural = 'категории'
    
    
    def __str__(self):
        return f'{self.name} ({self.transaction_type.name})'
    
            #++++++ модель подкатегория++++ 
class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    
    class Meta:
        # db_table ='subcategory'
        verbose_name ='подкатегория'
        verbose_name_plural = 'подкатегории'
    
    def __str__(self):
        return f"{self.name} -> {self.category.name}"
    
    
                    #++++++ модель транзакция++++
class Transaction(models.Model):
    date = models.DateField(default=timezone.now )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name="transactions")
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, related_name="transactions")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="transactions")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name="transactions")
    summa = models.DecimalField(max_digits=14, decimal_places=2)
    comment = models.TextField(blank=True, null=True)  # необязателен к заполнению
    
    class Meta:
        # db_table ='transaction'
        verbose_name ='транзакция'
        verbose_name_plural = 'транзакции'
    
    
    def __str__(self):
        return f"{self.date} | {self.transaction_type.name} | {self.summa} рублей"
    
