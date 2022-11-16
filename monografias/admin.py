from django.contrib import admin

from .models import Advisor, CoAdvisor, Author, Monography
# Register your models here.
admin.site.register(Advisor)
admin.site.register(CoAdvisor)
admin.site.register(Author)
admin.site.register(Monography)
