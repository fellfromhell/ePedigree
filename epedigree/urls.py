__author__ = 'vivincyriac'
from django.conf.urls import patterns, include, url
from epedigree.views import ItemListView, ItemDetailView, ItemCreateView, \
    OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, OrderLinesCreateView, OrderLinesDeleteView, \
        LotListView, LotCreateView, LotDetailView, LotUpdateView, LotTransCreateView, ClientListView, ClientDetailView, \
        ClientCreateView, LotTransDeleteView, PedigreeDetailView, client_search, LotCertifyView, index

urlpatterns = patterns('',
        # url(r'^food/$', food_list, name='food-list'),

        url(r'^clients/$', ClientListView.as_view(), name='client-list'), #list of items
        url(r'^clients/(?P<pk>\d+)$', ClientDetailView.as_view(), name='client-detail'),
        url(r'^clients/create$', ClientCreateView.as_view(), name='client-create'),
        url(r'^clients/search/$', "epedigree.views.submit_color_search_from_ajax", name="client-list2"),
        url(r"^clients/like_color_(?P<color_id>\d+)/$", "epedigree.views.toggle_client_like", name="toggle_client_like"),
        url(r'^items/$', ItemListView.as_view(), name='item-list'), #list of items
        url(r'^items/(?P<pk>\d+)$', ItemDetailView.as_view(), name='item-detail'),#detail of item
        url(r'^items/create$', ItemCreateView.as_view(), name='item-create'), #create new item



        url(r'^orders/$', OrderListView.as_view(), name='order-list'),
        url(r'^orders/new/$', OrderCreateView.as_view(), name='order-create'),
        url(r'^orders/(?P<pk>\d+)$', OrderDetailView.as_view(), name='order-detail'),
        url(r'^orders/(?P<pk>\d+)/update$', OrderUpdateView.as_view(), name='order-update'),

        url(r'^orders/(?P<pk>\d+)/add_orderline/$', OrderLinesCreateView.as_view(), name='orderline-create'),
        url(r'^orders/(?P<pk2>\d+)/remove_orderline/(?P<pk>\d+)/$', OrderLinesDeleteView.as_view(), name='orderline-delete'),

        url(r'^orders/(?P<pk2>\d+)/pedigree/(?P<pk>\d+)/$', PedigreeDetailView, name='pedigree-detail'),

        url(r'^lot/$', LotListView.as_view(), name='lot-list'),
        url(r'^lot/new/$', LotCreateView.as_view(), name='lot-create'),
        url(r'^lot/(?P<pk>\d+)$', LotDetailView.as_view(), name='lot-detail'),
        url(r'^lot/(?P<pk>\d+)/update$', LotUpdateView.as_view(), name='lot-update'),
        url(r'^lot/(?P<pk>\d+)/certify$', LotCertifyView.as_view(), name='lot-certify'),

        url(r'^lot/(?P<pk>\d+)/add_lottrans/$', LotTransCreateView.as_view(), name='lottrans-create'),
        url(r'^lot/(?P<pk2>\d+)/remove_lottrans/(?P<pk>\d+)/$', LotTransDeleteView.as_view(), name='lottrans-delete'),
        url(r"^$", index, name='index'),

        # url(r"^like_color_(?P<color_id>\d+)/$", "epedigree.views.toggle_color_like", name="toggle_color_like"),


        )