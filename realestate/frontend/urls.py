from django.urls import path

from . import views
# handler404 = 'frontend.views.handler404'

# handler500 = 'frontend.views.handler500'

# handler403 = 'frontend.views.page_not_found_view'

# handler400 = 'frontend.views.page_not_found_view'
urlpatterns = [
    path('', views.index, name='index'),
    #path('secret/', views.secret, name='secret'),
    #path('<int:id>/', views.bypass, name='detail'),
    # ex: /5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]