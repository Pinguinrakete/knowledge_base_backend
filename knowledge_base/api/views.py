from knowledge_base.models import Data
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DataSerializer


class DataView(APIView):
    def get(self, request):
        try:
            datas = Data.objects.all()

            if not datas.exists():
                return Response(
                    {"message": "Keine Daten gefunden"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = DataSerializer(
                datas,
                many=True,
                context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = DataSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
