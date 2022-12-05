import streamlit as st
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

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
jupiler_league = 'http://www.comparateur-de-cotes.fr/comparateur/football/Belgique-Jupiler-League-ed11'
super_league_suisse = 'http://www.comparateur-de-cotes.fr/comparateur/football/Suisse-Super-League-ed12'
liga_nos = 'http://www.comparateur-de-cotes.fr/comparateur/football/Portugal-Liga-NOS-ed15'
bundesliga_2_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Allemagne-Bundesliga-2-ed44'
championship_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Angleterre-Championship-ed13'
mls_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Etats-Unis-MLS-ed60'
premier_league_russie_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Russie-Premier-Ligue-ed51'
premier_league_ukraine_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Ukraine-Premier-League-ed61'
eredivisie_pb_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Pays-Bas-Eredivisie-ed10'
super_lig_turquie_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Turquie-Super-Lig-ed50'
bundesliga_autriche_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Autriche-Bundesliga-ed17'
superligue_danemark_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Danemark-Superligue-ed26'
ecosse_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Ecosse-Premier-League-ed120'
bresil_campeonato_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Br%C3%A9sil-Campeonato-ed116'
mexique_primera_A_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Mexico-Primera-A-ed109'
chili_primera_division_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Chili-Primera-Division-ed174'
equateur_serie_A_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Equateur-Serie-A-ed148'
copa_libertadores_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Copa-Libertadores-ed737'
maroc_botola_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Maroc-Botola-Pro-ed558'
allemagne_supercoupe_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Allemagne-SuperCoupe-ed1234'
bielorussie_division1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Bi%C3%A9lorussie-Div.-1-ed227'
bosnie_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Bosnie-Premier-Liga-ed324'
bulgarie_parvaliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Bulgarie-Parva-Liga-ed55'
chypre_division1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Chypre-Division-1-ed65'
croatie_division1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Croatie-Division-1-ed62'
espagne_Liga2_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Espagne-LaLiga-2-ed47'
estonie_premiumliiga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Estonie-Premium-Liiga-ed199'
finlande_veikkausliiga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Finlande-Veikkausliiga-ed29'
grece_superleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Gr%C3%A8ce-Superleague-ed19'
hongrie_nb1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Hongrie-NB-1-ed141'
ilesferoe_division1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Iles-Feroe-Division-1-ed1485'
irlande_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Irlande-Premier-League-ed112'
islande_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Islande-Premier-League-ed1123'
israel_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Israel-Premier-League-ed75'
italie_serieb_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Italie-Serie-B-ed14'
lettonie_virsliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Lettonie-Virsliga-ed253'
malte_premierdivision_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Malte-Premier-Division-ed281'
norvege_eliteserien_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Norv%C3%A8ge-Eliteserien-ed56'
paysdegalles_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/P.-de-Galles--Premier-League-ed137'
pologne_ekstraklasa_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Pologne-Ekstraklasa-ed30'
portugal_liga2_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Portugal-Liga-2-ed53'
republiquetcheque_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Rep.-Tch%C3%A8que-1-Liga-ed45'
roumanie_liga1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Roumanie-Liga-1-ed54'
serbie_superliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Serbie-Superliga-ed220'
slovaque_liga1_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Slovaquie-Liga-1-ed36'
slovenie_premierleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Slov%C3%A9nie-Division-1-ed35'
suede_allsvenskan_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Su%C3%A8de-Allsvenskan-ed28'
japon_jleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Japon-J-League-ed34'
paraguay_primeradivision_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Paraguay-Primera-Division-ed250'
coree_kleague_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Cor%C3%A9e-du-Sud-K-League-ed152'
coupe_de_france_url = 'http://www.comparateur-de-cotes.fr/comparateur/football/Coupe-de-France-ed317'
CAN_url = "http://www.comparateur-de-cotes.fr/comparateur/football/Coupe-d" + "'" +"Afrique-des-Nations-ed983"
fa_cup_url = "http://www.comparateur-de-cotes.fr/comparateur/football/Angleterre-FA-Cup-ed22"


competition_foot_url = [CAN_url, ligue_1_url, ligue_2_url, liga_url, serie_A_url, bundesliga_url, premier_league_url,
                            champions_league_url, europa_league_url, coupe_de_france_url, fa_cup_url, coupe_allemagne_url, carabao_cup_url, jupiler_league,
                        super_league_suisse, liga_nos, bundesliga_2_url, championship_url, mls_url, premier_league_russie_url,
                        premier_league_ukraine_url, eredivisie_pb_url, super_lig_turquie_url, bundesliga_autriche_url,
                        superligue_danemark_url, ecosse_premierleague_url, bresil_campeonato_url, mexique_primera_A_url,
                        chili_primera_division_url, equateur_serie_A_url, copa_libertadores_url, maroc_botola_url,
                        allemagne_supercoupe_url, bielorussie_division1_url, bosnie_premierleague_url, bulgarie_parvaliga_url,
                        chypre_division1_url, croatie_division1_url, espagne_Liga2_url, estonie_premiumliiga_url,
                        finlande_veikkausliiga_url, grece_superleague_url, hongrie_nb1_url, ilesferoe_division1_url,
                        irlande_premierleague_url, islande_premierleague_url, israel_premierleague_url, italie_serieb_url,
                        lettonie_virsliga_url, malte_premierdivision_url, norvege_eliteserien_url, paysdegalles_premierleague_url,
                        pologne_ekstraklasa_url, portugal_liga2_url, republiquetcheque_premierleague_url, roumanie_liga1_url,
                        serbie_superliga_url, slovaque_liga1_url, slovenie_premierleague_url, suede_allsvenskan_url,
                        japon_jleague_url, paraguay_primeradivision_url,coree_kleague_url]

name_foot = ['CAN','Ligue 1', 'Ligue 2', 'Liga', 'Serie_A', 'Bundesliga', 'Premier League', 'Champions League', 'Europa League',
             'Coupe de France','FA Cup','Carabao Cup', 'Coupe d\'Allemagne', 'Jupiler League', 'Super League Suisse','Liga Nos', 'Bundesliga 2',
             'Championship', 'MLS', 'Premier League Russie', 'Premier League Ukraine', 'Eredivisie Pays-Bas', 'Super Lig \
             Turquie', 'Bundesliga Autriche', 'Superligue Danemark', 'Ecosse Premierleague', 'Bresil Campeonato',
             'Mexique Primera A', 'Chili Primera Division', 'Equateur Serie A', 'Copa Libertadores', 'Maroc Botola',
             'SuperCoupe Allemagne', "Biélorussie Division 1", "Bosnie Premier League", 'Bulgarie Parvaliga', 'Chypre \
             Division 1', 'Croatie Division 1', 'Liga 2 Espagne', 'Estonie Premium Liga', 'Finlande Liga', 'Grece SuperLeague',
             'Hongrie L1', 'Iles Feroes Division 1', 'Irlande PremierLeague', 'Islande Premier League', 'Israel Premier League',
             'Italie Serie B', 'Lettonie Virsliga', 'Malte Premier Division', 'Norvège Elite', 'Pays de Galles Premier League',
             'Pologne Division 1', 'Portugal Liga 2', 'République Tchèque Premier League', 'Roumanie Liga 1', 'Serbie SuperLiga',
             'Slovaquie Liga 1', 'Slovénie Premier League', 'Suède Liga', 'Japon JLeague', 'Paraguay Primera Division',
             'Corée K-League']

# Compétition tennis
us_open_hommes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Hommes)-ed846'
us_open_femmes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Femmes)-ed847'
us_open_dh_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Doubles-H)-ed1294'
us_opendf_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/US-Open-(Doubles-F)-ed1295'
kitzbuhel_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Kitzb%C3%BChel-(250-Series)-ed1133'
istanbul_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Istanbul-(Intl.-Events)-ed895'
rome_atp_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Rome-(Masters)-ed819'
rome_wta_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Rome-(Prem.-Events)-ed883'
hambourg_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Hambourg-(500-Series)-ed837'
strasbourg_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Strasbourg-(Intl.-Events)-ed885'
roland_garros_hommes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Roland-Garros-(Hommes)-ed825'
roland_garros_femmes_url = 'http://www.comparateur-de-cotes.fr/comparateur/tennis/Roland-Garros-(Femmes)-ed832'
open_australie_hommes_url = "http://www.comparateur-de-cotes.fr/comparateur/tennis/Open-d'Australie-(Hommes)-ed711"
open_australie_femmes_url = "http://www.comparateur-de-cotes.fr/comparateur/tennis/Open-d'Australie-(Femmes)-ed710"
atp_cordoba_url = "http://www.comparateur-de-cotes.fr/comparateur/tennis/Cordoba-(250-Series)-ed2204"
atp_pune_url = "http://www.comparateur-de-cotes.fr/comparateur/tennis/Pune-(250-Series)-ed2194"
atp_montpellier_url = "http://www.comparateur-de-cotes.fr/comparateur/tennis/Montpellier-(250-Series)-ed1735"



competition_tennis_url = [us_opendf_url, us_open_dh_url, us_open_femmes_url, us_open_hommes_url, kitzbuhel_url,
                          istanbul_url, rome_atp_url, rome_wta_url, hambourg_url, strasbourg_url, roland_garros_hommes_url,
                          roland_garros_femmes_url, open_australie_hommes_url, open_australie_femmes_url, atp_cordoba_url,
                          atp_pune_url, atp_montpellier_url]

name_tennis = ['US Open DF', 'US Open DH', 'US Open Femmes', 'US Open Hommes', 'Kitzbuhel', 'Istanbul', 'Rome ATP',
               'Rome WTA', 'Hambourg', 'Strasbourg', 'Roland Garros Hommes', 'Roland Garros Femmes', "Open d'Australie H",
               "Open d'Australie F", "ATP Cordoba", "ATP Pune", "ATP Montpellier"]

# Compétition rugby
champions_cup_url = 'http://www.comparateur-de-cotes.fr/comparateur/rugby/Champions-Cup-ed569'
top_14_url = 'http://www.comparateur-de-cotes.fr/comparateur/rugby/France-Top-14-ed341'
pro_d2_url = 'http://www.comparateur-de-cotes.fr/comparateur/rugby/France-Pro-D2-ed537'

competition_rugby_url = [champions_cup_url, top_14_url, pro_d2_url]

name_rugby = ['Champions Cup', 'Top 14', 'Pro D2']

# Compétition basketball
nba_url = 'http://www.comparateur-de-cotes.fr/comparateur/basketball/Etats-Unis-NBA-ed353'

# Compétition handball
lidl_starligue_url = 'http://www.comparateur-de-cotes.fr/comparateur/handball/France-Division-1-ed268'
liga_asobal_url = 'http://www.comparateur-de-cotes.fr/comparateur/handball/Espagne-Liga-Asobal-ed267'
europe_ldcf_url = 'http://www.comparateur-de-cotes.fr/comparateur/handball/Ligue-des-Champions-(F)-ed265'

competition_handball_url = [lidl_starligue_url, liga_asobal_url, europe_ldcf_url]

name_hand = ['Lidl Starligue', 'Liga Asobal', 'Ligue des champions féminine']


# Compétition hockey
nhl_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Etats-Unis-NHL-ed378'
khl_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/KHL-Russie-Superligue-ed395'
rep_tcheque_extraliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Rep.-Tch%C3%A8que-Extraliga-ed380'
belarus_OL_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Belarus-OL-ed512'
suede_elitserien_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Su%C3%A8de-Elitserien-ed392'
slovaquie_extraliga_url = 'http://www.comparateur-de-cotes.fr/comparateur/hockey-sur-glace/Slovaquie-Extraliga-ed394'

competition_hockey_url = [nhl_url, khl_url, rep_tcheque_extraliga_url, belarus_OL_url, suede_elitserien_url,
                          slovaquie_extraliga_url]

name_hockey = ['NHL', 'KHL', 'Rep. Tcheque Extraliga', 'Belarus OL', 'Suede Elitserien', 'Slovaquie Extraliga']


# Opérateurs
zebet = "ZEbet"
winamax = "Winamax"
vbet = "Vbet"
unibet = "Unibet"
poker_stars = "PokerStars Sports"
pmu = "PMU"
parions_sports = "ParionsWeb"
netbet = "NetBet"
betclic = "Betclic"

operateurs = [winamax, unibet, betclic, parions_sports, zebet, pmu, poker_stars, vbet, netbet]



def script_1_N_2(nb_match, liste_competition, operateurs):
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
    bench_final = bench_final.astype(np.float64)
    bench_final = bench_final.apply(lambda x: x.replace(0.00, np.nan))

    for competition in bench_final.columns:
        bench_final.loc['Moyenne Compétition', competition] = round(((bench_final[competition]).sum()) / (
                    len(bench_final[competition]) - bench_final[competition].isnull().sum()),2)
    bench_final = bench_final.astype(np.float64)
    return bench_final

def script_1_2(nb_match, liste_competition, operateurs) :
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
    bench_final = bench_final.astype(np.float64)
    bench_final = bench_final.apply(lambda x: x.replace(0.00, np.nan))

    for competition in bench_final.columns:
        bench_final.loc['Moyenne Compétition', competition] = round(
            (bench_final[competition]).sum() / (
                        len(bench_final[competition]) - bench_final[competition].isnull().sum()), 2)
    bench_final = bench_final.astype(np.float64)

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


sport = st.sidebar.radio('Sports', ('Football', 'RTP of the day', 'Tennis', 'Rugby', 'Handball', 'Hockey', 'Entrée manuelle (1 compétition)',
                                    'Entrée manuelle (+ d\'1 compétition)'))

if sport == 'Football':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Football</h3>",
        unsafe_allow_html=True)
    tempo_url_foot = []
    tempo_name_foot = []

    tableau = pd.DataFrame(list(zip(name_foot, competition_foot_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_foot)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_foot.append(tableau.iloc[j,1])
                tempo_name_foot.append(tableau.iloc[j,0])
    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    moyenne = st.checkbox('Faire la moyenne par opérateur ?')
    lancement = st.button('Lancez le benchmark')

    if lancement and moyenne:

        bench_final = script_1_N_2(nb_rencontres, tempo_url_foot, operateur)
        bench_final.columns = tempo_name_foot
        bench_final['Moyenne Opérateur'] = 1
        for i in range(10):
            total_moyenne = 0.0
            diviseur = len(bench_final.columns) - 1
            for j in range(len(bench_final.columns) - 1):
                if bench_final.iloc[i, j] == 0:
                    diviseur -= 1
                else:
                    total_moyenne += float(bench_final.iloc[i, j])
            if diviseur == 0:
                bench_final.iloc[i, -1] = 0
            else:
                bench_final.iloc[i, -1] = "{:.2f}".format(total_moyenne / diviseur)
        bench_final = bench_final.astype(np.float64)
        st.table(bench_final.style.format("{:.2f}"))

    elif lancement:
        bench_final = script_1_N_2(nb_rencontres, tempo_url_foot, operateur)
        bench_final.columns = tempo_name_foot
        st.table(bench_final.style.format("{:.2f}"))

if sport == 'RTP of the day':

    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>RTP of the day</h3>",
        unsafe_allow_html=True)

    nb_rencontres = st.slider('How many events?', 0, 20, 2)
    tableau = pd.DataFrame(list(zip(name_foot, competition_foot_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Which competition?', name_foot)
    tempo_url_foot = []

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_foot.append(tableau.iloc[j,1])

    lancement = st.button('Launch')
    if lancement:
        for url in tempo_url_foot:

            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            bench_final = pd.DataFrame(index=[i for i in operateurs], columns=["1", "X", "2", "TRJ"])

            teams = []
            events = []
            cote = []
            trj_totaux = []
            indice = 0

            for k in range(nb_rencontres*2):
                try:
                    team = soup.find_all('a', {'class': "otn"})[k].get_text()
                    teams.append(team)

                    time.sleep(0.1)
                except:
                    break
            for a in range(int(len(teams) / 2)):
                events.append(teams[2*a] + " - " + teams[2*a+1])

            for j in range(nb_rencontres):
                for ope in operateurs:
                    try:
                        item = soup.find_all('tr', {'title': "Parier avec " +ope})[j].get_text()
                        item = item.strip().replace('\n', '')

                        item = item.split(' ')
                        item[:] = (i for i in item if i != '')
                        for l in range(len(item)):
                            cote.append(float(item[l]))

                        time.sleep(0.1)
                    except:
                        break

            for a in range(int(len(cote) / 3)):
                trj_totaux.append(round((1 / ((1 / (float(cote[3 * a]))) + (1 / (float(cote[3 * a + 1]))) + (
                        1 / (float(cote[3 * a + 2])))) * 100), 2))
            #trj_totaux = "{:.2f}".format(trj_totaux)

            for event in events:
                st.markdown(
                    "<h4 style='text-align: center; color: grey; size = 0'>" + event + "</h4>",
                    unsafe_allow_html=True)

                for i in range(len(operateurs)):
                    try:
                        for j in range(3):
                            bench_final.iloc[i,j] = cote[3*indice+j]
                        bench_final.iloc[i,3] = trj_totaux[indice]
                        indice = indice + 1
                    except:
                        break

                st.table(bench_final.style.format("{:.2f}"))


if sport == 'Tennis':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Tennis</h3>",
        unsafe_allow_html=True)

    tempo_url_tennis = []
    tempo_name_tennis = []

    tableau = pd.DataFrame(list(zip(name_tennis, competition_tennis_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_tennis)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j, 0]:
                tempo_url_tennis.append(tableau.iloc[j, 1])
                tempo_name_tennis.append(tableau.iloc[j, 0])
    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    moyenne = st.checkbox('Faire la moyenne par opérateur ?')
    lancement = st.button('Lancez le benchmark')

    if lancement and moyenne:

        bench_final = script_1_2(nb_rencontres, tempo_url_tennis, operateur)
        bench_final.columns = tempo_name_tennis
        bench_final['Moyenne Opérateur'] = 1
        for i in range(10):
            total_moyenne = 0.0
            diviseur = len(bench_final.columns) - 1
            for j in range(len(bench_final.columns) - 1):
                if bench_final.iloc[i, j] == 0:
                    diviseur -= 1
                else:
                    total_moyenne += float(bench_final.iloc[i, j])
            if diviseur == 0:
                bench_final.iloc[i, -1] = 0
            else:
                bench_final.iloc[i, -1] = "{:.2f}".format(total_moyenne / diviseur)

        st.table(bench_final.style.format("{:.2f}"))

    elif lancement:
        bench_final = script_1_2(nb_rencontres, tempo_url_tennis, operateur)
        bench_final.columns = tempo_name_tennis
        st.table(bench_final.style.format("{:.2f}"))


if sport == 'Rugby':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Rugby</h3>",
        unsafe_allow_html=True)

    tempo_url_rugby = []
    tempo_name_rugby = []

    tableau = pd.DataFrame(list(zip(name_rugby, competition_rugby_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_rugby)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_rugby.append(tableau.iloc[j,1])
                tempo_name_rugby.append(tableau.iloc[j,0])
    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    moyenne = st.checkbox('Faire la moyenne par opérateur ?')
    lancement = st.button('Lancez le benchmark')

    if lancement and moyenne:

        bench_final = script_1_N_2(nb_rencontres, tempo_url_rugby, operateur)
        bench_final.columns = tempo_name_rugby
        bench_final['Moyenne Opérateur'] = 1
        for i in range(10):
            total_moyenne = 0.0
            diviseur = len(bench_final.columns) - 1
            for j in range(len(bench_final.columns) - 1):
                if bench_final.iloc[i, j] == 0:
                    diviseur -= 1
                else:
                    total_moyenne += float(bench_final.iloc[i, j])
            if diviseur == 0:
                bench_final.iloc[i, -1] = 0
            else:
                bench_final.iloc[i, -1] = "{:.2f}".format(total_moyenne / diviseur)

        st.table(bench_final.style.format("{:.2f}"))

    elif lancement:
        bench_final = script_1_N_2(nb_rencontres, tempo_url_rugby, operateur)
        bench_final.columns = tempo_name_rugby
        st.table(bench_final.style.format("{:.2f}"))

if sport == 'Handball':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Handball</h3>",
        unsafe_allow_html=True)

    tempo_url_handball = []
    tempo_name_handball = []

    tableau = pd.DataFrame(list(zip(name_hand, competition_handball_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_hand)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_handball.append(tableau.iloc[j,1])
                tempo_name_handball.append(tableau.iloc[j,0])
    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    moyenne = st.checkbox('Faire la moyenne par opérateur ?')
    lancement = st.button('Lancez le benchmark')

    if lancement and moyenne:

        bench_final = script_1_N_2(nb_rencontres, tempo_url_handball, operateur)
        bench_final.columns = tempo_name_handball
        bench_final['Moyenne Opérateur'] = 1
        for i in range(10):
            total_moyenne = 0.0
            diviseur = len(bench_final.columns) - 1
            for j in range(len(bench_final.columns) - 1):
                if bench_final.iloc[i, j] == 0:
                    diviseur -= 1
                else:
                    total_moyenne += float(bench_final.iloc[i, j])
            if diviseur == 0:
                bench_final.iloc[i, -1] = 0
            else:
                bench_final.iloc[i, -1] = "{:.2f}".format(total_moyenne / diviseur)

        st.table(bench_final.style.format("{:.2f}"))
    elif lancement:
        bench_final = script_1_N_2(nb_rencontres, tempo_url_handball, operateur)
        bench_final.columns = tempo_name_handball
        st.table(bench_final.style.format("{:.2f}"))


if sport == 'Hockey':
    st.markdown(
        "<h3 style='text-align: center; color: grey; size = 0'>Benchmark Hockey</h3>",
        unsafe_allow_html=True)

    tempo_url_hockey = []
    tempo_name_hockey = []

    tableau = pd.DataFrame(list(zip(name_hockey, competition_hockey_url)), columns=['Selection', 'Url'])
    options = st.multiselect('Quelle compétition ?', name_hockey)

    for item in options:
        for j in range(len(tableau)):
            if item == tableau.iloc[j,0]:
                tempo_url_hockey.append(tableau.iloc[j,1])
                tempo_name_hockey.append(tableau.iloc[j,0])
    # Benchmark
    nb_rencontres = st.slider('Combien de rencontres à prendre en compte maximum ?', 0, 20, 2)
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    moyenne = st.checkbox('Faire la moyenne par opérateur ?')
    lancement = st.button('Lancez le benchmark')

    if lancement and moyenne:

        bench_final = script_1_N_2(nb_rencontres, tempo_url_hockey, operateur)
        bench_final.columns = tempo_name_hockey
        bench_final['Moyenne Opérateur'] = 1
        for i in range(10):
            total_moyenne = 0.0
            diviseur = len(bench_final.columns) - 1
            for j in range(len(bench_final.columns) - 1):
                if bench_final.iloc[i, j] == 0:
                    diviseur -= 1
                else:
                    total_moyenne += float(bench_final.iloc[i, j])
            if diviseur == 0:
                bench_final.iloc[i, -1] = 0
            else:
                bench_final.iloc[i, -1] = "{:.2f}".format(total_moyenne / diviseur)

        st.table(bench_final.style.format("{:.2f}"))

    elif lancement:
        bench_final = script_1_N_2(nb_rencontres, tempo_url_hockey, operateur)
        bench_final.columns = tempo_name_hockey
        st.table(bench_final.style.format("{:.2f}"))

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
    operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
    choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
    lancement = st.button('Lancez le benchmark')

    if lancement:

        if choix_issue == '1-2':
            bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)

        else:
            bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)

        bench_final.columns = [nom_competition]
        st.table(bench_final.style.format("{:.2f}"))


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
        operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)
            bench_final.columns = [nom_competition_1, nom_competition_2]
            bench_final['Moyenne Opérateur'] = 1

            for i in range(10):
                diviseur = 2
                for j in range(2):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1
                if diviseur == 0 :
                    bench_final.iloc[i, -1] = 0
                else :
                    bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i,1]))/diviseur)

            st.table(bench_final.style.format("{:.2f}"))


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
        operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3]
            bench_final['Moyenne Opérateur'] = 1

            for i in range(10):
                diviseur = 3
                for j in range(3):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1
                if diviseur == 0 :
                    bench_final.iloc[i, -1] = 0
                else :
                    bench_final.iloc[i, -1] = "{:.2f}".format(
                    (float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1]) + float(bench_final.iloc[i,2])) / diviseur)
            st.table(bench_final.style.format("{:.2f}"))



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
        operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3,nom_competition_4]
            bench_final['Moyenne Opérateur'] = 1

            for i in range(10):
                diviseur = 4
                for j in range(4):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                if diviseur == 0 :
                    bench_final.iloc[i, -1] = 0
                else :
                    bench_final.iloc[i, -1] = "{:.2f}".format(
                    (float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1]) + float(bench_final.iloc[i,2]) +
                     float(bench_final.iloc[i,3])) / diviseur)
            st.table(bench_final.style.format("{:.2f}"))

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
        operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3, nom_competition_4, nom_competition_5]
            bench_final['Moyenne Opérateur'] = 1

            for i in range(10):
                diviseur = 5
                for j in range(5):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                if diviseur == 0 :
                    bench_final.iloc[i, -1] = 0
                else :
                    bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1])
                                                    + float(bench_final.iloc[i,2]) + float(bench_final.iloc[i,3]) +
                                                           float(bench_final.iloc[i,4])) / diviseur)
            st.table(bench_final.style.format("{:.2f}"))

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
        operateur = st.multiselect('Quel opérateur ?', operateurs, default=operateurs)
        choix_issue = st.radio('Quelles issues possibles ?', ('1-2', '1-N-2'))
        lancement = st.button('Lancez le benchmark')
        if lancement:
            if choix_issue == '1-2':
                bench_final = script_1_2(nb_rencontres, entree_manuelle, operateur)
            else:
                bench_final = script_1_N_2(nb_rencontres, entree_manuelle, operateur)
            bench_final.columns = [nom_competition_1, nom_competition_2, nom_competition_3, nom_competition_4,
                                   nom_competition_5, nom_competition_6]

            bench_final['Moyenne Opérateur'] = 1

            for i in range(10):
                diviseur = 6
                for j in range(6):
                    if bench_final.iloc[i, j] == 0:
                        diviseur -= 1

                if diviseur == 0 :
                    bench_final.iloc[i, -1] = 0
                else :
                    bench_final.iloc[i, -1] = "{:.2f}".format((float(bench_final.iloc[i, 0]) + float(bench_final.iloc[i, 1])
                                                     + float(bench_final.iloc[i, 2]) + float(bench_final.iloc[i, 3]) +
                                                     float(bench_final.iloc[i, 4]) + float(bench_final.iloc[i,5])) / diviseur)

            st.table(bench_final.style.format("{:.2f}"))