from django.urls import path
from . import views

urlpatterns = [
    # path('', index, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
]