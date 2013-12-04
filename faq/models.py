from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=75,unique=True,db_index=True)
    display_order = models.PositiveIntegerField(default=1, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('display_order',)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    display_order = models.PositiveIntegerField(default=1, db_index=True)
    category = models.ForeignKey(Category, related_name='questions',
                                 null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('display_order',)

    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return ('faq_question_detail', (), {'pk':self.pk})
