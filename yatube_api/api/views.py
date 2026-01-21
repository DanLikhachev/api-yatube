from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class ViewSetMixin(viewsets.ModelViewSet):

    def update(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.get_serializer(
            object,
            data=request.data,
            partial=True
        )

        if object.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)

        return Response(status=HTTPStatus.BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        object = self.get_object()

        if object.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)

        serializer = self.get_serializer(
            object,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()

        if object.author != request.user:
            return Response(status=HTTPStatus.FORBIDDEN)
        else:
            self.perform_destroy(object)
            return Response(status=HTTPStatus.NO_CONTENT)


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
        related_post = self.kwargs.get('post')
        comments = Comment.objects.filter(post=related_post)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
