from django.conf.urls import patterns, include, url
from .views import QuestionListView, QuestionDetailView

urlpatterns = patterns('',
    url(r'^$', QuestionListView.as_view(), name='faq_question_list'),
    url(r'^question/(?P<pk>\d+)/$',
        QuestionDetailView.as_view(), name='faq_question_detail'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',
        QuestionListView.as_view(), name='faq_question_by_category')
)
