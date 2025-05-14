from django import forms
from main.models import Category, Status, SubCategory, Transaction, TransactionType


                # ++++++++создание форм+++++++
class TransactionTypeForm(forms.ModelForm):
    class Meta:
        model = TransactionType
        fields = ["name"]
        

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "transaction_type"]


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name", "category"]


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
            # применение метода init    
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

        self.fields["date"].label = "Дата"
        self.fields["status"].label = "Статус"
        self.fields["transaction_type"].label = "Тип"
        self.fields["category"].label = "Категория"
        self.fields["subcategory"].label = "Подкатегория"
        self.fields["amount"].label = "Сумма"
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
            self.fields["subcategory"].queryset = (
                self.instance.category.subcategories.all()
            )

    # проверка значений
    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get("transaction_type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        
                            #+++++Бизнес правило №1++++++
                            #+++++Пользователь не может выбрать подкатегорию, если она не связана с выбранной категорией++++++
        if category and subcategory and subcategory.category != category:
            raise forms.ValidationError(
                "Эта подкатегория не соотвествует выбранной категории"
            )               
            
                            #+++++Бизнес правило №2++++++
                            #+++++Пользователь не может выбрать категорию, если она не относится к типу++++++
        if transaction_type and category and category.transaction_type != category:
            raise forms.ValidationError(
                "Эта категория не соотвествует типу, выберите другую"
            )
        
        return cleaned_data
