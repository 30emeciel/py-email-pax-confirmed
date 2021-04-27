{% extends "email_base.rst" %}
{% block title %}{% include 'confirmed_pax_title_fr.txt' %}{% endblock %}

{% block content %}
Salut {{pax.name}} 🌸

Ton compte a été validé. Tu peux maintenant te `rendre sur Coliv'app <https://coliv.30emeciel.fr>`_ puis choisir les dates de ta présence au
coworking/coliving du 30ème Ciel.

{% endblock %}
