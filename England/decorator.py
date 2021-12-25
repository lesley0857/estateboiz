from .views import *
def returncleandata(view_func):
    def wrapper_func(*args,**kwargs):
        return formset.cleaned_data()
    return wrapper_func