import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

json_data = {
    'clientKey': '4825b001bd2176c64997b1936297293e',
    'task': {
        'type': 'RecaptchaV2TaskProxyless',
        'websiteURL': 'http://makeawebsitehub.com/recaptcha/test.php',
        'websiteKey': '6LfI9IsUAAAAAKuvopU0hfY8pWADfR_mogXokIIZ',
    },
    'softId': 0,
}

response = requests.post('http://147.93.3.89:8181/createTask', headers=headers, json=json_data)
print(response.json())
task_id = response.json().get('taskId')
if task_id:
    # Second request: Get the hCaptcha solution
    data = {
        "clientKey": "4825b001bd2176c64997b1936297293e",  # Your API client key
        "taskId": task_id,
    }

while True:
    
        response = requests.post('http://147.93.3.89:8181/getTaskResult', headers=headers, json=data)
        task_result_response = response.json()

        if task_result_response.get('status') == 'ready':
            # The solution is ready
            print("Captcha Solved:", task_result_response.get('solution').get('text'))
            break


# First request: Create hCaptcha solving task
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

# Replace these values with your specific target website and API key
json_data = {
    'clientKey': '4825b001bd2176c64997b1936297293e',  # Your API client key
    'task': {
        'type': 'HCaptchaTaskProxyless',  # Type for hCaptcha
        'websiteURL': 'https://hawspets.givecloud.co/give',  # Replace with the target website URL
        'websiteKey': 'y98e5065c-ad73-4417-a8ce-f8b296e69cf6',  # Replace with the website's hCaptcha site key
    },
    'softId': 0,
}

# Create the task
response = requests.post('http://147.93.3.89:8181/createTask', headers=headers, json=json_data)
create_task_response = response.json()
print("Create Task Response:", create_task_response)

# Extract taskId from the response
task_id = create_task_response.get('taskId')

if task_id:
    # Second request: Get the hCaptcha solution
    data = {
        "clientKey": "4825b001bd2176c64997b1936297293e",  # Your API client key
        "taskId": task_id,
    }

    # Poll the task result
    while True:
        response = requests.post('http://147.93.3.89:8181/getTaskResult', headers=headers, json=data)
        task_result_response = response.json()
        print("Task Result Response:", task_result_response)

        if task_result_response.get('status') == 'ready':
            # The solution is ready
            print("Captcha Solved:", task_result_response.get('solution'))
            break
