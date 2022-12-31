import requests
from bs4 import BeautifulSoup
import json

def get_daily_challenge_data() -> dict:

    daily_challenge_url = get_daily_challenge_url()
    return get_problem_data(daily_challenge_url)

def get_problem_data(problem_url:str) -> dict:

    problem_url = get_daily_challenge_url()
    problem_page_soup = get_page_soup(problem_url)
    
    data_container = problem_page_soup.find('script', {'id':'__NEXT_DATA__'}).getText()
    raw_problem_data = json.loads(data_container)['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['question']
    
    problem_data = {'title':raw_problem_data['title'], 
                    'difficulty':raw_problem_data['difficulty'], 
                    'likes':raw_problem_data['likes'], 
                    'dislikes':raw_problem_data['dislikes'], 
                    'url':problem_url}
    
    return problem_data

def get_daily_challenge_url() -> str:

    main_page_url = 'https://leetcode.com/problemset/all/'
    main_page_soup = get_page_soup(main_page_url)
    
    green_circle_class = 'h-7 w-7 bg-green-s dark:bg-dark-green-s hover:bg-green-3 dark:hover:bg-dark-green-3 text-white flex items-center justify-center rounded-full'
    dailiy_challenge_url = main_page_soup.find('span',{'class':green_circle_class}).parent['href']
    
    return 'https://leetcode.com' + dailiy_challenge_url

def get_page_soup(url:str) -> BeautifulSoup:
	
    webp = requests.get(url)
    return BeautifulSoup(webp.text, 'html.parser')