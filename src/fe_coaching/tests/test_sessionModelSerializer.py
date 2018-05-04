from django.test import TestCase

from ..serializers import SessionSerializer


class TestSessionModelSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            'number': 54321,
            'date': '21/07/1978',
            'start': '10:00',
            'end': '11:00',
        }

    def test_data(self):
        serializer = SessionSerializer(data=self.serializer_data)
        serializer.is_valid()
        data = serializer.data
        assert set(data.keys()) == set(['number', 'date', 'start', 'end'])

    def test_is_valid(self):
        serializer = SessionSerializer(data=self.serializer_data)
        assert serializer.is_valid()
