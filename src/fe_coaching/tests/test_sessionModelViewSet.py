from dateutil import parser
from django.urls import reverse
from fe_core.factories import UserFactory, EntityFactory
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

from ..models import Session

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

EXAMPLE_DATA = {
    'number': 321,
    'date': '21/07/1978',
    'start': '12:31',
    'end': '13:41',
    'content': 'test content'
}


class TestSessionModelViewSet(APITestCase):

    def setUp(self):
        self.entity = EntityFactory()
        self.user = UserFactory(entity=self.entity)
        payload = jwt_payload_handler(self.user)
        user_token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token)

    def test_response_201(self):
        response = self.client.post(reverse('session-list'), EXAMPLE_DATA)
        assert status.HTTP_201_CREATED == response.status_code
        session = Session.objects.first()
        data = response.data
        assert 7 == len(data)
        assert str(session.uuid) == data['uuid']
        assert session.number == data['number']
        assert session.date == parser.parse(data['date']).date()
        assert session.start == parser.parse(data['start']).time()
        assert session.end == parser.parse(data['end']).time()
        assert session.entity == self.entity
        assert session.user == self.user

    def test_anonymous_user(self):
        self.client.logout()
        response = self.client.post(reverse('session-list'), EXAMPLE_DATA)
        assert status.HTTP_403_FORBIDDEN == response.status_code
