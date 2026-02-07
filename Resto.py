import streamlit as st

# Menu du restaurant
menu = {
    "Pizza": 8.5,
    "Burger": 6.0,
    "Salade": 4.5,
    "Poulet rôti": 9.0,
    "Coca": 2.0,
    "Eau": 1.0
}

st.title("🍽️ Menu du Restaurant")

# Demander le nom du client
nom = st.text_input("Entrez votre nom :")

if nom:
    st.write(f"Bienvenue {nom} ! Voici notre menu :")
    for plat, prix in menu.items():
        st.write(f"- {plat} : {prix} $")

    commande = []
    choix = st.multiselect("Choisissez vos plats/boissons :", list(menu.keys()))

    if choix:
        for plat in choix:
            qte = st.number_input(f"Quantité de {plat} :", min_value=1, step=1)
            if qte > 0:
                commande.append((plat, qte))

        # Calcul de la facture
        facture = sum(menu[plat] * qte for plat, qte in commande)

        st.subheader("🧾 Facture")
        if len(commande) == 0:
            st.write("Aucune commande passée.")
        else:
            for plat, qte in commande:
                st.write(f"{plat} x{qte} = {menu[plat] * qte} $")
            st.write(f"**Total à payer : {facture} $**")

        # Exemple de match/case
        match len(commande):
            case 0:
                st.info("Vous n'avez rien commandé.")
            case 1:
                st.success("Merci pour votre petite commande !")
            case _:
                st.success("Merci pour votre commande généreuse !")