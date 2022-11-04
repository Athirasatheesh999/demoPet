
from django.urls import path
from.import views
app_name='petsapp'

urlpatterns = [

    path('',views.index,name="index"),
    path('pets/<int:pets_id>/',views.detail,name='detail'),
    path('add/',views.add_pets,name='add_pets'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name="delete"),

]
