from rest_framework.test import APITestCase


class GenerateUUIDViewTest(APITestCase):
    def test_generate_uuid_view(self):
        '''
        GIVEN that a request is made to /api/uuids endpoint
        WHEN GenerateUUIDView is called
        THEN a response is returned with a 200 status code
        '''
        response = self.client.get('/api/v1/uuids')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'success')
        self.assertEqual(type(response.data['data']), dict)
        self.assertEqual(response.data['errors'], None)
