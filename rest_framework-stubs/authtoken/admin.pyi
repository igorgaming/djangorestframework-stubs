from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

class TokenChangeList(ChangeList): ...
class TokenAdmin(admin.ModelAdmin): ...
