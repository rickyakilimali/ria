# tutorial/tables.py
import django_tables2 as tables
from .models import *

class ProductTable(tables.Table):
    class Meta:
        model = Laptop
        exclude = exclude = ('id','category','polymorphic_ctype','is_active','productbase_ptr',)
