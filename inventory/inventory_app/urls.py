from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, export_to_excel, export_to_pdf

router = DefaultRouter()
router.register('items', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('items/export/pdf/', export_to_pdf),
    path('items/export/excel/', export_to_excel),

]