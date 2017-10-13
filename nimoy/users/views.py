from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, api_view

from rolepermissions.checkers import has_role
from rolepermissions.roles import assign_role, remove_role

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


@api_view(['POST', 'DELETE'])
@authentication_classes((TokenAuthentication,))
def role_assign(request, user_id):
    if not request.user.is_superuser:
        return Response(status=status.HTTP_403_FORBIDDEN)
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        assign_role(user, 'judge')
    elif request.method == 'DELETE':
        remove_role(user, 'judge')
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def users_list(request):
    if not request.user.is_superuser:
        return Response(status=status.HTTP_403_FORBIDDEN)
    User = get_user_model()
    users = User.objects.all()
    return Response([{'id':x.id, 'username': x.username, 'email': x.email} for x in users],status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def user_profile(request):
    User = get_user_model()
    try:
        user = User.objects.get(pk=request.user.id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response([{'id':user.id, 'first_name':user.first_name, 'last_name':user.last_name,
            'username': user.username, 'email': user.email }],status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def user_update(request):
    User = get_user_model()
    try:
        user = User.objects.get(pk=request.user.id)
        import pdb
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.save()
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response([{'id':user.id, 'first_name':user.first_name, 'last_name':user.last_name,
            'username': user.username, 'email': user.email }],status=status.HTTP_200_OK)
