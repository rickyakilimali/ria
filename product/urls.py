from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import MyProductView, EditProductView


urlpatterns = [

			url(r'^my-product/$', MyProductView.as_view(), name='my-product'),
			url(r'^edit-product/$', EditProductView.as_view(), name='edit-product'),
]

