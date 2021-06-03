from django.urls import path
from mobileapp.views import create_brand,list_all_brands,delete_brand,index,update_brand
urlpatterns=[
    path("owner/brands",create_brand,name="createbrands"),
    path('owner/',index,name="home"),
    path("owner/list",list_all_brands,name="listbrands"),
    path("owner/delete/<int:id>",delete_brand,name="deletebrand"),
    path("owner/update/<int:id>",update_brand,name="updatebrand")
]
