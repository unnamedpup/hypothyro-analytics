from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('average-age-of-operation', views.average_age_of_operation, name="average_age_of_operation"),
    path("gender-percentage", views.gender_percentage, name="gender_percentage"),
    path("most-frequent-drug-before-operation", views.most_frequent_drug_before_operation, name="most_frequent_drug_before_operation"),
    path("most-frequent-drug-after-operation", views.most_frequent_drug_after_operation, name="most_frequent_drug_after_operation"),
    path("most-frequent-operation-type", views.most_frequent_operation_type, name="most_frequent_operation_type"),
    path("most-frequent-pathology-name", views.most_frequent_pathology_name, name="most_frequent_pathology_name"),
]


