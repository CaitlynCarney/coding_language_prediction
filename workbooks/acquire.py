import os
import time
import json
from bs4 import BeautifulSoup
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username
#-----------------------------------------------------------------------------


# Imports

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup
import os
import time
# scroll down for exercise functions


def tasty_soup(url):
    '''Takes in a url, requests, and parses the HTML
    returns a tasty little soup
    '''
    # set header to gain access
    headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}
    # set up the response variable
    response = requests.get(url, headers=headers)
    # create html
    html = response.text
    # use that tasty little soup
    soup = BeautifulSoup(html)
    # return soup
    return soup

def get_doctor_who_urls():
    '''
    scrapes github for all repos about Doctor Who
    search for Doctor Who and return a list of the repo urls.
    '''
    # get the first 100 pages
    pages = range(1, 101)
    # create a blank list for url's to be added
    urls = []
    # loop through the pages
    for p in pages:
        # base url for doctor who repos
        url = f'https://github.com/search?p={p}&q=doctor+who&type=Repositories'
        # make that tasty little soup
        soup = tasty_soup(url)
        # anchor it to v-align-middle
        page_urls_list = soup.find_all('a', class_='v-align-middle')
        # grab the 'href' link for each url
        page_urls = {link.get('href') for link in page_urls_list}
        # make a list to hold the repo urls
        page_urls = list(page_urls)
        # append the list from the page to the full list
        urls.append(page_urls)
        time.sleep(5)
    urls = [y for x in urls for y in x]
    # return urls
    return urls

REPOS = ['eccentricdevotion/TARDIS',
 'kuralabs/reactive-core-doctor-who-web',
 'fwallacephd/doctor-who',
 'kuralabs/reactive-core-doctor-who-core',
 'kuralabs/reactive-core-doctor-who-mobile',
 'WhoCraft/Weeping-Angels',
 'GeekInTheClass/DoctorWho',
 'dana-ross/doctor-who-episodes',
 'WhoCraft/Regeneration',
 'maz/blinking-angel',
 'markduwe/doctorwho',
 'ju-moulin/HTML_Projet-1_DoctorWhoCV',
 'pratush07/DoctorWho',
 'generalbrus/Generalbrus.github.io',
 'Schlenges/doctor-who-quote-api',
 'alicescfernandes/random-who',
 'oojas/flutter-doctor',
 'slastonm/Doctor_who',
 'codeforpakistan/Doctor-Finder',
 'onur-kaplan/Clickable-human-body-drawn-with-SVG',
 'pyropeter/K-9',
 'jhabarsingh/DOCMED',
 'margaretkroll/Who',
 'andreas0607/Doctorwho',
 'MCS-Kaijin/WhoScript',
 'jiminycricket/doctor-who-ghost-blog',
 'slychika/csci3155Paper',
 'cecilmillerioux/who',
 '23carnies/doctor-who-api',
 'CorentinTh/doctor-who',
 'Emanuelpna/doctor-who-quiz',
 'MoeRayo/Doctor-who-s-Quiz-App',
 'hexagon-software/Akhaten',
 'Joh316/doctor-who2',
 'dana-ross/catalogopolis-api',
 'franciscomemoli/medicalOffice',
 'mcandre/who',
 'eccentricdevotion/TARDISWeepingAngels',
 'jofelipe/css3-tardis',
 'Virag007/DoctorData',
 'ecmoore/doctor-who',
 'dracos/who-said',
 'bernie-haxx/Doctor-Patient',
 'Joh316/doctor-who',
 'Zaqweli/DoctorWho',
 'Kirashi0052/doctor-who',
 'Rahul-Lal/whoisthedoctor',
 'priera85/DoctorWho',
 'omiq/arduino_sd_wav',
 'anonymous033/DoctorWho',
 'Didarrius/DoctorWho',
 'RomanMiniv/DoctorWho',
 'eddidu/doctorWho',
 'fireaxil/DoctorWho',
 'maxxfly/DoctorWho',
 'King-Pin/DoctorWho',
 'abduljama/DoctorWho',
 'Nin1963/DoctorWho',
 'EthanWGerard/DoctorWho',
 'nan0jingxuan/DoctorWho',
 'nikgaru/doctorWho',
 'kaxuna1/doctorWho',
 'Tamer-Assaliya/DoctorWho',
 'guimaraeskellen/DoctorWho',
 'areejimair/DoctorWho_',
 'rocketboy376/DoctorWho',
 'jesstoh/DoctorWho',
 'DanNimara/DoctorWho',
 'MichelleBindel/WhoIsWhoOnDoctorWho',
 'dzenjadu/DoctorWho',
 'pokojt/doctorWho',
 'mywebsites-aj/mywebsites-aj.github.io',
 'doctor11/doc',
 'elena1905/DoctorWho',
 'EddyAtPessac/DoctorWho',
 'faboo/whogame',
 'ShkSalmanAhmad/DoctorWho',
 'JuliBilto/doctor-who-css-2',
 'Smurfe/Doctor-Who',
 'Cloudash/Doctor-Who',
 'BridgetVioletAvila/Doctor-Who',
 'dxa4481/theDoctorWithoutBoardersIsIn',
 'WhoCraft/WhoCosmetics',
 'Bunnbuns/Doctor-Who',
 'cerita/doctor-who',
 '2048online/Doctor-Who',
 'haseren4/DoctorWhoInvasionoftheDaleks',
 'Stefanmikulic/DoctorWhoTestMod',
 'trevorKirkby/doctorWhoGame',
 'charlottebrf/DoctorsWhoCode',
 'RunYouCleverBoy/DoctorWhoEpisodePicker',
 'aurelieclavier/doctorWhoRoot',
 'matthewmmorrow/DoctorWhoLARP',
 'MatthewaHamlet/doctorWhoDiceGame',
 'Stefanmikulic/DoctorWhoTestMod',
 'DoctorWhoFR/DoctorWhoFR',
 'staygolder/doctor-who-css',
 'charlottebrf/DoctorsWhoCode',
 'Hiba-alkurd/DoctorWhoCore',
 'chaos2007/doctorWhoTime',
 'Quacky2200/DoctorWho-AdventureGame',
 'vincentGuegan/DoctorWhoProject',
 'FireShootSK/DoctorWhoSound',
 'MatthewaHamlet/doctorWhoDiceGame',
 'romulobr/doctor-who-guide-android',
 'ChristineMOBrien/Doctor-Who-Website',
 'dabdulmyanov-zz/doctor-who-css',
 'alysekassa/doctor-who-css',
 'Maurice8750/Witch-Doctor',
 'Yalonso522/Doctor-Who-Session-02',
 'Yalonso522/doctor-who-css',
 'i4mthorish/Doctor-Who-Comic',
 'giorgi616/doctor-who-fan',
 'sandra023/Doctor-Who-Pacman',
 'mollytb/DoctorWhoNoDoubleClick',
 'danielbmathews/doctor_who',
 'LouiseLeal/DoctorWhoRpg2.0',
 'Smytt/Whoniverse---Doctor-Who-RPG-Game',
 'ANPez/WhoApi',
 'hannahcgunderman/INSC590-OSF-DoctorWho',
 'SolarDrew/Doctor-Who',
 'emgrasmeder/whoapp',
 'akpersad/Angular_Quiz',
 'fwallacephd/whoviangirl',
 'aserrao12/alexberen.github.io',
 'moonejon/trivia-game',
 'zemogle/doctorwho_skill',
 'AlkanetSmorgas/Arma-3-Weeping-Angels-Mod',
 'osborfg024/doctorwho',
 'brygphilomena/Gallifreyan-Circles',
 'TheRealKaneras/DWM',
 'Nmaher01/Doctor-Who',
 'jaclynbarrera/doctor-who',
 'NotArpit/Doctor-Who',
 'madeleineschwartz01/doctor-who',
 'ColineMorel/Doctor-Who',
 'KaylaRichardson/Doctor-Who',
 'Sellig20/Doctor_Who',
 'amskjold/doctor-who',
 'asantos08/Doctor-Who',
 'frabcus/kill-the-moon',
 'bhester4/weddingDW',
 'aseitz94/TriviaGame',
 'dariusk/doctorwhat',
 'monicaduconge/doctor-who',
 'kr4ckhe4d/doctor-who',
 'TDRC/doctor-who',
 'trentgillin/Doctor_Who',
 'smith86n/Doctor-who',
 'watermellon2018/doctor-who',
 'AnthonyCAmiano/doctor-who',
 'clintmad/doctor-who',
 'yyd007/Doctor-who',
 'PatrickJHenry/Doctor-Who',
 'KatieFujihara/doctor-who',
 'katiehyche/doctor-who',
 'vamsin07/Doctor-Who',
 'AnnaD1992/doctor-who',
 'giselleblanco/Doctor-Who',
 'AnnCa44/Doctor-Who',
 'Lindsay-Gulla/Doctor-Who',
 'ChristineMOBrien/doctor-who',
 'BrittneyMesa/Doctor-Who',
 'dabdulmyanov-zz/Doctor-Who',
 'LivClemente/doctor-who',
 'juliamschwartz/doctor-who',
 'Cjay1214/doctor-who',
 'b21986176/Doctor_Who',
 'colebmoore/Doctor-Who',
 'christinabahnatka/doctor-who',
 'Amandag328/Doctor-Who',
 'Hiba-alkurd/Doctor-Who',
 'ConstanceLuo/Doctor-Who',
 'mehmetcelikhan/Doctor-Who',
 'kevin-amatulli/Doctor-Who',
 'hetaJ/Doctor_who',
 'aharker619/Doctor-who',
 'Jess-Nguy/Doctor-Who',
 'CaitlinKempinski/doctor-who',
 'tanysaur/TriviaGame',
 'arielperalta/Doctor-Who',
 'rasponicc/doctor-who',
 'skyfox93/Doctor-Who',
 'RyanMoeller/doctor-who',
 'manza33/doctor_who',
 'liaoliveras/doctor-who',
 'taldridge01/Doctor-Who',
 'mariettasnia/doctor-who',
 'Pratyuxh/doctor-who',
 'Mara-K/Who_Project_Markup',
 'thomas-rex-mitchell/Doctor-Who',
 'efficacy/doctor-who-mf',
 'kalvarez01/Doctor-Who',
 'davorg/whonews.tv',
 'Splodge97/DoctorWhoClubPenguinTresureHunt',
 'javglex/FlappyWho',
 'katyanna/who-quotes',
 'macey26/dr-who-tardis-game',
 'GiaLucia/doctor-who-css',
 'KaylaRichardson/doctor-who-css',
 'JamesOConnor1993/doctor-who-css',
 'Nommington/Doctor-Who-Memory',
 'teddiemucha/doctor-who-css',
 'IctorM/doctor-who-stat-tracker',
 'dethtron5000/dr_who_grabber',
 'alysekassa/Doctor-Who-Version-2',
 'souldreamer/whos-your-doc',
 'GiaLucia/doctor-who-css-1',
 'isylumn/Alt-Doc-Who',
 'PatrickJHenry/doctor-who-css',
 'great-os/doctor.who.reference',
 'talitastravassos/doctor-who-tribute',
 'giselleblanco/doctor-who-css',
 'bachzz/Doctor-Who-Intro',
 'KaylaRichardson/Doctor-Who-Version-2',
 'wholmesian/Doctor-Who-NLP',
 'CardinisCode/Doctor-Who-Directory',
 'matthewesp/Doctor-Who-Quote-Generator',
 'nicolepeltier/doctor-who-css',
 'Amandag328/doctor-who-css',
 'robdude456/s',
 'giselleblanco/Doctor-Who-Version-2',
 'wrstone/fonts-doctorwho',
 'JamesOConnor1993/Doctor-Who-Version-2',
 'chiragmb96/dotnet-Doctor-who',
 'ragad/Doctor-Who-master',
 'kevin-amatulli/doctor-who-css',
 'kuramoriz/pygame_doctor_who_game',
 'lynmuldrow/Doctor-Who-Countdown-',
 'A1L33N/doctor_who_meme',
 'nicolepeltier/Doctor-Who-Version-2',
 'LinkXXI/Doctor-Who-Wallpaper-Changer',
 'manuel-dileo/doctor-who-dataset',
 'MrsG-ood/Doctor-Who-Tribute-Page',
 'ChristineMOBrien/doctor-who-website-thusfar',
 'staygolder/Doctor-Who-Version-2',
 'versesopm/Doctor-Who-Game',
 'JavaOfDoom/doctor-who-tribute-page',
 'llamaCode/Doctor-Who-Sketch',
 'Isauregastinne/doctor-who-css',
 'jordanjrh/doctor_who_quiz',
 'meisterelijah/Doctor-Who-Shooter',
 'melansob/Doctor-Who-DB',
 'ColineMorel/doctor-who-css',
 'Akarrou/doctor_who_ex2',
 'jgcreiglow/doctor-who-clicky-game',
 'sdrothco/doctor-who-quiz',
 'Tamer-Assaliya/EFCoreDoctorWho',
 'lisette1104/Doctor-Who-Project-',
 'angewzhao/doctor-who-dialogue-tracker',
 'bradleygamboa/Doctor-Who-Hangman',
 'ByteAbyss/Doctor_Who_Collection_Management',
 'JuliBilto/Doctor-Who---Session-02',
 'JiatengSun/Doctor-Who-test-project',
 'JavaOfDoom/doctor-who-survey-page',
 'JuanmaCG/WebDoctorWho',
 'Lyr071/doctor-who-stories',
 'cBridges851/Doctor-Who-Procedural-Program',
 'melansob/Doctor-Who-Story',
 'melansob/RPG-Doctor-Who-Story',
 'mkrill/Spring-02-Doctor-who',
 'AntonioAlegriaH/doctor-who-episodes-dataset',
 'Yalonso522/Doctor-Who-Version-2',
 'clholgat/Asteroids',
 'averyethomas/film-sync-doctor-who',
 'nmetzger1/doctor-who-scraper',
 'codingdesigner/doctor-who-streaming',
 'pingzing/doctor-who-soundboard',
 'samyuktasreekanth-cit/Doctor-Who-Project',
 'kalgynirae/doctor-whosical-songs',
 'Shamrez181/Doctor-Who-Interactive-Comic',
 'JHill89/Assignment-4',
 'elliewiekamp/doctor-who-css',
 'BridgetVioletAvila/Doctor-Who-master',
 'ads04r/doctor-who-rdf',
 'kevin-amatulli/Doctor-Who-Version-2',
 'adamwalter/doctor-who-randomizer',
 'Mars-75/Fan_Game_Doctor_Who',
 'harofax/Attack_of_the_Daleks',
 'Cambasra/Doctor-who.web',
 'DChang87/Paint-Project',
 'Yejin423/Doctor-Who-Web',
 'STGRobotics/K9',
 'UserCake/Gallifrey',
 'Graphmatic/tardis']

# creating the header to gain access to github scrapping
headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}
# create a loop
if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it")
#-----------------------------------------------------------------------------

def github_api_request(url: str) -> Union[List, Dict]:
    '''Take in url and header
    create json for it
    loop through respnse codes
    return the json file created'''
    # take in a url and the header
    response = requests.get(url, headers=headers)
    # create a json for the url
    response_data = response.json()
    # loop through the response codes
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)},"
            f"url: {url}")
    # return json
    return response_data


def get_repo_language(repo: str) -> str:
    '''Look for the coding languages in the repo(s)'''
    # take in the url(s)
    url = f"https://api.github.com/repos/{repo}"
    # get the info from the repo
    repo_info = github_api_request(url)
    # look thorugh the information
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        # specifically look for coding language
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    '''Look for the remaining content in the repo'''
    # take in the url(s)
    url = f"https://api.github.com/repos/{repo}/contents/"
    # get the repo informaiton
    contents = github_api_request(url)
    # look through the information (specifically content)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api 
    lists the files in a repo
    returns the url that can be used to download the repo's README file.
    """
    # look at each individual file
    for file in files:
        # look for readme's
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like 
    returns a dictionary with the coding language and the readme contents.
    """
    # get the contents
    contents = get_repo_contents(repo)
    # get readme contents
    readme_download_url = get_readme_download_url(contents)
    # create a readme contents to loop
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)
