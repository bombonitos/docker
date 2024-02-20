"""
URL configuration for hellokitty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from hello import views
#from hello.views import add_to_cart
from hello import views
from hello.views import Search


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("index/", views.index, name='index'),
    path("catalog/", views.catalog),
    path("cart/", views.cart),
    path("contact/", views.contact),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('profile/', views.profile, name='profile'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path("reviews/", views.reviews),
    path("search/", Search.as_view(), name='search'),
    path("politics/", views.politics),
    path("confidence/", views.confidence),
    path("about/", views.about),
    path("tovar/", views.tovar),


]


urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)