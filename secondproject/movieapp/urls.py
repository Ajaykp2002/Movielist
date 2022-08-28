# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path, include
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:movie_id>/',views.list,name="list"),
    path('add/',views.add,name="add"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]


