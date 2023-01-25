from django.urls import path
from rest_framework import routers

from .views import CommentViewSet, PostViewSet, like_post

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_post, name='like_post')
]

## name을 쓰는 이유는 다음과 같이 reverse를 통해 페이지 이동이 쉽기 때문이다. 이러면 url이 바뀌더라도 연결되는 코드들을 바꿀 필요가 없다.
# from django.urls import reverse
# reverse('bar')
