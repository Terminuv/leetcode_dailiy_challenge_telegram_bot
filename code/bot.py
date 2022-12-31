import requests
from lc_parser import get_daily_challenge_data
import time

def main():

	chat_id = 'Replace with the ID of the chat where you want the message to be sent'

	last_exec = 1672383600
	secs_in_day = 86400

	while True:

		cur_time = int(time.time())

		if cur_time >= last_exec + secs_in_day:
			send_daily_challenge_info(token, chat_id)
			last_exec = cur_time

		time.sleep(3600)

def send_daily_challenge_info(token, chat_id) -> None:
	
	for _ in range(5):
		try:
			message = generate_message()
			break
		except KeyError:
			message = 'Error'

	telegram_send_message(token, chat_id, message)

	return None

def generate_message() -> str:
	dc_data = get_daily_challenge_data()

	title = dc_data['title']
	dif = dc_data['difficulty']
	likes = dc_data['likes']
	dislikes = dc_data['dislikes']
	url = dc_data['url']

	message = f'{title}\nDifficulty: {dif}\nLikes: {likes}\nDislikes: {dislikes}\n{url}'
	return message

def telegram_send_message(token:str, chat_id:str, text:str) -> None:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    requests.post(url,json=payload)
    return None

if __name__ == '__main__':
	main()
