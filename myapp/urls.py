from django.urls import path
from . import views

urlpatterns = [
    path('', views.hydroproject_list, name='hydroproject_list'),
    path('create/', views.hydroproject_create, name='hydroproject_create'),
    path('update/<int:project_id>/', views.hydroproject_update, name='hydroproject_update'),
    path('delete/<int:project_id>/', views.hydroproject_delete, name='hydroproject_delete'),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.hydroproject_list, name='hydroproject_list'),
#     path('create/', views.hydroproject_create, name='hydroproject_create'),
#     path('update/<int:project_id>/', views.hydroproject_update, name='hydroproject_update'),
#     path('delete/<int:project_id>/', views.hydroproject_delete, name='hydroproject_delete'),
# ]
