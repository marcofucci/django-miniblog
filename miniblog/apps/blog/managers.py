import datetime

from django.db import models


class PublishedPostManager(models.Manager):
    """
    Returns published posts.
    """

    def published(self, for_user=None):
        """
        If for_user == None or a non-staff user, returns only published
        posts, that is posts with published status and with authored_at date
        not in the future.
        For staff users if returns all the posts, useful for previews.
        """
        from blog.constants import *
        
        if for_user is not None and for_user.is_staff:
            return self.all()
        
        return self.filter(
            authored_at__lte=datetime.datetime.now(), status=STATUS_PUBLISHED
        )