from rest_framework import status
from rest_framework.views import APIView

from api.serializers import UUIDModelSerializer

from .models import UUIDModel
from .utils import Response


class GenerateUUIDView(APIView):

    serializer_class = UUIDModelSerializer

    def get(self, request):
        try:
            UUIDModel.objects.create()
            uuids = {}

            all_uuids = UUIDModel.objects.all().order_by('-created_at')
            serializer = self.serializer_class(all_uuids, many=True)

            for item in serializer.data:
                uuids[str(item['created_at'])] = item['id']

            return Response(data=uuids, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(errors={'msg': str(e)}, status=status.HTTP_400_BAD_REQUEST)
