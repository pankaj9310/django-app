from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.auth import views as auth_views

from nimoy.users.views import role_assign, users_list, user_profile, user_update
from allauth.account.views import confirm_email as allauthemailconfirmation
from nimoy.projects.views import ProjectList, CreateProject, ProjectDetails, ProjectUpdate, ProjectList
from nimoy.tasks.views import TaskList, CreateTask, TaskDetails, TaskUpdate, TaskList
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),

    # # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # # User management
    url(r'^users/', include('nimoy.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^add-project/$', CreateProject.as_view(), name="add-project"),
    
    url(r'^project/(?P<pk>\d+)/$', ProjectDetails.as_view(), name="project_detail"),
    url(r'^project/(?P<pk>\d+)/edit/$', ProjectUpdate.as_view(), name="project_update"),
    url(r'^projects/$', ProjectList.as_view(), name='project_list'),
    url(r'^add-task/(?P<pk>\d+)', CreateTask.as_view(), name="add_task"),
    url(r'^task/(?P<pk>\d+)/$', TaskDetails.as_view(), name="task_detail"),
    url(r'^task/(?P<pk>\d+)/edit/$', TaskUpdate.as_view(), name="task_update"),
    url(r'^tasks/$', TaskList.as_view(), name='task_list'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
