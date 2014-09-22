from django.contrib import admin

# Register your models here.

from .models import jumpstarter

class AdminJumpstarter(admin.ModelAdmin):

	class Meta:

		model = jumpstarter

admin.site.register(jumpstarter, AdminJumpstarter)