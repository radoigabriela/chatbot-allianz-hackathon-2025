from flask import Flask, render_template, request

app = Flask(__name__)

# Definim un dicționar cu întrebări și răspunsuri
qa_pairs = {
    "Ce avantaj ofera clauza de decontare directa in asigurarile auto?" : "In cazul unui accident auto provocat de altcineva, Allianz-Tiriac iti repara masina rapid si eficient.", 

    "Protectia pretului de achizitie din asigurarea auto se aplica doar masinilor noi?" : "Da, doar vehiculelor noi, asigurate din primul an la Allianz-Tiriac, valabila in al doilea an de asigurare.", 

    "Ofera garantiile conditionate protectie suficienta pentru ambele parti intr-un contract?" : "Da, Allianz-Tiriac garanteaza plata catre Beneficiar in cazul nerespectarii contractului de catre Executant.", 

    "Cum se emite o asigurare de garantie contractuala pentru firme?" : "Se bazeaza pe contractul de lucrari/prestari servicii si garanteaza avansul, buna executie sau remedierea defectelor. Allianz-Tiriac emite garantii internationale (Surety Bonds).", 

    "Ce informatii sunt necesare pentru a obtine o oferta de asigurare de garantie?" : "Evaluam situatia financiara, experienta si capacitatile firmei. Pentru prima solicitare, completarea unui chestionar este necesara.", 

    "Se poate anula sau modifica o asigurare de garantie contractuala?" : "Da, dar doar cu acordul Beneficiarului. Modificarile de suma sau valabilitate necesita si ele acord scris.", 

    "Cand trebuie sa anunti Allianz-Tiriac despre o dauna auto?" : "Furt: in 24h. Alte riscuri: in 3 zile lucratoare. Accidente cu vatamari corporale: in 15 zile.", 

    "Ce faci daca, in urma unei daune auto, masina nu poate fi deplasata?" : "Apelezi Asistenta Rutiera Allianz-Tiriac. Daca ai Casco cu aceasta optiune, beneficiezi de tractare, transport pasageri, cazare sau masina de inlocuire.", 

    "Ce trebuie sa stii despre utilizarea formularului de constatare amiabila in cazul unui accident auto?" : "Poti folosi formularul de constatare amiabila daca nu sunt victime, sunt doar doua vehicule implicate si ambele au RCA valabil.", 

    "Unde iti poti repara masina dupa o dauna acoperita de asigurare?" : "In service-uri partenere Allianz-Tiriac, orice alt service sau in regie proprie, costurile fiind decontate conform politiei.", 

    "Ce documente sunt necesare pentru solutionarea unei daune auto?" : "Pentru Casco si RCA, sunt necesare certificatul de inmatriculare, permisul de conducere, cartea de identitate, actele de constatare (amiabila/politie), copia RCA-ului vinovatului si, daca e cazul, documente de transport.", 

    "Cum poate un service auto sa colaboreze cu Allianz-Tiriac pentru solutionarea daunelor?" : "Trimite un e-mail la partener@allianztiriac.ro cu autorizația RAR si certificatul de inregistrare.", 

    "Cand trebuie sa anunti Allianz-Tiriac despre o dauna la locuinta?" : "Furt – in 24h. Alte daune – in 5 zile de la constatare.", 

    "Ce trebuie sa faci in cazul unei daune la locuinta?" : "Limitezi pagubele, pastrezi bunurile afectate si anunti autoritatile. Pentru furt/vandalism – chemi Politia (112). Pentru incendiu – opresti gazul/curentul si chemi Pompierii. Pentru calamitată – anunti ISU sau Primaria.", 

    "Ce documente sunt necesare pentru solutionarea unei daune la locuinta?" : "Carte de identitate, polita, act de proprietate, imputernicire (daca e cazul), schita locuinta, acte autoritati, devize sau facturi pentru reparatii.", 

    "Ce evenimente pot fi notificate pe o asigurare de viata?" : "Accident, boala, deces, retragerea totala/partiala a valorii politiei, maturitatea contractului.", 

    "Cum notifici Allianz-Tiriac despre un eveniment acoperit de asigurarea de viata?" : "Online prin aplicatia Allianz-Tiriac sau pe site-ul oficial.", 

    "Ce documente sunt necesare pentru notificarea unei daune pe asigurarea de viata prin posta?" : "Formular de plata, chestionar tip 1 sau 2, documente medicale, CI, extras de cont. In unele cazuri, Allianz-Tiriac poate cere documente originale.", 

    "Cum accesezi un eveniment medical in reteaua de clinici partenere Allianz-Tiriac?" : "Te prezinti la clinica cu CI (sau certificatul de nastere pentru copii), semnezi raportul medical, iar Allianz-Tiriac achita direct serviciile.",

    "Cum beneficiezi de decontare pentru un serviciu medical efectuat in afara retelei partenere Allianz-Tiriac?" : "Platesti serviciile si ceri decontarea de la Allianz-Tiriac, prezentand documentele medicale necesare."
}

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        
        # Căutăm întrebarea în dicționar
        answer = qa_pairs.get(question, "Nu am înțeles întrebarea. Încearcă să întrebi din nou.")
    
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)