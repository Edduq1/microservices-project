from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.core.cache import cache

class HealthCheckView(APIView):
    permission_classes = [] # No requiere autenticación
    def get(self, request, *args, **kwargs):
        db_ok = False
        redis_ok = False
        try: # Probar DB
            connection.ensure_connection()
            db_ok = True
        except Exception: pass
        try: # Probar Redis
            redis_ok = cache.set('healthz', 'ok', timeout=1) and cache.get('healthz') == 'ok'
            if redis_ok: cache.delete('healthz')
        except Exception: pass

        if db_ok and redis_ok:
            return Response({"status": "ok", "db": "ok", "redis": "ok"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "db": "ok" if db_ok else "error", "redis": "ok" if redis_ok else "error"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)