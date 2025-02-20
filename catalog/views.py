from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy("users:login")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user

        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = "catalog/product_delete_confirm.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy('catalog:product_list')
