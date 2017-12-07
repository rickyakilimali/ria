from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import BusinessProfileDetailView
from category.views import CategoryProfileListView


urlpatterns = [

			#url(r'^login/$', views.login, {'template_name':'accounts/login.html'}, 'login'),
			url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
			url(r'^profile/(?P<pk>[-\d]+)/$', BusinessProfileDetailView.as_view(), name='businessprofile-detail'),
			url(r'^my-products/$', CategoryProfileListView.as_view(template_name='browse-my-category.html'), name='base'),
			url(r'^my-products/category-slug/$', CategoryProfileListView.as_view(template_name='browse-my-products.html'), name='base'),
]

