from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.urls.conf import include
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from rest_framework.request import Request

from over_engineered import settings

trace.set_tracer_provider(TracerProvider())

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))


def home_page_view(_: Request) -> HttpResponse:
    """Temp view for testing."""
    return HttpResponse("Hello, world")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page_view, name="home"),
    path("user/", include("users.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("toolbar/", include(debug_toolbar.urls)),
        *urlpatterns,
    ]
