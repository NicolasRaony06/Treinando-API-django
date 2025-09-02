from django.contrib import admin
from .models import Produto, ItemVenda, Venda

admin.site.register(Produto)
admin.site.register(ItemVenda)
admin.site.register(Venda)
