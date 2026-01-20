from django.urls import include, path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='post'
)
router.register(
    r'groups',
    GroupViewSet,
    basename='group'
)
router.register(
    r'posts/(?P<post>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls)),
]
