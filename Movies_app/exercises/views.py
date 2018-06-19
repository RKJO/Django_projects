from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from exercises.models import *
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from random import randint
# Create your views here.

html = """<html>
                <body>
                    """

def articles(request):
    article = Article.objects.filter(status=2)
    value = ""
    for art in article:
        value += html.format(art.title, art.author, art.date_added)
    return HttpResponse(value)


def show_band(request, id):
    band = Band.objects.get(id=id)
    result = " <h2> Band name: {}, Genre: {}, Year: {}, Active: {}, <br/>".format(band.name, band.genre, band.year, band.still_active)
    albums = band.album_set.all()
    for album in albums:
        result += "{}, {}, {}".format(album.title, album.year, album.rating)
        for song in album.song_set.all():
            result += "<br/>"
            result += "<p>{}<p/>".format(song.title)
            result += "<p>{}<p/>".format(song.album)

    return HttpResponse(result)


def show_range(request, start, end):
    result = html
    if request.method == "GET":
        # start_value = int(request.GET.get("start"))
        start_value = int(start)
        # end_value = int(request.GET.get("end"))
        end_value = int(end)
        for i in range(start_value, end_value + 1):
            result += "{}, ".format(str(i))
    result += """<body/>
                        <html/>"""

    return HttpResponse(result)


def show_multiplication(request, height, width):
    result = html + "<table border=1px>"
    # if request.method == "GET":
    # value_1 = request.GET.get("height")
    value_1 = height
    # value_2 = request.GET.get("width")
    value_2 = width
    if not value_1 or not value_2:
        result = "Nie podano parametru"
    else:
        for row in range(1, int(value_1) + 1):
            result += "<tr>"
            for col in range(1, int(value_2) + 1):
                result += "<td>{}</td>".format(row * col)
            result += "</tr>"

    result += """</table>
                    </body>
                        </html>"""

    # height = request.GET.get("height")
    # width = request.GET.get("width")
    # if not height or not width:
    #     answer = "Parameters are missing"
    # else:
    #     answer = "<html><head></head><body><table>"
    #     for i in range(1, int(height)+1):
    #         answer += "<tr>"
    #         for j in range(1, int(width)+1):
    #             answer += "<td>{}</td>".format(i*j)
    #         answer += "</tr>"
    #     answer += "</table></body></html>"

    return HttpResponse(result)


@csrf_exempt
def hello(request):
    result = html
    if request.method == "GET":
        result += """<form action="#" method="POST">
                        First name:<br>
                        <input type="text" name="firstname"><br>
                        Last name:<br>
                        <input type="text" name="lastname"><br>
                        <input type="submit" value="Wyślij">
                    </form>"""
    elif request.method == "POST":
        name = request.POST.get("firstname")
        surname = request.POST.get("lastname")
        result += "Witaj, {} {}!".format(name, surname)

    result += """</table>
                        </body>
                            </html>"""

    return HttpResponse(result)


@csrf_exempt
def temp_convert(request):
    result = html
    if request.method == "GET":
        result += """<form action="#" method="POST">
                        <label>
                            Temperatura:
                            <input type="number" min="0.00" step="0.01" name="degrees">
                        </label>
                            <input type="submit" name="convertionType" value="celcToFahr">
                            <input type="submit" name="convertionType" value="FahrToCelc">
                        </form>"""
    if request.method == "POST":
        degrees = float(request.POST.get("degrees"))
        convertionType = request.POST.get("convertionType")
        if convertionType == "celcToFahr":
            unit = "°F"
            after_conversion = 32 + (9/5) * degrees
        elif convertionType == "FahrToCelc":
            unit = "°C"
            after_conversion = 5/9 * (degrees - 32)
        result += "{:.1f} {}".format(after_conversion, unit)
    result += """</table>
                    </body>
                        </html>"""

    return HttpResponse(result)


def setSession(request):
    if request.session.get('counter') is None:
        result = "Counter is not set"
        request.session['counter'] = 0
        result += ", and i set it on 0"
    else:
        result = "Counter has already set"

    return HttpResponse(result)


def showSession(request):
    if request.session.get('counter') is None:
        result = "Counter is not set!"
    else:
        request.session['counter'] += 1
        counter = request.session.get('counter')
        result = "Counter: {}".format(counter)

    return HttpResponse(result)


def deleteSession(request):
    if request.session.get('counter') is None:
        result = "Counter is not set"
    elif request.session['counter'] is not None:
        counter = request.session.pop('counter')
        result = "Counter was: {} and it was deleted".format(counter)

    return HttpResponse(result)


def logout(request):
    if request.session.get('loggedUser') is None:
        result = "loggedUser is not set"
    elif request.session['loggedUser'] is not None:
        counter = request.session.pop('loggedUser')
        result = "loggedUser was: {} and it was deleted".format(counter)

    return HttpResponse(result)


@csrf_exempt
def login(request):
    response = HttpResponse()
    result = html
    if request.method == "GET":
        if request.session.get('loggedUser') is None:
            cookie_name = request.COOKIES.get("User")
            if cookie_name is None:
                cookie_name = ""
            result += """
                <form action="#" method="POST">
                    <label>
                        Imię:
                        <input type="text" name="name" value="{}">
                    </label>
                        <input type="submit" name="convertionType"><br>
                    <label>
                    <input type="checkbox" name="remember_me" >Remember Me
                    </label>
                        </form>""".format(cookie_name)
        else:
            loggedUser = request.session.get('loggedUser')
            result += "Witaj {}".format(loggedUser)
    elif request.method == "POST":
        name = request.POST.get('name')
        remember_me = request.POST.get('remember_me')
        request.session['loggedUser'] = name
        if remember_me:
            response.set_cookie("User", name)
        result = "Witaj {}".format(name)

    response.write(result)
    return response



@csrf_exempt
def addToSession(request):
    result = html
    if request.method == "GET":
        result += """<form action="#" method="POST">
                        <label>
                            Klucz:
                            <input type="text" name="key">
                        </label>
                        <label>
                            Wartość:
                            <input type="text" name="value">
                        </label>
                        <input type="submit" value="Wyślij">
                        </form>"""
    elif request.method == "POST":
        key = request.POST.get('key')
        value = request.POST.get('value')
        request.session[str(key)] = value
        result += "{}: {} - dodane do sesji".format(key, value)
    return HttpResponse(result)


def show_all_session_values(request):
    answer = html
    for key, values in request.session.items():
        answer += "<tr><td>{}</td><td>{}</td></td>".format(key, values)
    answer += "</body></html>"
    return HttpResponse(answer)


def set_cookie(request):
    response = HttpResponse("<p>Caisteczko ustawione</p>")
    print(response)
    response.set_cookie("User", "Rafal")
    return response


def show_cookie(request):
    if request.COOKIES['User'] is None:
        answer = "<p>Cookie doesn't exist!</p>"
    else:
        answer = request.COOKIES.get("User")
    return HttpResponse(answer)


def delete_cookie(request):
    if request.COOKIES['User'] is None:
        answer = "<p>Cookie doesn't exist!</p>"
    else:
        answer = request.COOKIES.pop('User')
    return HttpResponse(answer)


def display_form():
    form = """
        <form action="#" method="POST">
    <label>
        Klucz:
        <input type="text" name="key">
    </label>
    <label>
        Wartość:
        <input type="text" name="value">
    </label>
    <input type="submit" value="Wyślij">
    </form>
    """
    return form


@csrf_exempt
def addToCookie(request):
    response = HttpResponse()
    result = html
    if request.method == "GET":
        result += display_form()
    elif request.method == "POST":
        key_user = request.POST.get('key')
        value_user = request.POST.get('value')
        response.set_cookie(str(key_user)), value_user
        result = 'Cookie: {} added!'.format(key_user, value_user)
        response.write(result)
        return response


@method_decorator(csrf_exempt, name='dispatch')
class AddToCookie(View):
    def get(self, request):
        return HttpResponse(display_form())

    def post(self, request):
        response = HttpResponse()
        key_user = request.POST.get('key')
        value_user = request.POST.get('value')
        result += 'Cookie added!'
        response.set_cookie(str(key_user)), value_user
        response.write(result)
        return response


def showAllCookies(request):
    cookie = print_values(request.COOKIES)
    return HttpResponse(cookie)


def print_values(dict):
    result = html + "<table>"
    for key, values in dict.items():
        result += """"<tr><td>{}</td><td>{}</td>""".format(key, values)
    result += "</body></html>"
    return result


def show_number_2(request, min_number, max_number):
    num = randint(int(min_number), int(max_number))
    answer = """
             <html>
              <body>
               <p>Użytkownik podał wartośći {} i {}.<br/> Wylosowano liczbę: {}</p>
              </body>
             </html>
             """.format(min_number, max_number, num)
    return HttpResponse(answer)


answer = """<html>
                <body>
                    <p>{}</p>
                </body>
            </html>"""


def show_number3(request, min_number=None, max_number=None):
    num = randint(int(min_number), int(max_number))
    if min_number is None and max_number is None:
        value = "Wylosowano liczbę: {}".format(randint(0, 100))
    elif min_number is None:
        min_number = 0
        value = "Użytkownik podał wartość {}. <br/> Wylosowano liczbę: {}".format(max_number, num)
    else:
        value = "Użytkownik podał wartośći {} i {}.<br/> Wylosowano liczbę: {}".format(min_number, max_number, num)
    return HttpResponse(answer.formato(value))


def wrap_foo(funkcja):
    def html_temp(*args, **kwargs):
        answer = """
        <html>
            <head>
                <p>Owiniete Decoratorem</p>
            </head>
            <body>
                {}
            </body>
        </html""".format(funkcja(*args, **kwargs))
        return HttpResponse(answer)
    return html_temp


@csrf_exempt
@wrap_foo
def hello_name(request, name):
    hello = """<p>Witaj {}!</p>""".format(name)
    return hello
