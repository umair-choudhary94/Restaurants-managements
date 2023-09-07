
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("register",views.register,name="register"),
    path("login",views.login_user,name="loginUser"),
    path("logout",views.logout_user,name="logoutuser"),
    path("signup",views.signup,name="signup"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path("help",views.help,name="help"),
    path("search",views.search,name="search"),
    path("catsearch",views.catsearch,name="catsearch"),
    path("searchfood",views.searchfood,name="searchfood"),
    path("tables/<int:id>/",views.tables,name="tables"),
    path("booknow/<int:res>/<int:tb>/",views.booknow,name="booknow"),
    path("orderfood/<int:id>/",views.orderfood,name="orderfood"),
    path("restaurants/<int:id>/",views.visitresturants,name="visitresturants"),
]