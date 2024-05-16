import requests
from flask import render_template, jsonify, request, flash, redirect, url_for
from charity.data import projets
from charity import web_charity_bp
from charity.models.don import Don
from extensions import db


@web_charity_bp.route("/")
def index():
    return render_template('index.html', projets=projets)


@web_charity_bp.route("/details/<int:projetId>")
def details(projetId):
    details = next((projet for projet in projets
                    if projet["id"] == projetId), None)
    return render_template('details.html', retour=details)


@web_charity_bp.route("/don", methods=['POST'])
def don():
    try:
        identifiant = request.form['identifiant']
        montant = request.form['montant']
        telephone = request.form['telephone']
        modePayement = request.form['modePayement']
        projet_id = request.form['projet_id']

        don = Don(identifiant=identifiant,
                  montant=montant,
                  telephone=telephone,
                  modePayement=modePayement,
                  projet_id=projet_id)

        paygate_url = "https://paygateglobal.com/api/v1/pay"
        response = requests.post(paygate_url,
                                 json={
                                     'auth_token': '8e3d1095-e7dc-4cc9-ae23-2fd3409a4afe',
                                     'phone_number': telephone,
                                     'amount': montant,
                                     'identifiant': identifiant,
                                     'network': modePayement
                                 })
        response_data = response.json()
        print('reponse', response_data)

        db.session.add(don)
        db.session.commit()
        flash('Merci pour votre don.', 'succes')
        return redirect(url_for('charity_web.details'))
    except Exception as e:
        print(e)
        flash('Votre don a "échoué.', 'error')
        return redirect(url_for('charity_web.details'))