import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from blog.constants import *
from blog.managers import PublishedPostManager


class Category(models.Model):
    """
        Category object for Post.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(blank=True, 
            help_text='This will appear on the posts list.'
        )

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200, 
    		help_text='Title (200 characters max).'
    	)
    slug = models.SlugField(
    		help_text='Suggested value automatically generated from title.'
    	)
    
    tags = TaggableManager(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    
    summary = models.TextField(help_text='Blog post summary.')
    body = models.TextField(help_text='Main body.')
    
    author = models.ForeignKey(User, help_text='Author of this blog post.')
    authored_at = models.DateTimeField(
    		default=datetime.datetime.now, 
    		help_text='Date displayed on the main page.'
    	)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_DRAFT, 
            help_text="If saved as a draft, this blog post will not be visible."
        )
    
    objects = PublishedPostManager()
    
    class Meta:
        ordering  = ('-authored_at',)
        get_latest_by = 'authored_at'

    def __unicode__(self):
        return u'%s' % self.title
    
    @property
    def tags_list(self):
        """
            Return the list of keywords.
        """
        return self.tags.values_list('name', flat=True)

    def is_draft(self):
        return self.status == STATUS_DRAFT
    
    def is_published(self):
        return self.status == STATUS_PUBLISHED
    
    @models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', None, {
            'year': self.authored_at.year,
            'month': self.authored_at.strftime('%m'),
            'slug': self.slug
        })