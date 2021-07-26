import traceback
from django.template.loader import render_to_string
import requests

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

def link(href, anchor, class_='', click_to_copy=False):
    # Render link.html into HTML
    obj={
        'href': href,
        'anchor': anchor,
    }
    if class_:
        obj['classname'] = class_
    if click_to_copy:
        obj['click_to_copy'] = True
    return render_to_string('partials/link.html', obj)


def heading2(text, class_=''):
    obj = {'heading2': text}
    if class_:
        obj['classname'] = class_
    return render_to_string('partials/heading.html',obj) 


def free_wrap(html, class_='', wrapper='div'):
    obj = {'element': html}
    if class_:
        obj['classname'] = class_
    if wrapper=='span':
        obj['span'] = True
    elif wrapper=='input':
        obj['input'] = True
    else:
        obj['div'] = True
    return render_to_string('partials/freewrap.html',obj) 

