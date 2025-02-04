from django.urls import path
from . import views
urlpatterns = [
    path('', views.render_tree_view, name='tree_view'),
    path('note/', views.note, name='note'),
    path('person/<int:person_id>/', views.person_detail, name='person_detail'),
    path('d3-collapsible-tree/', views.d3_collapsible_tree, name='d3_collapsible_tree'),
    path('import_data_from_csv/', views.import_data_from_csv, name='import_data_from_csv'),  
    path('generate_tree_data/', views.generate_tree_data, name='generate_tree_data'),
    path('search/', views.search_person, name='search_person'),
    path('tree_with_female/', views.tree_with_female, name='tree_with_female'),
]
