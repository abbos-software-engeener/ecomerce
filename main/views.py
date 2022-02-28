from django.shortcuts import render
from rest_framework.views import APIView

from api.views import get_object_or_None
from user.responses import *
from .serializers import *


class PostCommentView(APIView):

    def __init__(self, **kwargs) -> None:
        self.MODEL = Post_Comment
        self.SERIALIZER = PostCommentSerializer
        self.GETSERIALIZER = PostCommentGetSerializer

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


class CantactView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Contact
        self.SERIALIZER = ContactSerializer
        super().__init__(**kwargs)

    def list(self, request):
        queryset = self.MODEL.objects.all()
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

