from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from epedigree.models import Item, Order, OrderLines, Lot, LotTransactions, Client, UserProfile
from epedigree.forms import ItemPostForm, OrderPostForm, \
    OrderLinesPostForm, LotPostForm, LotTransactionsPostForm, ClientPostForm, LotCertifyForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# create your views here.


def index(request):

    return render_to_response('index.html', context_instance=RequestContext(request))



class ClientListView(ListView):
    model = Client
    breadcrumbs = ['client']

    context_object_name = "colors"

    # VALID_SORTS = {
    #     "pk": "pk",
    #     "pkd": "-pk",
    #     "em": "eminence",
    #     "emd": "-eminence",
    # }
    # DEFAULT_SORT = 'pk'
    #         sort_key = request.GET.get('sort', DEFAULT_SORT) # Replace pk with your default.
    #     sort = VALID_SORTS.get(sort_key, DEFAULT_SORT)
    #
    #     eList = Employer.objects.filter(eminence__lt=4).order_by(sort)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """
        Returns the all colors, for display in the main table. The search
        result query set, if any, is passed as context.
        """
        return super(ClientListView, self).get_queryset()

    def get_context_data(self, **kwargs):
        #The current context.
        context = super(ClientListView, self).get_context_data(**kwargs)

        context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS

        return context


@login_required
def submit_color_search_from_ajax(request):
    """
    Processes a search request, ignoring any where less than two
    characters are provided. The search text is both trimmed and
    lower-cased.

    See <link to MIN_SEARCH_CHARS>
    """

    colors = []  #Assume no results.

    global  MIN_SEARCH_CHARS

    search_text = ""   #Assume no search
    if(request.method == "GET"):
        search_text = request.GET.get("color_search_text", "").strip().lower()
        if(len(search_text) < MIN_SEARCH_CHARS):
            """
            Ignore the search. This is also validated by
            JavaScript, and should never reach here, but remains
            as prevention.
            """
            search_text = ""

    #Assume no results.
    #Use an empty list instead of None. In the template, use
    #   {% if color_search_results.count > 0 %}
    color_results = []

    if(search_text != ""):
        color_results = Client.objects.filter(cName__icontains=search_text)

    #print('search_text="' + search_text + '", results=' + str(color_results))

    context = {
        "search_text": search_text,
        "color_search_results": color_results,
        "MIN_SEARCH_CHARS": MIN_SEARCH_CHARS,
    };

    return render_to_response("epedigree/color_search_results__html_snippet.txt",
                               context)


class ClientDetailView(DetailView):
    model = Client
    breadcrumbs = ['client']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientDetailView, self).dispatch(*args, **kwargs)


class ClientCreateView(CreateView):
    template_name = 'epedigree/client_form.html'
    model = Client
    form_class = ClientPostForm
    breadcrumbs = ['client']

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ClientCreateView, self).dispatch(*args, **kwargs)


class ItemListView(ListView):
    model = Item
    breadcrumbs = ['item']

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemListView, self).dispatch(*args, **kwargs)


class ItemDetailView(DetailView):
    model = Item
    breadcrumbs = ['item']

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemDetailView, self).dispatch(*args, **kwargs)


class ItemCreateView(CreateView):
    template_name = 'epedigree/item_form.html'
    model = Item
    form_class = ItemPostForm
    breadcrumbs = ['item']

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(ItemCreateView, self).dispatch(*args, **kwargs)


class OrderListView(ListView):
    model = Order
    breadcrumbs = ['order']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderListView, self).dispatch(*args, **kwargs)


class OrderDetailView(DetailView):
    model = Order
    breadcrumbs = ['order']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderDetailView, self).dispatch(*args, **kwargs)


class OrderCreateView(CreateView):
    template_name = 'epedigree/order_form.html'
    model = Order
    form_class = OrderPostForm
    breadcrumbs = ['order']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(OrderCreateView, self).dispatch(*args, **kwargs)


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderPostForm
    template_name = "epedigree/order_update_form.html"
    breadcrumbs = ['order']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(OrderUpdateView, self).dispatch(*args, **kwargs)


class OrderLinesCreateView(CreateView):
    model = OrderLines
    form_class = OrderLinesPostForm
    template_name = "epedigree/orderlines_form.html"
    breadcrumbs = ['order']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(OrderLinesCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self, *args, **kwargs):
        order = Order.objects.get(pk=self.kwargs['pk'])
        return {'order': order}

    def get_success_url(self):
        return reverse('order-detail', args=[self.kwargs['pk']])


class OrderLinesDeleteView(DeleteView):
    model = OrderLines
    breadcrumbs = ['order']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(OrderLinesDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('order-detail', args=[self.kwargs['pk2']])


class LotListView(ListView):
    model = Lot
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotListView, self).dispatch(*args, **kwargs)


class LotDetailView(DetailView):
    model = Lot
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotDetailView, self).dispatch(*args, **kwargs)


class LotCreateView(CreateView):
    template_name = 'epedigree/lot_form.html'
    model = Lot
    form_class = LotPostForm
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotCreateView, self).dispatch(*args, **kwargs)


class LotUpdateView(UpdateView):
    model = Lot
    form_class = LotPostForm
    template_name = "epedigree/lot_update_form.html"
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotUpdateView, self).dispatch(*args, **kwargs)

class LotCertifyView(UpdateView):
    model = Lot
    form_class = LotCertifyForm
    template_name = "epedigree/lot_update_form.html"
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotCertifyView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        lot = form.save(commit=False)
        lot.user = User.objects.get(username=self.request.user)
        lot.save()
        return HttpResponseRedirect(self.get_success_url())

class LotTransCreateView(CreateView):
    model = LotTransactions
    form_class = LotTransactionsPostForm
    template_name = "epedigree/lottrans_form.html"
    breadcrumbs = ['lot']


    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotTransCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self, *args, **kwargs):
        lot = Lot.objects.get(pk=self.kwargs['pk'])
        return {'lot': lot}

    def get_success_url(self):
        return reverse('lot-detail', args=[self.kwargs['pk']])


class LotTransDeleteView(DeleteView):
    model = LotTransactions
    breadcrumbs = ['lot']

    @method_decorator(staff_member_required)  #staff member
    def dispatch(self, *args, **kwargs):
        return super(LotTransDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('lot-detail', args=[self.kwargs['pk2']])


@login_required
def PedigreeDetailView(request, pk2, pk):
    order = Order.objects.get(id=pk2)
    orderline = OrderLines.objects.get(id=pk)
    lot = Lot.objects.get(id=orderline.lotnum_id)
    lottrans = LotTransactions.objects.all().filter(lot=lot)
    return render(request, 'epedigree/pedigree_detail.html', {'object': order, 'orderline': orderline, 'lot': lot, 'lottrans': lottrans})


@login_required(login_url='accounts:login')
def client_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''

    clients = Client.objects.filter(cName__contains=search_text)

    return render_to_response('epedigree/client_search.html', {'clients': clients})


from django.shortcuts     import redirect
from django.views.generic import ListView
from epedigree.models   import Color

MIN_SEARCH_CHARS = 2
"""
The minimum number of characters required in a search. If there are less,
the form submission is ignored. This value is used by the below view and
the template.
"""


@login_required
def toggle_client_like(request, color_id):
    """Toggle "like" for a single color, then refresh the color-list page."""
    color = None
    try:
        #There's only one object with this id, but this returns a list
        #of length one. Get the first (index 0)
        color = Client.objects.filter(clientID=color_id)[0]
    except Color.DoesNotExist as e:
        raise  ValueError("Unknown color.id=" + str(color_id) + ". Original error: " + str(e))

    #print("pre-toggle:  color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")

    color.is_favorited = not color.is_favorited
    color.save()  #Commit the change to the database

    #print("post-toggle: color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")

    return render_to_response("epedigree/color_like_link__html_snippet.txt",
                           {"color": color})