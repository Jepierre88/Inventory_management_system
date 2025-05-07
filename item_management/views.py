from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from .models import Item
from .serializers import ItemSerializer
from business_management.models import Business
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_item(request):
    user = request.user
    data = request.data.copy()

    # 1. WORKER: no necesita que el negocio venga en el request
    if user.user_type == 'WORKER':
        if not user.business:
            raise PermissionDenied("No tienes un negocio asignado.")
        data['business'] = str(user.business.id)

    # 2. CLIENT o SUPERADMIN: deben proporcionar el business
    else:
        business_id = data.get('business')
        if not business_id:
            return Response({"detail": "Debes proporcionar el ID del negocio."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            business = Business.objects.get(id=business_id)
        except Business.DoesNotExist:
            return Response({"detail": "Negocio no encontrado."},
                            status=status.HTTP_404_NOT_FOUND)

        if user.user_type == 'CLIENT' and not user.business_set.filter(id=business.id).exists():
            raise PermissionDenied("No puedes crear productos en un negocio que no te pertenece.")

    # 3. Serializar y guardar
    serializer = ItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

