from django.db.models import Count
from django.contrib.auth.models import User

from taggit.models import Tag

from blog.constants import *
from blog.models import Category


def get_annotated_authors():
    """
        Returns the list of authors ordered by posts count.
    """
    return User.objects.all().filter(post__status=STATUS_PUBLISHED).annotate(
            post_count=Count('post')
        ).filter(post_count__gt=0).order_by('-post_count')

def get_annotated_tags():
    """
        Returns the list of tags ordered by posts count.
    """
    return Tag.objects.all().filter(post__status=STATUS_PUBLISHED).annotate(
            post_count=Count('post')
        ).filter(post_count__gt=0).order_by('-post_count')

def get_annotated_categories():
    """
        Returns the list of categories ordered by posts count.
    """
    return Category.objects.all().filter(post__status=STATUS_PUBLISHED).annotate(
            post_count=Count('post')
        ).filter(post_count__gt=0).order_by('-post_count')