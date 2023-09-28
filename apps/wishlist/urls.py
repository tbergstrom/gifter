from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('add_item', views.add_item, name="add_item"),
    path('submit_item', views.submit_item, name="submit_item"),
    path('join/<int:item_id>/', views.join, name="join"),
    path('unjoin/<int:item_id>/', views.unjoin, name="unjoin"),
    path('delete/<int:item_id>/', views.delete, name="delete"),
    path('show/<int:item_id>/', views.show, name="show"),
    path('profile/<int:item_user_id>/', views.profile, name="profile")
]