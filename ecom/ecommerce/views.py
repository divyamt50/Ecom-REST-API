from rest_framework import viewsets, views
from rest_framework.response import Response
from ecommerce.models import Category, Products
from ecommerce.serializers import CategorySerializer, ProductsSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .helpers import send_otp_to_phone
from rest_framework.decorators import action

class SendOTPView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        
        if data.get('phone_number') is None:
            return Response({
                'status': 400,
                'message': 'Phone number is required'
            })
            
        if data.get('password') is None:
            return Response({
                'status': 400,
                'message': 'Key password is required'
            })
        
        category = Category.objects.create(
            phone_number=data.get('phone_number'),
            otp=send_otp_to_phone(data.get('phone_number'))
        )
        category.set_password = data.get('password')
        category.save()
        
        return Response({
            'status': 200,
            'message': 'OTP sent'
        })

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = request.data
        
        if data.get('phone_number') is None:
                return Response({
                    'status': 400,
                    'message': 'Phone number is required'
                })
        
        if data.get('otp') is None:
                return Response({
                    'status': 400,
                    'message': 'OTP is required'
                })
                
        
        category_objs = Category.objects.filter(phone_number = data.get('phone_number'))
        for category_obj in category_objs:
            if str(category_obj.otp) == str(data.get('otp')):
                category_obj.otp_verified = True
                category_obj.save()
                return Response({
                    'status': 200,
                    'message': 'OTP matched'
                })

        return Response({
            'status': 400,
            'message': 'Invalid OTP'
        })

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            prods = Products.objects.filter(prod_category=category)
            prods_serializer = ProductsSerializer(prods, many=True, context={'request': request})
            return Response(prods_serializer.data)
        except Category.DoesNotExist:
            return Response({
                'message': 'Category might not exist'
            })

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
