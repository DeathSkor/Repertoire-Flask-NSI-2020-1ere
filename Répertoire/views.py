from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def HtmlMenuRepertoire():
    return render_template('HtmlMenuRepertoire.html')
@app.route('/add')
def AjouterNum():
    return render_template("AjouterNum.html")
@app.route('/search')
def RechercherNum():
    return render_template("RechercherNum.html")
@app.route("/save", methods=["POST"])
def ResultatAjouter():
    result=request.form
    n=result['nom']
    num=result['numero']
    if n=='':
        r="Erreur: Le contact n'a pu été enregistrer (pas de nom)"
        return render_template("ResultatAjouter.html", resultat=r)
    test=str.isdigit(num)
    if test==False:
        r="Erreur: Le contact n'a pas pu être enregistrer(Numéro invalide)"
    else:
        with open ('fichier.txt','a') as f:
            f.write(n+"\n"+num+"\n")
        r="Le contact a bien été enregistré"
    return render_template("ResultatAjouter.html", resultat=r)
@app.route("/find", methods=["POST"])
def ResultatRechercher():
    result=request.form
    N=result['name']
    noms=[]
    with open("fichier.txt","r") as f:
        for ligne in f:
            ligne=ligne.replace("\n","")
            noms.append(ligne)
    a='introuvable'
    for i in noms:
        if i==N:
            a=noms.index(N)
            a=noms[a+1]
    return render_template("ResultatRechercher.html",num=a)
app.run(debug=True)

                        
