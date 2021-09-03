from django.db import models


class Snippet(models.Model):

    # Many to one relationship
    # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    # highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']


class Maps_Search_autocomplete(models.Model):
    user_id = models.IntegerField()
    search_time = models.DateTimeField(auto_now_add=True)
    search_place = models.TextField()
    username = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['search_time']


