from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('blog.views',
    url("^tag/(?P<tag>.*)/$", "blog_post_list", name="blog_post_list_tag"),
    url("^category/(?P<category>.*)/$", "blog_post_list", name="blog_post_list_category"),
    url("^author/(?P<author>\d+)/$", "blog_post_list", name="blog_post_list_author"),
    url(r"^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>.*)/$", "blog_post_detail", name="blog_post_detail"),
    url(r"^$", "blog_post_list", name="blog_post_list"),
)