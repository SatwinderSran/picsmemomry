from django.contrib import admin
from .models import Post,Slider



class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'city','date_posted')
    list_filter = ('name', 'author', 'city','date_posted')
    search_fields = ('author__username', 'name')      
    date_hierarchy = ('date_posted')



class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'order', 'start_date', 'end_date', 'active', 'featured']
    list_editable = ['order', 'start_date', 'end_date']
    class Meta:
        model = Slider


admin.site.register(Post, PostAdmin)
admin.site.register(Slider, SliderAdmin)