from django.urls import path
from shortner import views

urlpatterns=[
    path('',views.HomeView.as_view()),
    path('<slug:slug>',views.view1)
]