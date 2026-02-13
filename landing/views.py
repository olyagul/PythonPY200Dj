from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import FormView
from .forms import PizzaOrderForm


class PizzaOrderView(FormView):
    template_name = 'landing/order.html'
    form_class = PizzaOrderForm
    success_url = '/'

    def form_valid(self, form):
        form_data = form.cleaned_data.copy()
        if 'extra' in form_data and form_data['extra']:
            extra_names = []
            for code in form_data['extra']:
                for choice in PizzaOrderForm.base_fields['extra'].choices:
                    if choice[0] == code:
                        extra_names.append(choice[1])
                        break
            form_data['extra'] = extra_names


        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')


        user_agent = self.request.META.get('HTTP_USER_AGENT', 'Неизвестно')


        response_data = {
            'status': 'success',
            'order_data': form_data,
            'client_info': {
                'ip_address': ip,
                'user_agent': user_agent,
            }
        }

        return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False, 'indent': 4})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


