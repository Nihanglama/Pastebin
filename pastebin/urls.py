from django.urls import path
from .views import Home,Pasteitems,editor,executecode,Postpaste,Deleteitem,Profile

urlpatterns = [
    path('',Home,name='home'),
    path('formdata/',Postpaste,name='fromdata'),
    path('mypaste/',Pasteitems,name='mypaste'),
    path("profile/",Profile, name="profile"),
    path('delete/<int:pk>/',Deleteitem,name='delete'),
    path('editor/',editor,name='editor'),
    path('executecode/',executecode,name="executecode"),
]
