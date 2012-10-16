from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from taggit.models import Tag

from blog.constants import *
from blog.models import Post, Category
from blog.utils import get_annotated_categories, get_annotated_authors, \
    get_annotated_tags


def blog_post_detail(request, slug, year=None, month=None):
    """
        Displays a blog post.
    """
    
    post = get_object_or_404(Post.objects.published(for_user=request.user), slug=slug)
    
    recent_posts = Post.objects.published(for_user=request.user)

    return render_to_response('blog/blog_post_detail.html', {
            'post': post,
            'recent_posts': recent_posts
        }, context_instance=RequestContext(request))


def blog_post_list(request, tag=None, category=None, author=None, month=None):
    """
        Displays a list of blog posts that are filtered by tag or category.
    """
    
    posts = Post.objects.published(for_user=request.user)
    
    if tag:
        tag = get_object_or_404(Tag, slug=tag)
        posts = posts.filter(tags__slug=tag.slug)
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category__slug=category.slug)
    if author:
        author = get_object_or_404(User, pk=author)
        posts = posts.filter(author=author)

    categories = get_annotated_categories()
    tags = get_annotated_tags()
    authors = get_annotated_authors()
    return render_to_response('blog/blog_post_list.html', {
            'posts': posts,
            'tag': tag,
            'author': author,
            'category': category,
            'categories': categories,
            'tags': tags,
            'authors': authors
        }, context_instance=RequestContext(request))