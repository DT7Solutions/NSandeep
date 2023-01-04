from django.urls import path
from .views import home,Post_Item
urlpatterns = [
    path('', home,name="home"),
    path('blog/<int:id>', Post_Item,name="blog"),
]

