import datetime

from django.test import TestCase
from django.contrib.auth.models import User


from blog.models import Post


class PublishedPostManagerTestCase(TestCase):
    fixtures = ['posts.json']

    def test_published_posts_anonymous(self):
        posts = Post.objects.published().order_by('slug')

        self.assertEqual(
                [post.slug for post in posts],
                [u'brief-history-blues', u'brief-history-rock', u'learn-sing']
            )

        # changing date of learn-sing to future
        learn_sing = Post.objects.get(slug='learn-sing')
        learn_sing.authored_at = datetime.datetime.now() + datetime.timedelta(minutes=1)
        learn_sing.save()

        posts = Post.objects.published().order_by('slug')

        self.assertEqual(
                [post.slug for post in posts],
                [u'brief-history-blues', u'brief-history-rock']
            )

    def test_published_posts_staff(self):
        admin = User.objects.get(username='admin')

        posts = Post.objects.published(for_user=admin).order_by('slug')

        self.assertEqual(
                [post.slug for post in posts],
                [u'brief-history-blues', u'brief-history-rock', u'learn-draw', u'learn-sing']
            )

        # changing date of learn-sing to future
        learn_sing = Post.objects.get(slug='learn-sing')
        learn_sing.authored_at = datetime.datetime.now() + datetime.timedelta(minutes=1)
        learn_sing.save()

        posts = Post.objects.published(for_user=admin).order_by('slug')

        self.assertEqual(
                [post.slug for post in posts],
                [u'brief-history-blues', u'brief-history-rock', u'learn-draw', u'learn-sing']
            )
