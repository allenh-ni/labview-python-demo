import os
import slack

# Slack API TOKEN for Allen Hsu's Slack channel and bot.  https://acme-o519989.slack.com/
#os.environ["SLACK_API_TOKEN"] = "xoxb-626226701445-614843941202-VxQ9ikZlFiSLhgmTvIOQmBls"
#slack_token = os.environ["SLACK_API_TOKEN"]
#client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

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


# postMessage(message="Test passed. Would you like to run the test again?", imageAddress=r"C:\Users\sw marketing\Desktop\BYOATE\Support files & VIs\Test Code\Filter Test\CurrentTest.jpg")
# waitForResponse()