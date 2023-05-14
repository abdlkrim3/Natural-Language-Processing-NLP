import rdflib

# Créer un graphe RDF
g = rdflib.Graph()

# Définir les préfixes RDF/Schema.org
rdf_prefix = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
schema_prefix = rdflib.Namespace("http://schema.org/")

# Ajouter les triplets au graphe RDF
g.add((rdflib.URIRef("http://example.com/Product1"), rdf_prefix.type, schema_prefix.Product))
g.add((rdflib.URIRef("http://example.com/Product1"), schema_prefix.name, rdflib.Literal("Product A")))

g.add((rdflib.URIRef("http://example.com/Comment1"), rdf_prefix.type, schema_prefix.Comment))
g.add((rdflib.URIRef("http://example.com/Comment1"), schema_prefix.author, rdflib.Literal("Abderrahim")))
g.add((rdflib.URIRef("http://example.com/Comment1"), schema_prefix.text, rdflib.Literal("C'est un excellent produit !")))
g.add((rdflib.URIRef("http://example.com/Comment1"), schema_prefix.rating, rdflib.Literal("5")))
g.add((rdflib.URIRef("http://example.com/Comment1"), schema_prefix.datePublished, rdflib.Literal("2023-05-14")))
g.add((rdflib.URIRef("http://example.com/Comment1"), schema_prefix.about, rdflib.URIRef("http://example.com/Product1")))

g.add((rdflib.URIRef("http://example.com/Comment2"), rdf_prefix.type, schema_prefix.Comment))
g.add((rdflib.URIRef("http://example.com/Comment2"), schema_prefix.author, rdflib.Literal("Abdelkarim")))
g.add((rdflib.URIRef("http://example.com/Comment2"), schema_prefix.text, rdflib.Literal("Je ne suis pas satisfait du service.")))
g.add((rdflib.URIRef("http://example.com/Comment2"), schema_prefix.rating, rdflib.Literal("1")))
g.add((rdflib.URIRef("http://example.com/Comment2"), schema_prefix.datePublished, rdflib.Literal("2023-05-15")))
g.add((rdflib.URIRef("http://example.com/Comment2"), schema_prefix.about, rdflib.URIRef("http://example.com/Product1")))

g.add((rdflib.URIRef("http://example.com/Comment3"), rdf_prefix.type, schema_prefix.Comment))
g.add((rdflib.URIRef("http://example.com/Comment3"), schema_prefix.author, rdflib.Literal("Zakaria")))
g.add((rdflib.URIRef("http://example.com/Comment3"), schema_prefix.text, rdflib.Literal("Tres bon rapport qualite-prix.")))
g.add((rdflib.URIRef("http://example.com/Comment3"), schema_prefix.rating, rdflib.Literal("5")))
g.add((rdflib.URIRef("http://example.com/Comment3"), schema_prefix.datePublished, rdflib.Literal("2023-05-13")))
g.add((rdflib.URIRef("http://example.com/Comment3"), schema_prefix.about, rdflib.URIRef("http://example.com/Product1")))

g.add((rdflib.URIRef("http://example.com/Comment4"), rdf_prefix.type, schema_prefix.Comment))
g.add((rdflib.URIRef("http://example.com/Comment4"), schema_prefix.author, rdflib.Literal("Ahmed")))
g.add((rdflib.URIRef("http://example.com/Comment4"), schema_prefix.text, rdflib.Literal("J'aime bien le produit, mais il pourrait etre ameliore.")))
g.add((rdflib.URIRef("http://example.com/Comment4"), schema_prefix.rating, rdflib.Literal("2")))
g.add((rdflib.URIRef("http://example.com/Comment4"), schema_prefix.datePublished, rdflib.Literal("2023-05-16")))
g.add((rdflib.URIRef("http://example.com/Comment4"), schema_prefix.about, rdflib.URIRef("http://example.com/Product1")))

# Enregistrer le graphe RDF dans un fichier
file_path = "mon_fichier.rdf"  # Spécifiez le chemin du fichier de sortie
g.serialize(file_path, format="xml")
