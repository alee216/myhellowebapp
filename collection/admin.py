from django.contrib import admin
from collection.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

# Register your models here.

admin.site.register(Profile, ProfileAdmin)