class Avatar(models.Model):
    user = models.ForeignKey(User)
    image_id = models.CharField(_('image_id'), null=True, max_length=45,blank = True)
    date_uploaded = models.DateTimeField(default=datetime.datetime.now)

'''
image里面存放图片的各种尺寸的URL
'''