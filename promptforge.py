import os
import json

def generate_prompt(user_id, prompt_type):
    # Simulate generating a prompt based on user preferences
    prompt = f'Generate a {prompt_type} for user {user_id}.'
    return prompt

if __name__ == '__main__':
    user_id = '12345'
    prompt_type = 'feature_request'
    prompt = generate_prompt(user_id, prompt_type)
    print(prompt)