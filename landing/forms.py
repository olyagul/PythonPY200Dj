from django import forms

PIZZA_CHOICES = [
    ('margherita', 'Маргарита'),
    ('pepperoni', 'Пепперони'),
    ('hawaiian', 'Гавайская'),
    ('four_cheese', 'Четыре сыра'),
    ('meat', 'Мясная'),
]

# Размер пиццы
SIZE_CHOICES = [
    ('small', 'Маленькая (25 см)'),
    ('medium', 'Средняя (30 см)'),
    ('large', 'Большая (35 см)'),
]

# доп. ингредиенты
EXTRA_CHOICES = [
    ('cheese', 'Двойной сыр'),
    ('mushrooms', 'Грибы'),
    ('olives', 'Оливки'),
    ('bacon', 'Бекон'),
    ('pineapple', 'Ананас'),
]


class PizzaOrderForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'})
    )

    phone = forms.CharField(
        max_length=20,
        label='Телефон',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'})
    )

    address = forms.CharField(
        max_length=200,
        label='Адрес доставки',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Улица, дом, квартира'})
    )

    pizza_choice = forms.ChoiceField(
        choices=PIZZA_CHOICES,
        label='Выберите пиццу',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        label='Выберите размер',
        widget=forms.RadioSelect
    )

    extra = forms.MultipleChoiceField(
        choices=EXTRA_CHOICES,
        label='Дополнительные ингредиенты',
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    comment = forms.CharField(
        label='Комментарий к заказу',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Особые пожелания...'}),
        required=False
    )