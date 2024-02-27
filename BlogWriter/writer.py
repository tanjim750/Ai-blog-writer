import openai
import google.generativeai as genai

# Set your OpenAI API key
openai.api_key = "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"
def palm_writer(prompt):
    genai.configure(api_key="AIzaSyBBOWhVsNNn4slbGIQhWCG8weeGz4Hv26k")

    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message(prompt)
    return convo.last.text

def chatgpt_writer(gpt_prompt):
    # Request content from the GPT model
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # You can adjust the engine based on your needs
        prompt=gpt_prompt,
        temperature=0.7,  # Adjust the temperature for creativity (0.0 for deterministic, 1.0 for maximum creativity)
        max_tokens=800,  # Adjust the max tokens to control response length
        n=1,
        stop=None  # You can specify a stop sequence if needed
    )

    # Extract and return the generated content
    return response['choices'][0]['text']

def generate_prompt(user_topic):
    prompt = '''
    # Generate a blog post
    
    ## Introduction
    Write a captivating introduction about {user_topic}, providing a brief overview and generating interest.
    
    ## Topic Diversity
    Discuss various aspects of {user_topic}, utilizing H2 and H3 headings as needed. Highlight key elements, such as variations, unique features, and any cultural or ecological significance.
    
    - Incorporate subsections with relevant details based on {user_topic}.
    
    ## Unique Features
    Create an H2 heading for this section. Explore the distinctive traits of {user_topic}, focusing on any special characteristics or adaptations it may have.
    
    - Use H3 headings to delve into specific aspects or features.
    
    ## Visual Elements
    If applicable, include images or visual elements to enhance the content. Utilize the <img> tag for image embedding.
    
    ## Conclusion
    Conclude the blog with a summary that emphasizes the importance or fascination of {user_topic}. Encourage further exploration or discussion.
    
    # Ensure the generated content is in HTML format, utilizing <h2>, <h3>, <p>, <li>, <ul>, <table>, <img>, and other relevant HTML tags.
    '''

    prompt = prompt.replace('{user_topic}',user_topic)
    return prompt

