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

def li(object_list, class_=''):
    # Render list.html into HTML
    obj={
        'object_list': object_list,
    }
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/list.html', obj)

def p(content, class_=''):
    # Render paragraph.html into HTML
    obj={
        'content': content,
    }
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/paragraph.html', obj)

def table(header, rows, class_=''):
    # Render paragraph.html into HTML
    obj={
        'header': header,
        'rows': rows,
    }
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/table.html', obj)

def a(href, anchor, class_=''):
    # Render link.html into HTML
    obj={
        'href': href,
        'anchor': anchor,
    }
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/link.html', obj)