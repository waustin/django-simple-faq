from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here
from .models import Question, Category


class FaqTestBase(TestCase):
    def setUp(self):
        self.cat_1 = Category.objects.create(name="Cat1",
                                             slug='cat1',
                                             display_order=2)

        self.cat_2 = Category.objects.create(name="Cat2",
                                             slug='cat2',
                                             display_order=1)

        self.q_1 = Question.objects.create(question="Q1",
                                           answer="A1",
                                           display_order=2,
                                           category=self.cat_1)
        self.q_2 = Question.objects.create(question="Q2",
                                           answer="A2",
                                           display_order=2,
                                           category=self.cat_2)
        self.q_3 = Question.objects.create(question="Q3",
                                           answer="A3",
                                           display_order=1,
                                           category=self.cat_1)
        self.q_4 = Question.objects.create(question="Q4",
                                           answer="A4",
                                           display_order=1,
                                           category=self.cat_2)


class FaqModelTests(FaqTestBase):

    def test_question_create(self):
        cat = Category.objects.create(name="Cat",
                                      slug='cat',
                                      display_order=2)

        q = Question.objects.create(question="This is a question?",
                                    answer="This is the answer",
                                    display_order=2,
                                    category=cat)

        self.assertEqual(q.__unicode__(), q.question)

    def test_category_create(self):
        cat = Category.objects.create(name="Cat",
                                      slug='cat',
                                      display_order=2)
        self.assertEqual(cat.__unicode__(), cat.name)


class FaqViewTests(FaqTestBase):
    def test_question_list_view(self):
        response = self.client.get(reverse('faq_question_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/question_list.html')
        # Question should be returned sorted by their categories display order
        # and then their display order
        self.assertQuerysetEqual(response.context['question_list'],
                                 [repr(self.q_4), repr(self.q_2),
                                  repr(self.q_3), repr(self.q_1)])

    def test_questions_by_category(self):
        response = self.client.get(reverse('faq_question_by_category',
                                   kwargs={'category_slug':self.cat_1.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/question_list.html')
        self.assertEqual(response.context['selected_category'].slug, self.cat_1.slug)
        self.assertQuerysetEqual(response.context['question_list'],
                                 [repr(self.q_3), repr(self.q_1)])

    def test_question_detail_view(self):
        response = self.client.get(self.q_4.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/question_detail.html')
        self.assertEqual(response.context['question'], self.q_4)
