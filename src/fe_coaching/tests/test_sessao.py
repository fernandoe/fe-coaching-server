from django.test import TestCase
from fe_core.factories import UserFactory, EntityFactory

from .factories import SessionFactory


class TestSessao(TestCase):
    def setUp(self):
        self.email = 'test62737@example7464.com'
        self.user = UserFactory(email=self.email)
        self.entity = EntityFactory()

    def test_factory(self):
        session = SessionFactory()
        assert session is not None

    def test__str__(self):
        task = SessionFactory(user=self.user, number=123)
        assert f'{self.email}#123' == str(task)
