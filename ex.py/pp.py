

import json

questions = [
    {
        "question": "Quelle est la meilleure méthode pour conserver un poisson frais?",
        "options": ["Réfrigération immédiate", "Séchage au soleil", "Température ambiante", "Congélation sans emballage"],
        "answer": "Réfrigération immédiate"
    },
    {
        "question": "Quel poisson est le plus riche en oméga-3?",
        "options": ["Saumon", "Thon", "Merlan", "Cabillaud"],
        "answer": "Saumon"
    },
    {
        "question": "Quel poisson est le plus recommandé pour les enfants?",
        "options": ["Saumon", "Truite", "Sardines", "Cabillaud"],
        "answer": "Saumon"
    },
    {
        "question": "Quel poisson est idéal pour les adultes et les seniors?",
        "options": ["Maquereau", "Thon", "Flétan", "Sole"],
        "answer": "Maquereau"
    },
    {
        "question": "Quel poisson est le plus adapté aux personnes diabétiques?",
        "options": ["Saumon", "Tilapia", "Sardines", "Truite"],
        "answer": "Saumon"
    },
    {
        "question": "Quelle méthode de cuisson conserve le mieux les nutriments du poisson?",
        "options": ["Grillé", "Frit", "Vapeur", "Bouilli"],
        "answer": "Vapeur"
    },
    {
        "question": "Quel poisson contient le plus de vitamine D?",
        "options": ["Saumon", "Anguille", "Hareng", "Sardines"],
        "answer": "Hareng"
    },
    {
        "question": "Quelle est la durée idéale pour congeler un poisson sans perdre sa qualité?",
        "options": ["1 mois", "3 mois", "6 mois", "12 mois"],
        "answer": "6 mois"
    },
    {
        "question": "Quel poisson est le plus conseillé pour les femmes enceintes?",
        "options": ["Saumon", "Sardines", "Maquereau", "Flétan"],
        "answer": "Sardines"
    },
    {
        "question": "Quel poisson est déconseillé en raison de sa forte concentration en mercure?",
        "options": ["Thon", "Saumon", "Truite", "Cabillaud"],
        "answer": "Thon"
    },
    {
        "question": "Quelle est la meilleure façon de conserver un poisson au réfrigérateur?",
        "options": ["Dans un récipient hermétique", "À l’air libre", "Dans du papier journal", "Immergé dans l’eau"],
        "answer": "Dans un récipient hermétique"
    },
    {
        "question": "Quel poisson est idéal pour une alimentation riche en protéines et faible en gras?",
        "options": ["Sole", "Tilapia", "Truite", "Saumon"],
        "answer": "Tilapia"
    }
]

with open("quiz_questions.json", "w", encoding="utf-8") as file:
    json.dump(questions, file, indent=4)

print("Fichier JSON créé avec succès!")
