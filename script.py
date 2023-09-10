#! /usr/bin/env python3
import os
import requests

url = ''
input_directory = ''

def read_feedback_files(input_directory):
	feedback_list  = []
	files =  os.listdir(input_directory)

	for filename in files:
		if filename.endswith('.txt'):
			feedback_dict = {}
			file_path = os.path.join(input_directory, filename)

			with open(file_path, 'r') as file:
				lines  =  file.readlines()
				feedback_dict['title'] = lines[0].strip()
				feedback_dict['name'] = lines[1].strip()
				feedback_dict['date'] = lines[2].strip()
				feedback_dict['feedback'] = lines[3].strip()

				feedback_list.append(feedback_dict)
	return feedback_list


def upload_feedback(feedback_data):
	for feedback in feedback_data:
		response = requests.post(url, json=feedback)
		if response.status_code == 201:
			print(f"Feedback uploaded succesfully: {feedback['title']}")
		else:
			print(f"Failed to upload feedback: {feedback['title']}")

if __name__ == "__main__":
	feedback_data = read_feedback_files(input_directory)
	upload_feedback(feedback_data)
