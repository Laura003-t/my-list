from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('sign-up/', views.register, name='signup'),
    path('logout/', views.logout, name='logout'),

    # Main Pages
    path('home/', views.home, name='home'),
    path('folders/', views.folders, name='folders'),
    path('profile/', views.profile, name='profile'),

    # Folders
    path('folders/create/', views.folders_create, name='create_folder'),
    path('folders/<str:pk>/update/', views.lists_update, name='update_folder'),

    # Lists
    path('folders/<str:pk>/lists/', views.lists, name='lists'),
    path('folders/<str:pk>/lists/create/', views.lists_create, name='create_list'),

    # List details
    path('lists/<str:pk>/', views.list_details, name='list_detail'),
    path('lists/<str:pk>/add-item/', views.add_list_item, name='add_list_item'),
    path('lists/<str:pk>/export-pdf/', views.export_list, name='export_list_pdf'),

    # List items actions
    path('lists/item/<str:pk>/toggle-item/', views.toggle_list_item, name='toggle_item'),
    path('lists/item/<str:pk>/edit/', views.edit_list_item, name='edit_time'),
    path('lists/item/<str:pk>/delete/', views.delete_list_item, name='delete_item'),
]