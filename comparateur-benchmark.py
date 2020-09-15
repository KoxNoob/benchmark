import streamlit as st
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}

# Compétition football
ligue_des_nations_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Ligue-des-Nations-ed2195'

qualif_euro2021_moins21_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Qualif.-Euro-2021-(-21)-ed1039'
champions_league_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Ligue-des-Champions-ed7'
europa_league_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Ligue-Europa-ed1181'
ligue_1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/France-Ligue-1-ed3'
ligue_2_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/France-Ligue-2-ed9'
liga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Espagne-LaLiga-ed6'
bundesliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Allemagne-Bundesliga-ed4'
premier_league_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Angleterre-Premier-League-ed2'
serie_A_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Italie-Serie-A-ed5'
coupe_allemagne_url = "http://www.comparateur-de-cotes.fr/comparateur/football/Coupe-d'Allemagne-ed23"
carabao_cup_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Angleterre-EFL-Cup-ed21'


# Compétition tennis
us_open_hommes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Hommes)-ed846'
us_open_femmes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Femmes)-ed847'
us_open_dh_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Doubles-H)-ed1294'
us_opendf_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Doubles-F)-ed1295'
kitzbuhel_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Kitzb%C3%BChel-(250-Series)-ed1133'
istanbul_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Istanbul-(Intl.-Events)-ed895'
rome_atp_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Rome-(Masters)-ed819'
rome_wta_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Rome-(Prem.-Events)-ed883'

# Compétition rugby
champions_cup_url = 'http://www.comparateur-de-cotes.fr/comparateur/rugby/Champions-Cup-ed569'
top_14_url = 'http://www.comparateur-de-cotes.fr/comparateur/rugby/France-Top-14-ed341'

# Compétition basketball
nba_url = 'http://www.comparateur-de-cotes.fr/comparateur/basketball/Etats-Unis-NBA-ed353'

# Compétition handball
lidl_starligue_url = 'http://www.comparateur-de-cotes.fr/comparateur/handball/France-Division-1-ed268'
liga_asobal_url = 'http://www.comparateur-de-cotes.fr/comparateur/handball/Espagne-Liga-Asobal-ed267'

# Compétition hockey
nhl_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Etats-Unis-NHL-ed378'
khl_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/KHL-Russie-Superligue-ed395'

url_competitions = [ligue_1_url, ligue_2_url, liga_url, bundesliga_url, serie_A_url, premier_league_url,
                    ligue_des_nations_url, qualif_euro2021_moins21_url, champions_league_url, europa_league_url,
                    coupe_allemagne_url, us_open_hommes_url, us_open_femmes_url, us_open_dh_url, us_opendf_url,
                    kitzbuhel_url, istanbul_url, champions_cup_url, top_14_url, nba_url, lidl_starligue_url,
                    liga_asobal_url, nhl_url, khl_url]

name_competitions = ['Ligue 1', 'Ligue 2', 'Liga', 'Bundesliga', 'Serie A', 'Premier League', 'Ligue des Nations',
                     'Qualif Euro 2021 (-21 ans)', 'Champions League', 'Europa League', 'Coupe d\'Allemagne',
                     'US Open Hommes', 'US Open Femmes', 'US Open Double Hommes', 'US Open Double Femmes', 'Kitzbühel',
                     'Istanbul', 'Champions Cup', 'Top14', 'NBA', 'Lidl Starligue', 'Liga Asobal', 'NHL', 'KHL']

# Opérateurs
zebet = "ZEbet"
winamax = "Winamax"
vbet = "Vbet"
unibet = "Unibet"
poker_stars = "PokerStars Sports"
pmu = "PMU"
parions_sports = "ParionsWeb"
netbet = "NetBet"
bwin = "Bwin"
betclic = "Betclic"

operateurs = [winamax, unibet, betclic, parions_sports, zebet, pmu, bwin, poker_stars, vbet, netbet]


def script_1_N_2(nb_match, liste_competition):
    global trj_moyenne
    bench_final = pd.DataFrame(index=[i for i in operateurs])
    for sport in liste_competition:
        page = requests.get(sport, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        liste_trj = []
        for ope in operateurs:
            try:
                trj_totaux = []
                trj_moyenne = 0
                cote = []
                for k in range(nb_match):
                    try:
                        item = soup.find_all('tr', {'title': "Parier avec " + ope})[k].get_text()
                        item = item.strip().replace('\n', '')

                        item = item.split(' ')
                        item[:] = (i for i in item if i != '')
                        for l in range(len(item)):
                            cote.append(float(item[l]))

                        time.sleep(0.2)
                    except:
                        break

                for a in range(int(len(cote) / 3)):
                    trj_totaux.append(1 / ((1 / (float(cote[3 * a]))) + (1 / (float(cote[3 * a + 1]))) + (
                            1 / (float(cote[3 * a + 2])))) * 100)

                trj_moyenne = round((sum(trj_totaux) / len(trj_totaux)), 2)
                trj_moyenne = "{:.2f}".format(trj_moyenne)

            except:
                pass
            liste_trj.append(trj_moyenne)
        bench_tempo = pd.DataFrame(data=liste_trj, index=[i for i in operateurs])
        bench_final = bench_final.merge(bench_tempo, left_index=True, right_index=True)

    return bench_final

def script_1_2(nb_match, liste_competition) :
    global trj_moyenne
    bench_final = pd.DataFrame(index=[i for i in operateurs])
    for sport in liste_competition:
        page = requests.get(sport, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        liste_trj = []
        for ope in operateurs:
            try:
                trj_totaux = []
                trj_moyenne = 0
                cote = []
                for k in range(nb_match):
                    try:
                        item = soup.find_all('tr', {'title': "Parier avec " + ope})[k].get_text()
                        item = item.strip().replace('\n', '')

                        item = item.split(' ')
                        item[:] = (i for i in item if i != '')
                        for l in range(len(item)):
                            cote.append(float(item[l]))

                        time.sleep(0.2)
                    except:
                        break


                for a in range(int(len(cote) / 2)):
                    trj_totaux.append(1 / ((1 / (float(cote[2 * a]))) + (1 / (float(cote[2 * a + 1])))) * 100)

                trj_moyenne = round((sum(trj_totaux) / len(trj_totaux)), 2)
                trj_moyenne = "{:.2f}".format(trj_moyenne)

            except:
                pass
            liste_trj.append(trj_moyenne)
        bench_tempo = pd.DataFrame(data=liste_trj, index=[i for i in operateurs])
        bench_final = bench_final.merge(bench_tempo, left_index=True, right_index=True)

    return bench_final

@st.cache
def choix_final(initial, final):
    for choix in initial:
        if choix == True:
            final.append(choix)
    return final


@st.cache
def choix_final_url(initial, final, url):
    for choix in initial:
        if choix == True:
            url.append(choix)
    return final


sport = st.sidebar.radio('Sports', ('Football', 'Tennis', 'Rugby', 'Handball', 'Hockey', 'Entrée manuelle (1 compétition)', 'Entrée manuelle (+ d\'1 compétition)'))

if sport == 'Football':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Football</h3>",
        unsafe_allow_html=True)

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 30, 2)
    lancement = st.button('Lancez le benchmark')
    competition_foot_initial = [ligue_1_url, ligue_2_url, liga_url, serie_A_url, bundesliga_url, premier_league_url,
                                champions_league_url, europa_league_url, carabao_cup_url,
                                coupe_allemagne_url]

    if lancement:
        bench_final = script_1_N_2(nb_rencontres,competition_foot_initial)
        bench_final.columns = ['Ligue 1', 'Ligue 2', 'Liga', 'Bundesliga', 'Serie A', 'Premier League',
                               'Carabao Cup', 'Champions League', 'Europa League', 'Coupe d\'Allemagne']
        st.table(bench_final)


if sport == 'Tennis':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Tennis</h3>",
        unsafe_allow_html=True)

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    lancement = st.button('Lancez le benchmark')
    competition_tennis_initial = [rome_atp_url, rome_wta_url]

    if lancement:
        bench_final = script_1_2(nb_rencontres, competition_tennis_initial)
        bench_final.columns = ['Rome ATP', 'Rome WTA']
        st.table(bench_final)


if sport == 'Rugby':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Rugby</h3>",
        unsafe_allow_html=True)

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    lancement = st.button('Lancez le benchmark')
    competition_tennis_initial = [top_14_url, champions_cup_url]

    if lancement:
        bench_final = script_1_N_2(nb_rencontres, competition_tennis_initial)
        bench_final.columns = ['Top14', 'Champions Cup']
        st.table(bench_final)



if sport == 'Handball':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Handball</h3>",
        unsafe_allow_html=True)

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    lancement = st.button('Lancez le benchmark')
    competition_tennis_initial = [lidl_starligue_url, liga_asobal_url]

    if lancement:
        bench_final = script_1_N_2(nb_rencontres, competition_tennis_initial)
        bench_final.columns = ['Lidl Starligue', 'Liga Asobal']
        st.table(bench_final)


if sport == 'Hockey':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Hockey</h3>",
        unsafe_allow_html=True)

    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    lancement = st.button('Lancez le benchmark')
    competition_tennis_initial = [nhl_url, khl_url]

    if lancement:
        bench_final = script_1_N_2(nb_rencontres, competition_tennis_initial)
        bench_final.columns = ['NHL', 'KHL']
        st.table(bench_final)

if sport == "Entrée manuelle (1 compétition)":
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark 1 Compétition Manuelle</h3>",
        unsafe_allow_html=True)

    st.write(
        "Afin d'effectuer du benchmark sur une compétition qui ne serait pas encore renseignée, vous pouvez \
        utiliser cette section.")
    st.write("Le benchmark se fait à partir du site http://www.comparateur-de-cotes.fr/")
    st.write("Dans le premier champ, renseignez l'url de la compétition du site comparateur-de-cote. Donnez un nom à \
    cette compétition. Ensuite sélectionnez le nombre de matchs sur lequel vous voulez faire la moyenne des TRJ. Enfin \
    renseignez le nombre d'issues possibles et cliquez sur \"Lancer le benchmark\"")


    entree_manuelle = []
    url = st.text_input('Collez l\'url ici')
    entree_manuelle.append(url)
    nom_competition = st.text_input("Comment s'appelle la compétition ?")
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
    lancement = st.button('Lancez le benchmark')

    if lancement:

        if choix_issue == '1-2':
            bench_final = script_1_2(nb_rencontres, entree_manuelle)

        else:
            bench_final = script_1_N_2(nb_rencontres, entree_manuelle)

        bench_final.columns = [nom_competition]
        st.table(bench_final)


if sport == 'Entrée manuelle (+ d\'1 compétition)' :

    nb_competition = st.selectbox('Combien de compétitions à bencher ?', ('2', '3', '4', '5', '6'))

    if nb_competition == '2' :
        entree_manuelle = []
        url_1 = st.text_input('URL n°1')
        entree_manuelle.append(url_1)
        nom_competition_1 = st.text_input("Nom Compétition 1")
        url_2 = st.text_input('URL N°2')
        entree_manuelle.append(url_2)
        nom_competition_2 = st.text_input("Nom Compétition 2")
        nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle)
            bench_final.columns = [nom_competition_1, nom_competition_2]
            bench_final['moyenne'] = 1

            for i in range(10):
                diviseur = 2
                for j in range(2):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1
                bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i,1]))/diviseur)

            st.table(bench_final)


    if nb_competition == '3' :
        entree_manuelle = []
        url_1 = st.text_input('URL n°1')
        entree_manuelle.append(url_1)
        nom_competition_1 = st.text_input("Nom Compétition 1")
        url_2 = st.text_input('URL N°2')
        entree_manuelle.append(url_2)
        nom_competition_2 = st.text_input("Nom Compétition 2")
        url_3 = st.text_input('URL n°3')
        entree_manuelle.append(url_3)
        nom_competition_3 = st.text_input("Nom Compétition 3")
        nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3]
            bench_final['moyenne'] = 1

            for i in range(10):
                diviseur = 3
                for j in range(3):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1
                bench_final.iloc[i, -1] = "{:.2f}".format(
                    (float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1]) + float(bench_final.iloc[i,2])) / diviseur)

            st.table(bench_final)



    if nb_competition == '4' :
        entree_manuelle = []
        url_1 = st.text_input('URL n°1')
        entree_manuelle.append(url_1)
        nom_competition_1 = st.text_input("Nom Compétition 1")
        url_2 = st.text_input('URL N°2')
        entree_manuelle.append(url_2)
        nom_competition_2 = st.text_input("Nom Compétition 2")
        url_3 = st.text_input('URL n°3')
        entree_manuelle.append(url_3)
        nom_competition_3 = st.text_input("Nom Compétition 3")
        url_4 = st.text_input('URL n°4')
        entree_manuelle.append(url_4)
        nom_competition_4 = st.text_input("Nom Compétition 4")
        nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3,nom_competition_4]
            bench_final['moyenne'] = 1

            for i in range(10):
                diviseur = 4
                for j in range(4):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                bench_final.iloc[i, -1] = "{:.2f}".format(
                    (float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1]) + float(bench_final.iloc[i,2]) +
                     float(bench_final.iloc[i,3])) / diviseur)
            st.table(bench_final)

    if nb_competition == '5':
        entree_manuelle = []
        url_1 = st.text_input('URL n°1')
        entree_manuelle.append(url_1)
        nom_competition_1 = st.text_input("Nom Compétition 1")
        url_2 = st.text_input('URL N°2')
        entree_manuelle.append(url_2)
        nom_competition_2 = st.text_input("Nom Compétition 2")
        url_3 = st.text_input('URL n°3')
        entree_manuelle.append(url_3)
        nom_competition_3 = st.text_input("Nom Compétition 3")
        url_4 = st.text_input('URL n°4')
        entree_manuelle.append(url_4)
        nom_competition_4 = st.text_input("Nom Compétition 4")
        url_5 = st.text_input('URL n°5')
        entree_manuelle.append(url_5)
        nom_competition_5 = st.text_input("Nom Compétition 5")
        nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3, nom_competition_4, nom_competition_5]
            bench_final['moyenne'] = 1

            for i in range(10):
                diviseur = 5
                for j in range(5):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1])
                                                    + float(bench_final.iloc[i,2]) + float(bench_final.iloc[i,3]) +
                                                           float(bench_final.iloc[i,4])) / diviseur)
            st.table(bench_final)

    if nb_competition == '6':
        entree_manuelle = []
        url_1 = st.text_input('URL n°1')
        entree_manuelle.append(url_1)
        nom_competition_1 = st.text_input("Nom Compétition 1")
        url_2 = st.text_input('URL N°2')
        entree_manuelle.append(url_2)
        nom_competition_2 = st.text_input("Nom Compétition 2")
        url_3 = st.text_input('URL n°3')
        entree_manuelle.append(url_3)
        nom_competition_3 = st.text_input("Nom Compétition 3")
        url_4 = st.text_input('URL n°4')
        entree_manuelle.append(url_4)
        nom_competition_4 = st.text_input("Nom Compétition 4")
        url_5 = st.text_input('URL n°5')
        entree_manuelle.append(url_5)
        nom_competition_5 = st.text_input("Nom Compétition 5")
        url_6 = st.text_input('URL n°6')
        entree_manuelle.append(url_6)
        nom_competition_6 = st.text_input("Nom Compétition 6")
        nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3, nom_competition_4,
                                   nom_competition_5, nom_competition_6]

            bench_final['moyenne'] = 1

            for i in range(10):
                diviseur = 6
                for j in range(6):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1])
                                                     + float(bench_final.iloc[i, 2]) + float(bench_final.iloc[i, 3]) +
                                                     float(bench_final.iloc[i, 4]) + float(bench_final.iloc[i,5])) / diviseur)

            st.table(bench_final)