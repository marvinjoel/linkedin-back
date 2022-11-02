from rest_framework import routers

from accounts.genericviews import ListUsers

router = routers.SimpleRouter()
router.register(r'user', ListUsers)

urlpatterns = router.urls

