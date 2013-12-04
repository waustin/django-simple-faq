from django import forms
from django.conf import settings
from django.contrib import admin

from .models import Category, Question

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'display_order')
    prepopulated_fields = {'slug': ('name',)}


class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = {
            #'question' : forms.Textarea(attrs={'class':'mceSimple'}),
            'answer': forms.Textarea(attrs={'class':'mceSimple'})
        }

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('question', 'display_order', 'category')
    search_fields = ('question', 'answer')
    list_filter = ('category',)

    class Media:
        js = (settings.STATIC_URL + 'js/tiny_mce/tiny_mce.js',
              settings.STATIC_URL + 'js/tiny_mce_simple_init.js')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)

