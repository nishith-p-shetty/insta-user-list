from insta_scraper import InstagramScraper
import argparse
import logging

logging.basicConfig(level=logging.INFO)

print("\tInstagram User List Creater..... by nishith-p-shetty")
def main():
	parser = argparse.ArgumentParser(description='Instagram followers scrapper')
	parser.add_argument('--username', dest='username', action='store')
	parser.add_argument('--password', dest='password', action='store')
	args = parser.parse_args()

	scrapper = InstagramScraper(args.username, args.password)
	logging.info(" Creating session")
	scrapper.create_session()

	logging.info(" Extracting followers")
	scrapper.scrape_followers()

	logging.info(" Extracting followees")
	scrapper.scrape_following()

	logging.info(" Generating user list. Please check user_list.txt text file")
	scrapper.generate_unfollowers_list()

if __name__ == '__main__':
	main()