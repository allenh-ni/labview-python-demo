import os
import slack
import traceback

# Install slack package with "pip install slackclient=2.0.0"

def send_message(slack_api_token, slack_channel, message):
    os.environ["SLACK_API_TOKEN"] = slack_api_token
    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    try:
        response = client.chat_postMessage(
            channel=slack_channel,
            text=message)
        print('Sent message')
		
    except:
        traceback.print_exc()
        print('Error sending message')

def send_image(slack_api_token, slack_channel, image_filepath):
    os.environ["SLACK_API_TOKEN"] = slack_api_token
    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    try:
        response = client.files_upload(
            channels=slack_channel,
			file=image_filepath.replace('\\','/')) #replace all instances of '\' with '/'
        print('Sent image')
    except:
        traceback.print_exc()
        print('Error sending image')

