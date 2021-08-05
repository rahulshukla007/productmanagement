from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('addprod/', views.addProduct, name="addproduct"),
    path('editprod/<str:pk>', views.editProduct, name="editproduct"),
    path('delprod/<str:pk>', views.delProduct, name="delproduct")


]
