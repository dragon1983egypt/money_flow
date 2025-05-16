
from django.urls import path
from main import views

 
app_name = 'main'


                   #+++++++++++Транзакциии url++++++++++
urlpatterns = [
     path('', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
                             #+++++++++++справочник url++++++++++
    path('guide/', views.guide_list, name='guide_list'),
                            #+++++++++++категория url++++++++++
    path('guide/category/create/', views.category_create, name='category_create'),
    path('guide/category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('guide/category/<int:pk>/delete/', views.category_delete, name='category_delete'),
                             #+++++++++++Подкатегория url++++++++++
    path('guide/subcategory/create/', views.subcategory_create, name='subcategory_create'),
    path('guide/subcategory/<int:pk>/edit/', views.subcategory_edit, name='subcategory_edit'),
    path('guide/subcategory/<int:pk>/delete/', views.subcategory_delete, name='subcategory_delete'),
                            #+++++++++++тип url++++++++++
    path('guide/type/create/', views.transtype_create, name='transtype_create'),
    path('guide/type/<int:pk>/delete/', views.transaction_delete, name='transtype_delete'),
    path('guide/type/<int:pk>/edit/', views.transtype_edit, name='transtype_edit'),
                            #+++++++++++статус url++++++++++
    path('guide/status/create/', views.status_create, name='status_create'),
    path('guide/status/<int:pk>/edit/', views.status_edit, name='status_edit'),
    path('guide/status/<int:pk>/delete/', views.status_delete, name='status_delete'),
]
