from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, RFQ, Quotation, Vendor, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import ItemForm, RFQForm, QuotationForm, VendorForm
from django.contrib import messages
from .decorators import client_required, vendor_required
from django.db.models import Q, Count



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')  # 'client' or 'vendor'
        if form.is_valid() and user_type in ['client', 'vendor']:
            user = form.save()
            if user_type == 'vendor':
                Vendor.objects.create(user=user)
            else:
                Client.objects.create(user=user)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if hasattr(request.user, 'client'):
        return redirect('item_list')
    elif hasattr(request.user, 'vendor'):
        return redirect('rfq_list')
    else:
        return redirect('admin:index')


# Client Views
@login_required
@client_required
def item_list(request):
    items = Item.objects.filter(client=request.user.client)
    return render(request, 'core/item_list.html', {'items': items})


@login_required
@client_required
def item_add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.client = request.user.client
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'core/item_form.html', {'form': form})


@login_required
@client_required
def rfq_create(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')
        if item_ids:
            rfq = RFQ.objects.create(client=request.user.client)
            rfq.items.add(*item_ids)
            rfq.save()
            messages.success(request, 'RFQ created successfully.')
            return redirect('rfq_detail', pk=rfq.pk)
        else:
            messages.error(request, 'No items selected to create an RFQ.')
            return redirect('item_list')
    else:
        return redirect('item_list')


@login_required
def rfq_detail(request, pk):
    rfq = get_object_or_404(RFQ, pk=pk)

    if hasattr(request.user, 'client'):
        # Client access: Ensure the RFQ belongs to the client
        if rfq.client != request.user.client:
            messages.error(request, 'You do not have permission to view this RFQ.')
            return redirect('dashboard')
        quotations = Quotation.objects.filter(rfq=rfq)
        lowest_quotation = quotations.order_by('estimated_cost').first()
        return render(request, 'core/rfq_detail_client.html', {
            'rfq': rfq,
            'quotations': quotations,
            'lowest_quotation': lowest_quotation,
        })

    elif hasattr(request.user, 'vendor'):
        quotation = Quotation.objects.filter(rfq=rfq, vendor=request.user.vendor).first()
        if not quotation:
            messages.error(request, 'You do not have permission to view this RFQ.')
            return redirect('dashboard')
        return render(request, 'core/rfq_detail_vendor.html', {
            'rfq': rfq,
            'quotation': quotation,
        })

    else:
        # If the user is neither a client nor a vendor
        messages.error(request, 'You do not have permission to view this RFQ.')
        return redirect('dashboard')


@login_required
@client_required
def rfq_approve(request, pk):
    rfq = get_object_or_404(RFQ, pk=pk, client=request.user.client)
    lowest_quotation = Quotation.objects.filter(rfq=rfq, is_approved=False).order_by('estimated_cost').first()
    if lowest_quotation:
        lowest_quotation.is_approved = True
        lowest_quotation.save()
        messages.success(request, 'Lowest quotation has been approved.')
    else:
        messages.error(request, 'No available quotations to approve.')
    return redirect('rfq_detail', pk=pk)


# Vendor Views
@login_required
@vendor_required
def rfq_list(request):
    # RFQs with no approved quotations and vendor has not submitted a quotation
    rfqs = RFQ.objects.annotate(
        approved_quotation_count=Count('quotation', filter=Q(quotation__is_approved=True)),
        vendor_quotation_count=Count('quotation', filter=Q(quotation__vendor=request.user.vendor))
    ).filter(
        approved_quotation_count=0,
        vendor_quotation_count=0
    )
    return render(request, 'core/rfq_list.html', {'rfqs': rfqs})


# vendor views but with question was approved to track the approved quotation for the user
@login_required
@vendor_required
def rfq_approved_list(request):
    rfqs = RFQ.objects.filter(
        quotation__vendor=request.user.vendor,
        quotation__is_approved=True
    ).distinct()
    return render(request, 'core/rfq_approved_list.html', {'rfqs': rfqs})


@login_required
@vendor_required
def quotation_add(request, rfq_id):
    rfq = get_object_or_404(RFQ, pk=rfq_id)
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            quotation = form.save(commit=False)
            quotation.rfq = rfq
            quotation.vendor = request.user.vendor
            quotation.save()
            return redirect('rfq_list')
    else:
        form = QuotationForm()
    return render(request, 'core/quotation_form.html', {'form': form, 'rfq': rfq})


@login_required
def load_quotations(request, pk):
    rfq = get_object_or_404(RFQ, pk=pk)
    quotations = Quotation.objects.filter(rfq=rfq)
    return render(request, 'core/quotations_partial.html', {'quotations': quotations})


@login_required
@client_required
def rfq_list_client(request):
    # Retrieve all RFQs associated with the logged-in client
    rfqs = RFQ.objects.filter(client=request.user.client)
    return render(request, 'core/rfq_list_client.html', {'rfqs': rfqs})