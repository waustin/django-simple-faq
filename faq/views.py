from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Question, Category


class QuestionDetailView(DetailView):
    model = Question


class QuestionListView(ListView):
    def get_paginate_by(self):
        return settings.SIMPLE_FAQ_PAGINATE_BY

    def get_queryset(self, queryset):
        self.category = None
        if 'category_slug' in self.kwargs:
            self.category = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
            questions = Question.objects.filter(category=self.category).select_related('category').order_by('display_order')
        else:
            questions = Question.objects.all().select_related('category').order_by('category__display_order', 'display_order')

        return questions

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['selected_category'] = self.category
        return context
