import datetime

from django.test import TestCase
from django.core.urlresolvers import reverse

from blog.constants import *
from blog.models import Post


class PostTestCase(TestCase):
    def test_is_draft(self):
    	post = Post(title='my title', slug='my-title', status=STATUS_DRAFT)
    	self.assertTrue(post.is_draft())

    	post.status = STATUS_PUBLISHED
    	self.assertFalse(post.is_draft())

    def test_is_published(self):
    	post = Post(title='my title', slug='my-title', status=STATUS_DRAFT)
    	self.assertFalse(post.is_published())    	

    	post.status = STATUS_PUBLISHED
    	self.assertTrue(post.is_published())

    def test_get_absolute_url(self):
    	post = Post(
	    		title='my title', 
	    		slug='my-title', 
	    		status=STATUS_DRAFT,
	    		authored_at=datetime.datetime(day=16, month=10, year=2012)
    		)

    	self.assertEqual(
    			post.get_absolute_url(),
    			reverse('blog_post_detail', kwargs={
			            'year': 2012,
			            'month': 10,
			            'slug': 'my-title'
    				})
    		)
