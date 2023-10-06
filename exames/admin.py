from django.contrib import admin

from django.contrib import admin
from .models import TiposExames, SolicitacaoExame, PedidosExames

admin.site.register(TiposExames)
admin.site.register(PedidosExames)
admin.site.register(SolicitacaoExame)