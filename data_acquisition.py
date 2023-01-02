import requests
from bs4 import BeautifulSoup
import pandas as pd

url_sonu = 0
liste = []
while url_sonu<=420:
    url = "https://sofifa.com/players?type=all&lg%5B0%5D=13&col=vl&sort=desc&offset="\
          +str(url_sonu)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    cekilen_veri = soup.find_all("table", {"class": "table table-hover persist-area"})
    tablo = (cekilen_veri[0].contents)[len(cekilen_veri[0].contents) - 2]
    tablo1 = tablo.find_all("tr")

    veri = soup.find("table", attrs={"class": "table table-hover persist-area"})
    tablo2 = veri.find_all("td", attrs={"class": "col-name"})

    for name in tablo1:
        player_names = name.find_all("div", {"class": "ellipsis"})
        player_names2 = player_names[0].text

        ages = name.find_all("td", {"class": "col col-ae"})
        ages2 = ages[0].text

        positions = name.find_all("a", {"rel": "nofollow"})
        positions2 = positions[0].text

        clubs = name.find_all("div", {"class": "ellipsis"})
        clubs2 = clubs[1].a.text

        nation = name.find("td", {"class": "col-name"})
        nations = nation.find('img').get('title')

        value = name.find("td", {"class":"col col-vl col-sort"})
        value2 = value.text

        link_sonu = name.a.get("href")
        link_basi = "https://sofifa.com"
        link = link_basi + link_sonu
        link = link.replace('230008/', 'live')
        r_1 = requests.get(link)
        soup1 = BeautifulSoup(r_1.content, "html.parser")
        cekilen_veri2 = soup1.find_all("table")
        a = (cekilen_veri2[0].contents)[len(cekilen_veri2[0].contents) - 2]
        a11 = a.find_all("tr")

        if len(a11) > 1:
            a1 = a11[1]

        elif len(a11) == 1:
            a1 = a11[0]
        elif len(a11) == 0:
            a1 = None


        league = a1.find_all("td", attrs={"class": "col-name text-ellipsis"})
        league2 = league[1].text

        nonBreakSpace = u'\xa0'
        matches = a1.find_all("td", attrs={"class": "col-all col-stat text-right"})
        matches2 = matches[0].text
        matches2 = matches2.replace(nonBreakSpace, '')
        goal = a1.find_all("td", attrs={"title": "Goals"})
        goal2 = goal[0].text
        goal2 = goal2.replace(nonBreakSpace,'')
        shots = a1.find_all("td", attrs={"title": "Shots"})
        shots2 = shots[0].text
        shots2 = shots2.replace(nonBreakSpace, '')
        onTarget = a1.find_all("td", attrs={"title": "On Target"})
        onTarget2 = onTarget[0].text
        onTarget2 = onTarget2.replace(nonBreakSpace, '')
        passes = a1.find_all("td", attrs={"title": "Passes"})
        passes2 = passes[0].text
        passes2 = passes2.replace(nonBreakSpace, '')
        passingAccuracy = a1.find_all("td", attrs={"title": "Passing Accuracy"})
        passingAccuracy2 = passingAccuracy[0].text
        passingAccuracy2 = passingAccuracy2.replace(nonBreakSpace, '')
        keyPasses = a1.find_all("td", attrs={"title": "Key Passes"})
        keyPasses2 = keyPasses[0].text
        keyPasses2 = keyPasses2.replace(nonBreakSpace, '')
        crosses = a1.find_all("td", attrs={"title": "Crosses"})
        crosses2 = crosses[0].text
        crosses2 = crosses2.replace(nonBreakSpace, '')
        crossesAccurate = a1.find_all("td", attrs={"title": "Crosses accurate"})
        crossesAccurate2 = crossesAccurate[0].text
        crossesAccurate2 = crossesAccurate2.replace(nonBreakSpace, '')
        dribblesAttempts = a1.find_all("td", attrs={"title": "Dribbles Attempts"})
        dribblesAttempts2 = dribblesAttempts[0].text
        dribblesAttempts2 = dribblesAttempts2.replace(nonBreakSpace, '')
        dribblesSuccess = a1.find_all("td", attrs={"title": "Dribbles Success"})
        dribblesSuccess2 = dribblesSuccess[0].text
        dribblesSuccess2 = dribblesSuccess2.replace(nonBreakSpace, '')
        dribbledPast = a1.find_all("td", attrs={"title": "Dribbled Past"})
        dribbledPast2 = dribbledPast[0].text
        dribbledPast2 = dribbledPast2.replace(nonBreakSpace, '')
        dribblesDispossessed = a1.find_all("td", attrs={"title": "Dribbles Dispossessed"})
        dribblesDispossessed2 = dribblesDispossessed[0].text
        dribblesDispossessed2 = dribblesDispossessed2.replace(nonBreakSpace, '')
        duels = a1.find_all("td", attrs={"title": "Duels"})
        duels2 = duels[0].text
        duels2 = duels2.replace(nonBreakSpace, '')
        duelsWon = a1.find_all("td", attrs={"title": "Duels Won"})
        duelsWon2 = duelsWon[0].text
        duelsWon2 = duelsWon2.replace(nonBreakSpace, '')
        tackles = a1.find_all("td", attrs={"title": "Tackles"})
        tackles2 = tackles[0].text
        tackles2 = tackles2.replace(nonBreakSpace, '')
        interceptions = a1.find_all("td", attrs={"title": "Interceptions"})
        interceptions2 = interceptions[0].text
        interceptions2 = interceptions2.replace(nonBreakSpace, '')
        blocks = a1.find_all("td", attrs={"title": "Blocks"})
        blocks2 = blocks[0].text
        blocks2 = blocks2.replace(nonBreakSpace, '')
        foulsCommitted = a1.find_all("td", attrs={"title": "Fouls Committed"})
        foulsCommitted2 = foulsCommitted[0].text
        foulsCommitted2 = foulsCommitted2.replace(nonBreakSpace, '')
        foulsDrawn = a1.find_all("td", attrs={"title": "Fouls Drawn"})
        foulsDrawn2 = foulsDrawn[0].text
        foulsDrawn2 = foulsDrawn2.replace(nonBreakSpace, '')
        yellowCards = a1.find_all("td", attrs={"title": "Yellow Cards"})
        yellowCards2 = yellowCards[0].text
        yellowCards2 = yellowCards2.replace(nonBreakSpace, '')
        redCards = a1.find_all("td", attrs={"title": "Red Cards"})
        redCards2 = redCards[0].text
        redCards2 = redCards2.replace(nonBreakSpace, '')
        saves = a1.find_all("td", attrs={"title": "Saves"})
        saves2 = saves[0].text
        saves2 = saves2.replace(nonBreakSpace, '')
        insideBoxSaves = a1.find_all("td", attrs={"title": "Inside Box Saves"})
        insideBoxSaves2 = insideBoxSaves[0].text
        insideBoxSaves2 = insideBoxSaves2.replace(nonBreakSpace, '')
        penaltySaved = a1.find_all("td", attrs={"title": "Penalty Saved"})
        penaltySaved2 = penaltySaved[0].text
        penaltySaved2 = penaltySaved2.replace(nonBreakSpace, '')
        cleanSheets = a1.find_all("td", attrs={"title": "Clean Sheets"})
        cleanSheets2 = cleanSheets[0].text
        cleanSheets2 = cleanSheets2.replace(nonBreakSpace, '')

        liste.append([player_names2, ages2, positions2, clubs2, nations,value2,league2,matches2,goal2,shots2,onTarget2,passes2,
                     passingAccuracy2,keyPasses2,crosses2,crossesAccurate2,dribblesAttempts2,dribblesSuccess2,
                     dribbledPast2,dribblesDispossessed2,duels2,duelsWon2,tackles2,interceptions2,blocks2,
                     foulsCommitted2,foulsDrawn2,yellowCards2,redCards2,saves2,insideBoxSaves2,penaltySaved2,
                     cleanSheets2])
        data = pd.DataFrame(liste, columns=["name", "age", "position", "club", "nation", "value", "league", "matches", "Goals",
                                            "Shots", "On Target", "Passes", "Passing Accuracy", "Key Passes", "Crosses",
                                            "Crosses accurate", "Dribbles Attempts", "Dribbles Success","Dribbled Past",
                                            "Dribbles Dispossessed", "Duels", "Duels Won", "Tackles", "Interceptions",
                                            "Blocks", "Fouls Committed", "Fouls Drawn", "Yellow Cards", "Red Cards",
                                            "Saves", "Inside Box Saves", "Penalty Saved", "Clean Sheets"])

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)

        #print(data)
        data.to_csv('players.csv')
    url_sonu += 60