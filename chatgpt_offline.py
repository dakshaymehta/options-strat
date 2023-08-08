# Import the necessary libraries
import openai

# Set the OpenAI API key
openai.api_key = "API_KEY"

# Function to generate a response from ChatGPT
def generate_response(user_input):
    # Use the OpenAI API to generate a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        temperature=0.5
    )

    # Return the generated response
    return response["choices"][0]["text"]

# Main function to run ChatGPT
def run_chatgpt():
    # Continuously prompt the user for input
    while True:
        user_input = input("User: ")

        # Generate a response from ChatGPT
        response = generate_response(user_input)

        # Print the response from ChatGPT
        print("ChatGPT: " + response)

# Run ChatGPT
run_chatgpt()
