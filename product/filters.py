from .models import *
import django_filters




class ProductFilter(django_filters.FilterSet):
	class Meta:
			model = Laptop
			exclude = ['nom','vendeur','prix','is_active','category','units','polymorphic_ctype',]




def get_product_filter(product_model,criteria, queryset):


	class _ProductFilter(django_filters.FilterSet):
		class Meta:
			model = product_model
			exclude = ['nom','vendeur','prix','is_active','category','is_available','units',]

	return 	_ProductFilter(criteria, queryset)
