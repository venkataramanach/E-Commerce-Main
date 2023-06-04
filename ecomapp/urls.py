from django.urls import path
from .views import *
from . import views


app_name = "ecomapp"
urlpatterns = [

    # Client side pages
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(), name="allproducts"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="productdetail"),
    path("stores/",views.getStore,name="stores"),

    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
    path("my-cart/", MyCartView.as_view(), name="mycart"),
    path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
    path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),

    path("checkout/", CheckoutView.as_view(), name="checkout"),

    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),

    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),

    path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),

    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),

    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),

    path("search/", SearchView.as_view(), name="search"),

    path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
    path("password-reset/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),
    # Admin Side pages

    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),

    path("admin-all-orders/", AdminOrderListView.as_view(), name="adminorderlist"),

    path("admin-order-<int:pk>-change/",
         AdminOrderStatuChangeView.as_view(), name="adminorderstatuschange"),

    path("admin-product/list/", AdminProductListView.as_view(),
         name="adminproductlist"),
    path("admin-product/add/", AdminProductCreateView.as_view(),
         name="adminproductcreate"),
    path('KLUStat',views.KLStat,name="klu_stat"),
    path('KLU_Groc',views.KLGroc,name="klu_groc"),

    path('Gtr_Groc',views.GtrGroc,name="gtr_groc"),
    path('gtr_stat',views.GtrStat,name="gtr_stat"),
    path('Gtr_electronics',views.GtrElec,name="gtr_elec"),
    path('Gtr_Cloth',views.GtrCloth,name="gtr_cloth"),
    path('Gtr_Home',views.GtrHome,name="gtr_home"),

    path('Vjw_Groc',views.VjwGroc,name="vjw_groc"),
    path('Vjw_stat',views.VjwStat,name="vjw_stat"),
    path('Vjw_elec',views.VjwElec,name="vjw_elec"),
    path('Vjw_Cloth',views.VjwCloth,name="vjw_cloth"),
    path('Vjw_Home',views.VjwHome,name="vjw_home"),
    path('pie_chart',views.pie_chart,name="pie_chart"),
    path('stationery',views.StationaryProducts,name="stationary"),
    path('category/<str:cat>',views.GetCategory,name="get_category"),
    #path('category/<str:cat>',views.filter_data,name='filter_data'),
    path('sort_lh/<str:cat>',views.sort_lh,name="sort_lh"),
    path('sort_hl/<str:cat>',views.sort_hl,name="sort_hl"),
]
