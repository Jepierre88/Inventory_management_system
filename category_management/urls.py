from django.urls import path
from .views import *

urlpatterns = [
    path("update/<str:pk>", UpdateCategory.as_view()),
    path("", createCategory),
    path("delete/<str:pk>", DeleteCategory.as_view()),
    path("one/<str:pk>", ReadCategoryByID.as_view())
]
