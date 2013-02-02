class Following(models.Model):
    follower_content_type = models.ForeignKey(ContentType, related_name="followed", verbose_name=_('follower'))
    follower_object_id = models.PositiveIntegerField()
    follower_content_object = generic.GenericForeignKey('follower_content_type', 'follower_object_id')
    
    followed_content_type = models.ForeignKey(ContentType, related_name="followers", verbose_name=_('followed'))
    followed_object_id = models.PositiveIntegerField()
    followed_content_object = generic.GenericForeignKey('followed_content_type', 'followed_object_id')