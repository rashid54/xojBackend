from ojworkings import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('problist',views.Problist, basename='problist')

urlpatterns = router.urls
