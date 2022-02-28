from rest_framework.views import APIView
from .serializers import *
from user.responses import *
from .filters import *

def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None


class CategoryView(APIView):

    def __init__(self, **kwargs) -> None:
        self.MODEL = Category
        self.SERIALIZER = CategorySerializer
        self.FILTER = CategoryFilter
        self.FILTER_FIELDS = [
            'created_at_max',
            'created_at_min',
            'name'
        ]
        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=queryset)
        queryset = filter.qs
        serializer = self.SERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, status=ResponseSuccess)

    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')


class ProductView(APIView):

    def __init__(self, **kwargs) -> None:
        self.MODEL = Product
        self.SERIALIZER = ProductSerializer
        self.GETSERIALIZER = ProductGetSerializer
        self.FILTER = ProductFilter
        self.FILTER_FIELDS = [
            'category',
            'min_price',
            'max_price',
            'name',
            'size'
        ]
        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=queryset)
        queryset = filter.qs
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, status=ResponseSuccess)

    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')


class CardView(APIView):

    def __init__(self, **kwargs) -> None:
        self.MODEL = Card
        self.SERIALIZER = CardSerializer
        self.GETSERIALIZER = ProductGetSerializer
        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, status=ResponseSuccess)

    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')


class OrderView(APIView):

    def __init__(self, **kwargs) -> None:
        self.MODEL = Product
        self.SERIALIZER = ProductSerializer
        self.GETSERIALIZER = ProductGetSerializer

        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, status=ResponseSuccess)

    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)

            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')


class OrderProductView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = OrderProduct
        self.SERIALIZER = OrderProductSerializer
        self.GETSERIALIZER = OrderProductGetSerializer

        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, status=ResponseSuccess)

    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')