# Love the LORD your GOD with all mind and with all your soul and with
# all your might. And Love your neighbor as your self.
from django.test import TestCase
from .models import Activaties
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError


def activaties(
    title: str = "Codilng",
    activate_type: str = "TK",
    description: str = "Writing code for programming",
    is_activate_done: bool = False,
    published_time: datetime = timezone.now(),
):
    act = Activaties(
        title=title,
        activate_type=activate_type,
        description=description,
        is_activate_done=is_activate_done,
        published_time=published_time,
    )
    act.clean_fields()
    act.save()


# Create your tests here.
class TestActivaties(TestCase):
    def test_if_activate_is_not_empty(self):
        activaties()
        act_count = Activaties.objects.count()
        self.assertGreater(act_count, 0)

    def test_if_activate_throw_error_on_wrong_activate_type(self):
        with self.assertRaises(ValidationError):
            activaties(activate_type="act")


class TestUserInterface(TestCase):
    def setUp(self):
        self.get_todo = self.client.get("/todo/")

    def test_the_page_state(self):
        self.assertEqual(self.get_todo.status_code, 200)

    def test_page_title(self):
        self.assertTrue("Todo" in self.get_todo.content.decode())

    def test_page_description(self):
        self.assertIn("What's Today's Schedule", self.get_todo.content.decode())

    def test_if_input_exists(self):
        response = self.get_todo
        self.assertContains(response, "<form", count=1)
        self.assertContains(response, "<input")

    
    

