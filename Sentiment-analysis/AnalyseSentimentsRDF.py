import rdflib
from rdflib.parser import Parser
from transformers import pipeline

# Charger le modèle d'analyse des sentiments en français
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# Chemin vers le fichier RDF
rdf_file_path = "mon_fichier.rdf"

# Charger le fichier RDF
graph = rdflib.Graph()
graph.parse(rdf_file_path, format="xml", parser=Parser(), encoding='utf-8')

# Définir les namespaces
ns1 = rdflib.Namespace("http://schema.org/")

# Requête SPARQL pour extraire les commentaires
query = """
    PREFIX ns1: <http://schema.org/>
    SELECT ?comment ?text
    WHERE {
        ?comment a ns1:Comment ;
                 ns1:text ?text .
    }
"""

# Exécuter la requête SPARQL
results = graph.query(query)

# Analyser les sentiments des commentaires
for row in results:
    commentaire = str(row.comment)
    texte = str(row.text)

    # Analyser le sentiment du commentaire
    resultats = sentiment_analyzer(texte)

    # Extraire le sentiment prédit
    sentiment_label = resultats[0]['label']

    # Mappez les étiquettes de sentiment sur positif, négatif ou neutre
    sentiment_mapping = {
        '1 star': 'negatif',
        '2 stars': 'negatif',
        '3 stars': 'neutre',
        '4 stars': 'positif',
        '5 stars': 'positif'
    }

    # Convertir l'étiquette de sentiment au format souhaité
    sentiment = sentiment_mapping.get(sentiment_label)

    # Afficher le résultat
    print("Commentaire :", commentaire)
    print("Texte :", texte)
    print("Sentiment detecte :", sentiment)
    print("--------------------------------------")
