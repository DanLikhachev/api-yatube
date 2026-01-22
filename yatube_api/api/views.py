# Python Standard Libraries
from http import HTTPStatus

# Django core
from django.shortcuts import get_object_or_404

# Third party libraries (related or not to Django)
from rest_framework import viewsets
from rest_framework.response import Response

# First party libraries (that is, our project’s imports)
from posts.models import Comment, Group, Post

# Local imports
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class ViewSetMixin(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(
            item,
            data=request.data,
            partial=False
        )

        if item.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)
        serializer.is_valid()
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(
            item,
            data=request.data,
            partial=True
        )

        if item.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)
        serializer.is_valid()
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()

        if item.author == request.user:
            super().destroy(request, *args, **kwargs)
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(status=HTTPStatus.FORBIDDEN)


class PostViewSet(ViewSetMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class CommentViewSet(ViewSetMixin):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post')
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)
