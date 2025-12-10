from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics, permissions
from django.conf import settings
from django.db.models import Q
from .models import Post
from rest_framework.pagination import PageNumberPagination

class PostViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, destroy for posts.
    Supports search by title and content and ordering by created_at.
    """
    queryset = Post.objects.all().select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def recent_comments(self, request, pk=None):
        post = self.get_object()
        recent = post.comments.order_by('-created_at')[:5]
        serializer = CommentSerializer(recent, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for comments. Listing comments globally (or filter by post via ?post=<id>).
    Only comment authors can edit/delete their own comments.
    """
    queryset = Comment.objects.all().select_related('author', 'post')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.request.query_params.get('post')
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedPagination(PageNumberPagination):
    page_size = 10

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user
        # posts by users this user follows OR the user's own posts (optional)
        following_ids = user.following.values_list('id', flat=True)
        # include self posts optionally:
        qs = Post.objects.filter(author__id__in=list(following_ids))
        # If you want the feed to include user's own posts:
        # qs = Post.objects.filter(Q(author__id__in=list(following_ids)) | Q(author=user))
        return qs.order_by('-created_at')
Post.objects.filter(author__in=following_users).order_by, following.all()
