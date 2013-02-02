# Django model
class Tag(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True, db_index=True)



# in database it is:
# id, tag_id(fk-tag), content_type_id(fk-content_type), object_id()
class TaggedItem(models.Model):
    """
    Holds the relationship between a tag and the item being tagged.
    """
    tag          = models.ForeignKey(Tag, verbose_name=_('tag'), related_name='items')
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id    = models.PositiveIntegerField(_('object id'), db_index=True)
    object       = generic.GenericForeignKey('content_type', 'object_id')

## 