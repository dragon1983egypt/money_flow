
from django.shortcuts import get_object_or_404, redirect, render


from main.forms import CategoryForm, StatusForm, SubCategoryForm, TransactionForm, TransactionTypeForm
from main.models import Category, Status, SubCategory, Transaction, TransactionType

# Create your views here.


                            # +++++++++Список+++++++++
def transaction_list(request):
    transactions = Transaction.objects.all().order_by("-date")

    date_to = request.GET.get("date_to")
    date_form = request.GET.get("date_form")
    status_id = request.GET.get("status_id")
    type_id = request.GET.get("type")
    category_id = request.GET.get("category")
    subcategory_id = request.GET.get("subcategory")

                        # +++++++++++++фильтрация+++++++++
    if date_to:
        transactions = transactions.filter(date__lte=date_to)
    if date_form:
        transactions = transactions.filter(date__gte=date_form)
    if status_id and status_id.isdigit:
        transactions = transactions.filter(status_id=status_id)
    if type_id and type_id.isdigit:
        transactions = transactions.filter(type_id=type - id)
    if category_id and category_id.isdigit:
        transactions = transactions.filter(category_id=category_id)
    if subcategory_id and subcategory_id.isdigit:
        transactions = transactions.filter(subcategory_id=subcategory_id)

                # ++++++++++Извлекаем все обьекты+++++++++
    statusess = Status.object.all()
    types = TransactionType.object.all()
    categories = Category.object.all()
    subcategories = SubCategory.object.all()

    # ++++++++пишем контекст+++++++
    context = {
        "transactions": transactions,
        "statuses": statusess,
        "types": types,
        "categories": categories,
        "subcategories": subcategories,
        "filters": {
            "date_to": date_to,
            "date_from": date_form,
            "type": type_id,
            "status": status_id,
            "category": category_id,
            "subcategory": subcategory_id,
        },
    }
    return render(request, "cash_list.html", context)


                # ++++++++++создание записи++++++++++++
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:transaction_list")
        else:
            form = TransactionForm()
        return render(
            request, "main_form.html", {
                "form": form, 
                "title": "Запись создана"}
        )

        # ++++++++++++++редактирование записи++++++++++++++
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("main:transaction_list")
        else:
            form = TransactionForm(instance=transaction)
        return render(
            request, "main_form.html", {
                "form": form, 
                "title": "Запись отредактирована"}
        )

        #  ++++++++++++ удаление запси+++++++++++
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect("main:transaction_list")
    return render(
        request, 'main_form.html', {
            'transaction':transaction,
            'delete_confirm':True,
            'title': 'Запись удалена'
        }
    )
    
    
                #++++++++++++Справочники+++++++++++++++++
def guide_list(request):
    statuses =Status.objects.all()
    types    = TransactionType.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return render (
        request, 'guide_form.html', {
            'statuses': statuses,
            'types' : types,
            'categories': categories,
            'subcategories': subcategories,
        }
    )
    
                #++++++++++++++Статус+++++++++++++++++++++
                #++++++++++++++Создать+++++++++++++++++++++
def status_create(request):
    if request.method == "POST":
        form =StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = StatusForm()
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Создан новый статус"}
        )

                 #++++++++++++++Редактировать+++++++++++++++++++++
def status_edit(request,pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = StatusForm(instance=status)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Статус отредактирован"}
        )
        
                #++++++++++++++Удалить+++++++++++++++++++++
def status_delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == "POST":
        status.delete()
        return redirect("main:guide_list")
    return render(
        request, 'guide_form.html', {
            'object':status,
            'delete_confirm':True,
            'title': 'Статус удален'
        }
    )
    
                #+++++++++++++++Transactiontype++++++++++++++++++++
                #++++++++++++++Создать+++++++++++++++++++++
  
def transtype_create(request):
    if request.method == "POST":
        form =TransactionTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = TransactionTypeForm(instance=transtype_create)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Создан новый тип "}
        )

             #++++++++++++++Редактировать+++++++++++++++++++++
def transtype_edit(request,pk):
    transtype = get_object_or_404(TransactionType, pk=pk)
    if request.method == "POST":
        form = StatusForm(request.POST, instance=transtype)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = StatusForm(instance=transtype)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Тип отредактирован"}
        )
        
                #++++++++++++++Удалить+++++++++++++++++++++
def transtype_delete(request, pk):
    transtype = get_object_or_404(TransactionType, pk=pk)
    if request.method == "POST":
        transtype.delete()
        return redirect("main:guide_list")
    return render(
        request, 'guide_form.html', {
            'object':transtype,
            'delete_confirm':True,
            'title': 'Тип удален'
        }
    )
    
                #+++++++++++++++Категория++++++++++++++++++
                #++++++++++++++Создать+++++++++++++++++++++
  
def category_create(request):
    if request.method == "POST":
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = CategoryForm(instance=category_create)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Создана новая категория "}
        )

             #++++++++++++++Редактировать+++++++++++++++++++++
def category_edit(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = CategoryForm(instance=category)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Категория отредактирована"}
        )
        
                #++++++++++++++Удалить+++++++++++++++++++++
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("main:guide_list")
    return render(
        request, 'guide_form.html', {
            'object':category,
            'delete_confirm':True,
            'title': 'Категория удалена'
        }
    )                
                
                
                
                #+++++++++++++++Подкатегория++++++++++++++++++
                #++++++++++++++Создать+++++++++++++++++++++
  
def subcategory_create(request):
    if request.method == "POST":
        form =SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = TransactionTypeForm(instance=subcategory_create)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Создана новая подкатегория "}
        )

             #++++++++++++++Редактировать+++++++++++++++++++++
def subcategory_edit(request,pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        form = StatusForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect("main:guide_list")
        else:
            form = StatusForm(instance=subcategory)
        return render(
            request, "guide_form.html", {
                "form": form, 
                "title": "Подкатегория отредактирована"}
        )
        
                #++++++++++++++Удалить+++++++++++++++++++++
def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        subcategory.delete()
        return redirect("main:guide_list")
    return render(
        request, 'guide_form.html', {
            'object':subcategory,
            'delete_confirm':True,
            'title': 'Подкатегория удалена'
        }
    )