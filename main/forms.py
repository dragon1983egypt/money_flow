from tabnanny import verbose
from django import forms
from main.models import Category, Status, SubCategory, Transaction, TransactionType


# ++++++++создание форм+++++++
class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ["name"]
        verbose_name = 'тип транзакции'
        verbose_name_plural = 'типы транзакций'


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "transaction_type"]
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name", "category"]
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'


class TransactionForm(forms.ModelForm):
    date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Transaction
        fields = (
            "date",
            "status",
            "transaction_type",
            "category",
            "subcategory",
            "summa",
            "comment",
        )
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзакции'
        # применение метода init   и фильтрация

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["date"].label = "Дата"
        self.fields["status"].label = "Статус"
        self.fields["transaction_type"].label = "Тип"
        self.fields["category"].label = "Категория"
        self.fields["subcategory"].label = "Подкатегория"
        self.fields["summa"].label = "Сумма"
        self.fields["comment"].label = "Комментарий"

        if "category" in self.data:
            try:
                category_id = int(self.data.get("category"))
                self.fields["subcategory"].queryset = SubCategory.objects.filter(
                    category_id=category_id
                )
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.category:
            self.fields["subcategory"].queryset = self.instance.category.subcategories.all()
            

    # проверка значений валидации
    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get("transaction_type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        # +++++Бизнес правило №1++++++
        # +++++Пользователь не может выбрать подкатегорию, если она не связана с выбранной категорией++++++
        if category and subcategory and subcategory.category != category:
            raise forms.ValidationError(
                "Эта подкатегория не соотвествует выбранной категории"
            )

            # +++++Бизнес правило №2++++++
            # +++++Пользователь не может выбрать категорию, если она не относится к типу++++++
        if transaction_type and category and category.transaction_type != transaction_type:
            raise forms.ValidationError(
                "Эта категория не соотвествует типу, выберите другую"
            )

        return cleaned_data
