# Import the necessary libraries
import speech_recognition as sr
import os

# Set up the speech recognition
r = sr.Recognizer()

# Function to recognize speech and return the result
def recognize_speech():
  # Record the user's audio
  with sr.Microphone() as source:
    audio = r.listen(source)

  # Try to recognize the speech
  try:
    return r.recognize_google(audio)
  except sr.UnknownValueError:
    return "I'm sorry, I didn't understand what you said."
  except sr.RequestError:
    return "I'm sorry, I am unable to process your request at this time."

# Function to respond to the user's input
def respond(user_input):
  # If the user says "hello", respond with a greeting
  if "hello" in user_input.lower():
    return "Hello there! How can I help you?"
  # If the user says "goodbye", respond with a farewell
  elif "goodbye" in user_input.lower():
    return "Goodbye! It was nice chatting with you."
  # If the user says anything else, respond with a default message
  else:
    return "I'm sorry, I am not sure how to respond to that. Could you please rephrase your question?"

# Main function to run the AI assistant
def run_assistant():
  # Continuously prompt the user for input
  while True:
    user_input = recognize_speech()
    response = respond(user_input)
    print(response)

# Run the AI assistant
run_assistant()
