import sys
import requests
from bs4 import BeautifulSoup
import re

def parse_html_text(text):
	for line_break in text.find_all("br"):
		line_break.replace_with("\n")

	return text.text;

def get_input_output(url):
	# getting the page from url.
	page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

	# converting the page into soup.
	soup = BeautifulSoup(page.text, "html.parser")

	input_divs = soup.find_all("div", class_="input")
	input_list = list()

	for input_div in input_divs:
		input_list.append(parse_html_text(input_div.find("pre")))

	output_divs = soup.find_all("div", class_="output")
	output_list = list()

	for output_div in output_divs:
		output_list.append(parse_html_text(output_div.find("pre")))

	return input_list, output_list

# Getting the arguments.
# arguments = sys.argv[1:]

# get_intput_output(arguments[0])