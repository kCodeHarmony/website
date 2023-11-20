from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.posts, name='news'),
    path('category/<int:id>', views.category, name='category'),
    path('categories', views.categories, name='categories'),
    path('detail/<int:id>', views.post_details, name='details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
