from django.urls import path

from leads.views import home_page, view_leads,get_lead_details_by_index,lead_create, lead_update_view,lead_delete_view

app_name = "leads"

urlpatterns = [
    path('landing', home_page, name='home'),
    path('view/', view_leads, name='view_leads'),
    path('<int:pk>', get_lead_details_by_index, name='lead_details'),
    path('create', lead_create, name='lead_create'),
    path('<int:pk>/update/', lead_update_view, name='lead_update'),
    path('<int:pk>/delete/', lead_delete_view, name='lead_delete'),
]
