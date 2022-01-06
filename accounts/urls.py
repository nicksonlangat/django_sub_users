from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', views.RegisterUserView)
router.register(r'users', views.UserViewset)
router.register(r'sub_users', views.SubUserViewset)

urlpatterns = router.urls