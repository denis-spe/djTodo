# Love the LORD your GOD with all thine mind and with all thine soul
# And love your neighbor as your self

# Libraries to be used
from . import views
from django.urls import path, URLPattern
from typing import List

# Application name
app_name = "todo"

# A list of url patterns
urlpatterns: List[URLPattern] = [
    path("", view=views.index, name="index")
]