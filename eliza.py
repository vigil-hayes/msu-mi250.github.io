import random
import sys

# List of inputs and possible responsxes
responses = [
  ("hello",                                                       # Prompt
     ["Hello!  Glad you could be here today.",                    # Possible respons
      "Hi there.  How are you today?",                            # Possible respons
      "Hello, how are you feeling today?"                         # Possible respons
      ]),
  ("mother",
     ["Tell me more about your mother",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?"
      ]),
  ("father",
     ["Tell me more about your father",
      "What was your relationship with your father like?",
      "How do you feel about your father?"
      ]),
  ("i feel",
     ["Good, tell me more about those feelings",
      "Do you often feel that?",
      "When you feel that way, what do you do?"
      ]),      
  ("i am",
     ["How long have you been that way?",
      "How do you feel about that?",
      "Why do you think you are like that?"
      ]),      
  ("",
     ["Please tell me more",
      "Can you elaborate on that?",
      "I see",
      "How does that make you feel?",
      "How do you feel when you say that?"
      ]),
  ]

##################################################################################
#### This is the code that asks the user for input, and then prints out a response


# Begin by asking the user a question
print("Welcome to Eliza!")
print("How are you feeling today?")

while True:                                    # Keep going forever
  resp = input("> ").lower()              # Ask the user for input, and save it in the "input" variable
  if "goodbye" in resp:                       # Check and see if the user said goodbye
    print("Goodbye!")                          #   If they did, say goodbye back
    sys.exit(0)                                #   and then exit (end) the program
                                               # If we get here, then the user didn't say goodbye.  So let's figure out how to response
  for response in responses:                   # Look through all of the possible reponses listed above
    if response[0] in resp:                   #   Check if what the user said is the prompt we are looking at
      print(random.choice(response[1]))        #     If the prompt matches, then choose a random response and print it out for the user
      break                                    #     If the prompt matches, then stop looing for more prompts so we don't print out more than one response



