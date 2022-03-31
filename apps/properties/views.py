import logging

from django.utils.translation import gettext_lazy as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import PropertyFilter
from .exceptions import PropertyNotFound
from .models import Property, PropertyViews
from .pagination import PropertyPagination
from .serializers import PropertyCreateSerializer, PropertySerializer, PropertyViewSerializer

logger = logging.getLogger(__name__)


class ListAllPropertiesAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = PropertyFilter
    search_fields = ('country', 'city')
    ordering_fields = ('created_at',)
    queryset = Property.objects.all().order_by('-created_at')


class ListAgentsPropertiesAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = PropertyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = PropertyFilter
    search_fields = ('country', 'city')
    ordering_fields = ('created_at',)

    def get_queryset(self):
        user = self.request.user
        queryset = Property.objects.filter(user=user).order_by('-created_at')
        return queryset


class PropertySearchView(generics.ListAPIView):
    serializer_class = PropertyViewSerializer
    queryset = Property.objects.all()


class PropertyDetailView(APIView):
    def get(self, request, slug):
        property = Property.objects.get(slug=slug)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if not PropertyViews.objects.filter(property=property, ip=ip).exists():
            PropertyViews.objects.create(property=property, ip=ip)
            property.views += 1
            property.save()

        serializer = PropertySerializer(property, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes((permissions.IsAuthenticated,))
def update_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    if property.user != request.user:
        return Response({'error': _('You cant update or edit a property that doesnt belong to you')},
                        status=status.HTTP_403_FORBIDDEN, )
    if request.method == 'PUT':
        serializer = PropertySerializer(property, request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def create_property_api_view(request):
    request.data._mutable = True
    request.data['user'] = request.user.pkid
    serializer = PropertyCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        logger.info(_(f'property {serializer.data.get("title")} created by {request.user.username}'))
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def delete_property_api_view(request, slug):
    try:
        property = Property.objects.get(slug=slug)
    except Property.DoesNotExist:
        raise PropertyNotFound

    if property.user != request.user:
        return Response({'error': _('You cant delete a property that doesnt belong to you')},
                        status=status.HTTP_403_FORBIDDEN)
    if request.method == 'DELETE':
        delete_operation = property.delete()
        data = {}
        if delete_operation:
            data['success'] = _('Deletion was successful')
        else:
            data['failure'] = _('Deletion failed')
        return Response(data=data)


@api_view(['POST'])
def uploadPropertyImage(request):
    property_id = request.data['property_id']
    property = Property.objects.get(id=property_id)
    property.main_photo = request.FILES.get('main_photo')
    property.photo1 = request.FILES.get('photo1')
    property.photo2 = request.FILES.get('photo2')
    property.photo3 = request.FILES.get('photo3')
    property.photo4 = request.FILES.get('photo4')
    property.save()
    return Response({'success': _('Image(s) uploaded')})


class PropertySearchAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PropertyCreateSerializer

    def post(self, request):
        queryset = Property.objects.filter(published_status=True, advert_type__iexact=self.request.data['advert_type'],
                                           property_type__iexact=self.request.data['property_type'])

        price = self.request.data['price']
        if price == '€0+':
            price = 0
        elif price == '€50,000+':
            price = 50000
        elif price == '€100,000+':
            price = 100000
        elif price == '€200,000+':
            price = 200000
        elif price == '€400,000+':
            price = 400000
        elif price == '€600,000+':
            price = 600000
        elif price == 'Any':
            price = -1

        if price != -1:
            queryset = queryset.filter(price__gte=price)

        bedrooms = self.request.data['bedrooms']
        if bedrooms == '0+':
            bedrooms = 0
        elif bedrooms == '1+':
            bedrooms = 1
        elif bedrooms == '2+':
            bedrooms = 2
        elif bedrooms == '3+':
            bedrooms = 3
        elif bedrooms == '4+':
            bedrooms = 4
        elif bedrooms == '5+':
            bedrooms = 5

        bathrooms = self.request.data['bathrooms']
        if bathrooms == '0+':
            bathrooms = 0.0
        elif bathrooms == '1+':
            bathrooms = 1.0
        elif bathrooms == '2+':
            bathrooms = 2.0
        elif bathrooms == '3+':
            bathrooms = 3.0
        elif bathrooms == '4+':
            bathrooms = 4.0

        queryset = queryset.filter(bedrooms__gte=bedrooms, bathrooms__gte=bathrooms,
                                   description__icontains=self.request.data['catch_phrase'])

        serializer = PropertySerializer(queryset, many=True)
        return Response(serializer.data)
