
from django.contrib import admin
from .models import *
from django.contrib.admin import site, ModelAdmin
from django.contrib.admin import DateFieldListFilter
# Register your models here.
from django_admin_listfilter_dropdown.filters import  DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
from django.utils.html import format_html
from django.forms import widgets
from django.contrib.admin import SimpleListFilter
from admin_auto_filters.filters import AutocompleteFilter
import csv
from django.http import HttpResponse
from django.contrib.admin.widgets import AdminFileWidget
from django.contrib.admin import ListFilter, FieldListFilter
from django.utils.html import format_html
from django.forms import TextInput, Textarea
from django.db import models
from django import forms

# for image showing in inlines
class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))


#for multiple images
class Restaurants_imagesInline(admin.TabularInline):
    model = Restaurants_images 
    extra = 0
    can_delete = True
    classes = ['collapse']

    def has_delete_permission(self, request, obj=None):
        return True
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


class DifferentlySizedTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', 60)
        attrs.setdefault('rows', 10)
        super(DifferentlySizedTextarea, self).__init__(*args, **kwargs)


#class DiningnForm(forms.ModelForm):

    

class DiningAdmin(admin.ModelAdmin):
   
    list_display = ('Name_of_Restaurant','Address','Cuisines','Country','State','City','Rating')
    
    #list_display = ('Name_of_Restaurant', 'Category','Rating','City','Area','State','Country','Pin_Code','Helpline_Number','Cuisines','Average_Cost','Address','Brief_Overview','Active_Status','Added_on')
    search_fields=['Name_of_Restaurant','Category','Rating','City','Area','State','Country','Pin_Code','Cuisines','Average_Cost','Address','Active_Status','Added_on']
    #list_filter=['Name_of_Restaurant','Select_Category','Select_Rating','Select_City','Select_Area','Select_State','Select_Country','Pin_Code','Select_Cuisines','Select_Average_Cost','Address','Brief_Overview','Active_Status','Added_on']
    #raw_id_fields = ('Name_of_Restaurant','Select_Category')
    #for dropdown filter
    list_filter = (('Category', ChoiceDropdownFilter),('Country', ChoiceDropdownFilter),('State', ChoiceDropdownFilter),('City', ChoiceDropdownFilter),('Area', ChoiceDropdownFilter),('Rating', ChoiceDropdownFilter),('Cuisines', ChoiceDropdownFilter),('Average_Cost', ChoiceDropdownFilter),('Added_on', DateFieldListFilter))
    class Media:
        js = ['Dining/js/list_filter_collapse.js','Dining/js/guarded_admin.js']
    list_per_page = 7
    inlines = [Restaurants_imagesInline]
    formfield_overrides = { models.TextField: {'widget': DifferentlySizedTextarea}}

    # For delete lable
    actions = ['delete_model']
  

    def get_action_choices(self, request):
        default_choices = [("", " Action ")]
        return super(DiningAdmin, self).get_action_choices(request, default_choices)


    #for delete restaurant
    def get_actions(self, request):
        actions = super(DiningAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_model.short_description = 'Delete'

   #for viewlist changes
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Dining'}
        return super(DiningAdmin, self).changelist_view(request, extra_context=extra_context)
        
        
   

admin.site.register(Dining, DiningAdmin)  





#class VendorsRestaurant_searchAdmin(admin.ModelAdmin):
    #list_display =('Rating','City','Area','Cuisines')
   # search_fields=['Area']
   # list_filter = (('Rating', ChoiceDropdownFilter),('City', ChoiceDropdownFilter),('Area', ChoiceDropdownFilter),('Cuisines', ChoiceDropdownFilter))
   # list_per_page = 250

#admin.site.register(VendorsRestaurant_search, VendorsRestaurant_searchAdmin)




