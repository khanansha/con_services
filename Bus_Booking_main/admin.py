from django.contrib import admin
from . models import BusBooking
# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.admin import site, ModelAdmin
from django.contrib.admin import DateFieldListFilter
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
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
from merged_inlines.admin import MergedInlineAdmin

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

        output.append(super(AdminFileWidget, self).render(
            name, value, attrs, renderer))
        return mark_safe(u''.join(output))


class imagesInline(admin.TabularInline):
    model = image
    extra = 1
    can_delete = True
    classes = ['collapse']

    def has_delete_permission(self, request, obj=None):
        return True
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }



class BusBookingAdmin(admin.ModelAdmin):

    list_display = ('Name_of_Bus', 'Facilities',
                    'Bus_Type', 'Rating', 'Ticket_Amount_Per_Passenger','AddedOn','Status')
    #list_filter = (('Airport', ChoiceDropdownFilter),('Country', ChoiceDropdownFilter),('City', ChoiceDropdownFilter),('AddedOn', DateFieldListFilter),('Status', ChoiceDropdownFilter))   
    #fieldsets =(
         #   ('Extra Fields', {'fields': ('Package_Details',)}),
   #) 
    search_fields=['Name_of_Bus','Bus_Type','Rating','Status']           
    list_per_page = 7
    inlines = [imagesInline]

    #for viewlist changes
    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'BUS BOOKING'}
        return super(BusBookingAdmin, self).changelist_view(request, extra_context=extra_context)
    # For delete lable
    actions = ['delete_model']
  

    def get_action_choices(self, request):
        default_choices = [("", " Action ")]
        return super(BusBookingAdmin, self).get_action_choices(request, default_choices)


    #for delete restaurant
    def get_actions(self, request):
        actions = super(BusBookingAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_model.short_description = 'Delete'
    
        


admin.site.register(BusBooking, BusBookingAdmin)
