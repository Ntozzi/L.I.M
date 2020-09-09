from django.shortcuts import render
from django.http import HttpResponse
import random


def keygens(request):
    return render(request, 'keygen/keygens.html')


def response(request):
    theresponse=""
    characters = ""

    if request.GET.get("Catégories d'expression"):
        characters = ["Rimée", "Chantée", "Comédie musicale", "Jukebox]",
                        "Texte Imposé","Sans parole","Silencieuse","doublage américain",
                      "Gromolo","Grommelot"]
        theresponse = random.choice(characters)
    if request.GET.get('Catégories de contraintes'):
        characters = ["Mimée", "Muette puis mimée", "Croisement",
                      "Suicide","Mort en scène","carnage",
                      "Déplacements limités","Assis, debout, accroupis, couché","Générateur de mots",
                      "Porno censuré","Sans limite d'espace","Dans le noir",
                      "Abécédaire""Switch","Zone d'humeurs",
                      "Grosse colère","Humeur imposée"]
        theresponse = random.choice(characters)
    if request.GET.get('Catégories de structure'):
        characters = ["Poursuite", "Double-poursuite", "Roman-photo",
                      "Fusillade","Peau de chagrin","exercice de style",
                      "Zapping télé","Etages","Téléphone arabe mimé",
                      "Harold","Carré hollandais","Traveling",
                      "Points de vue","Taxi","Trois-Têtes",
                      "Zapping","Avec exagération"]
        theresponse = random.choice(characters)
    if request.GET.get('À la manière de...'):
        characters = ["La Commedia Dell'Arte", "Matrix", "Tragédie grecque",
                        "Comédie musicale", "Western", "Romance",
                        "Zapping télé", "Telenovela", "Porno censuré",
                        "Harry Potter", "Shakespeare", "Conte",
                        "Film d'horreur", "Film muet", "Reality TV",
                        "Science-fiction", "Documentaire animalier",]
        theresponse = random.choice(characters)


    return render(request, 'keygen/response.html', {'response': theresponse})

# Create your views here.