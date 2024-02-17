from django.contrib import admin

from .models import *

admin.site.register([Person, IR, LAR, IRLAR, PersonIR, Request])