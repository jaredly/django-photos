from django.db import models

class Photo(models.Model):
    """Photo model"""
    title = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)

    image = models.ImageField(upload_to = 'photos')
    description = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    tags = TagField()

    class Meta:
        ordering = ('-time',)

    def __unicode__(self):
        return u'%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('photos_detail', None, {'slug': self.slug})

class Gallery(models.Model):
    """Gallery model"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    description = models.CharField(max_length=255, blank=True)
    time = models.DateTimeField(auto_now=True)
    tags = TagField()

    images = models.ManyToManyField(Photo, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ('-time',)

    @permalink
    def get_absolute_url(self):
        return ('photos_gallery', None, {'slug': self.slug})

# Create your models here.
