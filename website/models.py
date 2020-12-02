from django.db import models

class Content(models.Model):
    STATUS = (
        ('Published', 'Published'),
        ('Draft', 'Draft'),
        ('Deleted', 'Deleted'),
    )
    title = models.CharField(max_length=1000, default='Title', blank=False)
    slug = models.CharField(max_length=256, blank=False)
    body = models.TextField(default='Body')
    excerpt = models.TextField(default='Excerpt')
    status = models.CharField(max_length=16, choices=STATUS, default='Draft')
    mod_date = models.DateTimeField('Date modified')

class Category(models.Model):
    name = models.CharField(max_length=256, blank=False)
    slug = models.CharField(max_length=256, blank=False)
    def __str__(self):
        return "%s" % (self.name)
    def __unicode__(self):
        return  u'%s' % (self.name)

    @property
    def get_products(self):
        return Product.objects.filter(category__name=self.name)

class Product(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Deleted', 'Deleted'),
    )
    name = models.CharField(max_length=1000, default='Product name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    is_featured = models.BooleanField(default=True, verbose_name='Featured product?', help_text='Check if featured')
    slug = models.CharField(max_length=256, default='slug')
    description = models.TextField(default='Product description')
    features = models.TextField(default='Product features')
    image = models.ImageField(upload_to='product/', blank=True)
    price = models.CharField(max_length=16, default='$20')
    status = models.CharField(max_length=16, choices=STATUS, default='Available')
    mod_date = models.DateTimeField('Date modified')
