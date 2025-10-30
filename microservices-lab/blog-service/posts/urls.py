from rest_framework.routers import DefaultRouter
from .views import PostViewSet # Importa tu vista existente

router = DefaultRouter()
# Registra el ViewSet. DRF crea /posts/ y /posts/<pk>/ automáticamente
router.register(r'', PostViewSet, basename='post')

urlpatterns = router.urls