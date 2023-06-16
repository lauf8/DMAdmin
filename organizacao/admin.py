from django.contrib import admin
from .models import Oficialaria, OficialExecutivo, MestreConselheiroEstadual, MestreConselheiroRegional, GrandeConscelho
admin.site.register(OficialExecutivo)
admin.site.register(MestreConselheiroEstadual)
admin.site.register(GrandeConscelho)
admin.site.register(Oficialaria)
admin.site.register(MestreConselheiroRegional)
