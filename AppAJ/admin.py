from operator import contains
from typing import Container
from django.contrib import admin

from AppAJ.views import contacto, materiales, nosotros, trabajos_realizados
from AppAJ.models import Admin, Contacto, Materiales, Nosotros, Trabajos_realizados

# Register your models here.

admin.site.register(Contacto)
admin.site.register(Materiales)
admin.site.register(Nosotros)
admin.site.register(Trabajos_realizados)
admin.site.register(Admin)


