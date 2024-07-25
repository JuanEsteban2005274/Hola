from django.urls import path
from .import views
from tienda.views import ReporteProductoExcel # lo utilizaremos en una vista

urlpatterns = [
    path('tienda/', views.tienda, name='Tienda' ),
    path('reporte/', ReporteProductoExcel.as_view(), name='reporte' ), # 
    path('listado/', views.Listado, name='Listado' ),
    path('pdf/', views.ListaProductoPdf.as_view(), name='pdf' ),
    path('api/', views.api, name='api' ),
]