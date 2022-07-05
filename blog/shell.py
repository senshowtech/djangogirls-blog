from blog.models import *
from django.contrib.auth.models import User
from django.db.models import Count

# save data and add relationship to many to many User model
save_data1 = Post(title='test', text='test', author_id=1)
save_data1.save()
sena = User.objects.get(username='sena')
save_data1.like_by.add(sena)

# lihat keseluruhan data di queryset
# values_list()

# relasi many to many to user
posts = Post.objects.prefetch_related(
    'like_by').all().annotate(count=Count('like_by'))
