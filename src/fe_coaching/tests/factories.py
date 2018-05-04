import factory
from django.contrib.auth import get_user_model
from fe_core.factories import UserFactory, EntityFactory

from ..models import Session

User = get_user_model()


class SessionFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    entity = factory.SubFactory(EntityFactory)

    class Meta:
        model = Session
