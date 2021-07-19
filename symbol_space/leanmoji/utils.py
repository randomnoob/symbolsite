from django.template.loader import render_to_string


def card(title, body, class_=''):
    # Render card.html into HTML
    obj={
        'title': title,
        'body': body,
    }
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/card.html', obj)

