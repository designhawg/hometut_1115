from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		('Carrot Corn',			{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'
	

admin.site.register(Poll, PollAdmin)