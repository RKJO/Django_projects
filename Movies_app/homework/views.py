from django.shortcuts import render
from homework.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import redirect


def decor_warp_html(foo):
    def warp_html(*args, **kwargs):
        result = """<html>
            <head>
            </head>
            <body>
            <table>
            {}
            </table>
            </body>
            </html>""".format(foo(*args, **kwargs))
        return HttpResponse(result)
    return warp_html


@decor_warp_html
def movies(request):
    movies_list = Movie.objects.order_by("-year")
    result = """<tr>
                    <td width=70><b/>Title</td>
                    <td width=70><b/>Year</td>
                    <td width=70><b/>Rating</td>
                    <td width=70><b/>Director</td>
                    <td width=70><b/>Screenplay</td></tr>"""
    for movie in movies_list:
        result += """<tr>
                        <td><a href='/movie_details/{}'><b>{}</b></a></td>""".format(movie.id, movie.title)
        result += """   <td>{}</td>
                        <td>{}</td>
                        <td>{} {}</td>
                        <td>{} {}</td>
                        """.format(movie.year,
                                   movie.rating,
                                   movie.director.first_name,
                                   movie.director.last_name,
                                   movie.screenplay.first_name,
                                   movie.screenplay.last_name,)
        result += """<td><form>
                            <input type="button" value="Edit" onclick="location.href='/edit_movie/{}'"
                            </form></td></tr>""".format(movie.id)
    result += """<tr><td><form>
                            <input type="button" value="Add" onclick="location.href='/add_movie'"
                        </form></td></tr>
                """
    return result


@decor_warp_html
def movie_details(request, id):
    movies_details = Movie.objects.get(id=id)
    result = ""
    result += """<tr><td width="230">ID:<b/> {}</td></tr>
                    <tr><td>Title:<b /> {}</td></tr>
                    <tr><td>Year:<b /> {}</td></tr>
                    <tr><td>Rating:<b /> {}<td/></tr>
                    <tr><td>Director:<b /> {} {}</td></tr>
                    <tr><td>Screenplay:<b /> {} {}</td></tr>
                    """.format(movies_details.id,
                               movies_details.title,
                               movies_details.year,
                               movies_details.rating,
                               movies_details.director.first_name,
                               movies_details.director.last_name,
                               movies_details.screenplay.first_name,
                               movies_details.screenplay.last_name,)
    for movie in movies_details.genre.all():
        result += """<tr><td>Genre: {}<br></td></tr>
                """.format(movie.genre,)
    for person in movies_details.personmovie_set.all():
        result += """<tr><td>występują:<ul><li><b>{} {}</b><br></td></tr>
                    <tr><td>rola: {}</li><br></td></tr>""".format(person.person.first_name,
                                                                  person.person.last_name,
                                                                  person.role)

    return result


@csrf_exempt
@decor_warp_html
def edit_movie(request, id_value):
    movie_edit = Movie.objects.get(id=id_value)
    movie_persons = Person.objects.all()
    details = movie_details(request, id)
    result = ""
    if request.method == "GET":
        result += """<form action="#" method="POST">
                           <label>Edytuj dane:</label><br/>
                                <label>ID: </label>
                                    <input size=4 type="text" name="id" placeholder="{}">
                                <label>Title: </label>
                                    <input type="text" name="title" placeholder="{}">
                                <label>Year: </label>
                                <input type="text" name="year" placeholder="{}">
                                <label>Rating : </label>
                                <input type="text" name="rating" placeholder="{}"><br />                              
                           """.format(movie_edit.id,
                                      movie_edit.title,
                                      movie_edit.year,
                                      movie_edit.rating)

        result += """<label>&nbsp Director: </label>
                            <select name="director">"""
        for directors in movie_persons:
            display_director = directors.first_name + " " + directors.last_name
            if directors.id != movie_edit.director.id:
                result += '<option value={}>{}</option>'.format(directors.id, display_director)
            else:
                result += '<option value={} selected>{} </option>'.format(directors.id, display_director)
        result += "</select><br />"

        result += """<label>&nbsp Screenplay: </label>
                                    <select name="screenplay_name">"""
        for screenplays in movie_persons:
            display_screenplays = screenplays.first_name + " " + screenplays.last_name
            if screenplays.id != movie_edit.screenplay.id:
                result += '<option value={}>{}</option>'.format(screenplays.id, display_screenplays)
            else:
                result += '<option value={} selected>{} </option>'.format(screenplays.id, display_screenplays)
        result += "</select><br/>"

        result += """<input type="submit" name="submit" value="Zapisz">
                    <input type="button" value="Powrót" onclick="location.href='/movies'"
                    </form>"""

    if request.method == "POST":
        movie_id = request.POST.get("id")
        movie_title = request.POST.get("title")
        movie_year = request.POST.get("year")
        movie_rating = request.POST.get("rating")
        movie_director = request.POST.get("director_name")
        movie_screenplay = request.POST.get("screenplay_name")
        if movie_id != movie_edit.id and movie_id != "":
            movie_edit.id = movie_id
            movie_edit.save()
        if movie_title != movie_edit.title and movie_title != "":
            movie_edit.title = movie_title
            movie_edit.save()
        if movie_year != movie_edit.year and movie_year != "":
            movie_edit.year = movie_year
            movie_edit.save()
        if movie_rating != movie_edit.rating and movie_rating != "":
            movie_edit.rating = movie_rating
            movie_edit.save()
        if movie_director != movie_edit.director.id and movie_director is not None:
            if movie_director == "":
                pass
            else:
                movie_edit.director = Person.objects.get(pk=int(movie_director)),
                movie_edit.save()
        if movie_screenplay != movie_edit.screenplay.id and movie_screenplay is not None:
            if movie_screenplay == "":
                pass
            else:
                movie_edit.screenplay = Person.objects.get(pk=int(movie_screenplay))
                movie_edit.save()

        result += """<tr><td>Dane po edycji: </tr></td>
                        <tr>
                            <td><b>ID :</b> {}</td><br />
                            <td><b>Title :</b> {}</td><br />
                            <td><b>Year :</b> {}</td><br />
                            <td><b>Rating :</b> {}</td><br />
                            <td><b>Director :</b> {} {}</td><br />
                            <td><b>Screenplay :</b> {} {}</td><br />
                        </tr><br/>
                        <tr><td><form>
                        <input type="button" value="Powrót" onclick="location.href='/movies'"
                        </form></td></tr>
                        """.format(movie_edit.id,
                                   movie_edit.title,
                                   movie_edit.year,
                                   movie_edit.rating,
                                   movie_edit.director.first_name,
                                   movie_edit.director.last_name,
                                   movie_edit.screenplay.first_name,
                                   movie_edit.screenplay.last_name)

    return details, result


@csrf_exempt
# @decor_warp_html
def add_movie(request):
    all_persons = Person.objects.all()
    result = """<html>
            <head></head>
            <body>
            <table>"""
    if request.method == "GET":
        result += """<form action="#" method="POST">
                           <label>Wprowadź dane filmu:</label><br/>"""
        result += """<label>&nbsp Title: </label>
                        <input type="text" name="title"> """
        result += """<label>&nbsp Year: </label>
                        <input type="text" name="year">"""
        result += """<label>&nbsp Rating: </label>
                                <input size=4 type="text" name="rating">"""
        result += """<label>&nbsp Director: </label>
                        <select name="director">"""

        for each_director in all_persons:
            first_and_last_director = each_director.first_name + " " + each_director.last_name
            result += '<option value={}>{}</option>'.format(each_director.id, first_and_last_director)
        result += "</select>"
        result += """<label>&nbsp Screenplay: </label>
                                <select name="screenplay">"""

        for each_screenplay in all_persons:
            first_and_last_screenplay = each_screenplay.first_name + " " + each_screenplay.last_name
            result += '<option value={}>{}</option>'.format(each_screenplay.id, first_and_last_screenplay)
        result += "</select><br />"
        result += """<input type="submit" name="submit" value="Zapisz">
                           </form></body><html> """

        return HttpResponse(result)

    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        rating = request.POST.get("rating")
        director = request.POST.get("director")
        screenplay = request.POST.get("screenplay")

        Movie.objects.create(title=title,
                             year=year,
                             rating=rating,
                             director=Person.objects.get(pk=int(director)),
                             screenplay=Person.objects.get(pk=int(screenplay)))

    return HttpResponseRedirect("movies")


@decor_warp_html
def persons(request):
    person_val = Person.objects.all()
    result = ""
    result += """<tr>
                    <td width="30"><b />ID</td>
                    <td width="130"><b />Name</td>
                    <td></td></tr>
                    """
    for persons_list in person_val:
        result += """<tr>
                    <td>{}</td>
                    <td>{} {}</td><td>
                    <form>
                    <input type="button" value="Edit" onclick="location.href='/edit_person/{}'"
                    </form>
                    </td></tr>""".format(persons_list.id,
                                         persons_list.first_name,
                                         persons_list.last_name,
                                         persons_list.id)
    result += """<tr><td><form>
                    <input type="button" value="Add Person" onclick="location.href='/add_person'"
                </form></td></tr>
        """
    return result


@csrf_exempt
@decor_warp_html
def edit_person(request, id):
    person_edit = Person.objects.get(id=id)
    result = ""
    if request.method == "GET":
        result += """<form action="#" method="POST">
                           <label>Edytuj dane:</label><br/>
                                <input type="text" name="first_name" placeholder="{}">
                                <input type="text" name="last_name" placeholder="{}"><br/>
                                <input type="submit" name="submit" value="Zapisz">
                           </form>""".format(person_edit.first_name, person_edit.last_name)
    result += """<form>
                    <input type="button" value="Powrót" onclick="location.href='/persons'"
                    </form>
        """

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        if first_name != person_edit.first_name and first_name != "":
            person_edit.first_name = first_name
            person_edit.save()
        if last_name != person_edit.last_name and last_name != "":
            person_edit.last_name = last_name
            person_edit.save()
        result += """Nowo wprowadzone dane: <br/> {} {}
                    </br></br>
                    <form>
                    <input type="submit" value="Powrót" onclick="location.href='/persons'"
                    </form>
                    """.format(person_edit.first_name, person_edit.last_name)

    return result


@csrf_exempt
# @decor_warp_html
def add_person(request):
    result = """<html>
            <head></head>
            <body>
            <table>"""
    if request.method == "GET":
        result += """<form action="#" method="POST">
                           <label>Wprowadź dane osoby:</label><br/>
                                <input type="text" name="first_name" placeholder=" First name">
                                <input type="text" name="last_name" placeholder=" Last name"><br/>
                                <input type="submit" name="submit" value="Zapisz">
                           </form>"""
        result += """
    </body>
    <html> """
        return HttpResponse(result)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        Person.objects.create(first_name=first_name, last_name=last_name)

    return HttpResponseRedirect("persons")
