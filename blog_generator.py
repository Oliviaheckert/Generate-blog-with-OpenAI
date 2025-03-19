import openai
from dotenv import dotenv_values

# Load API key from .env file
config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    try:
        response = openai.completions.create(
            model = 'gpt-3.5-turbo-instruct',
            prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
            max_tokens = 400, # Determines how long response is, token limit = 4096
            temperature = 0.3 # Determines randomness of response, 0 = same response every time, 1 = different response every time, even if it's the same prompt
        )

        retrieve_blog = response.choices[0].text
        return retrieve_blog
    except Exception as e:
        return f"An error occured: {e}"


# Multiple paragraphs
keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for Yes, anything else for No: ')
    if (answer == 'Y'):
        paragraph_topic = input('What is the topic of the paragraph? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
        print('Thank you for using the blog generator!')