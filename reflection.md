# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The hints were misleading
          - example: One of the anwers was 40, when I put 100 it said to go lower, but when I made it 50 it said to go higher

    Another thing I noticed was how the difficulty did not match the amount of attempts you were given

    Once you selected the play a new game button a new game would not start

    Using the Developer debug information I noticed how the Score was the one managing wether or not the user needed to increase the number
    rather than the secret

    The developer debug information also showed how the game wouldnt restart the history so it wasnt starting a game when changing the difficuty

    Another Issue was how you could not press enter to submit a response



- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

    1. The hints were extremely misleading
    2. The new game button did not work
    3. The difficutly headings did not match the actual difficulty of the games

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    
    The AI tool I used on this project was CLAUDE code


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

    One example would be when I told it to fix the hints being misleading. Claude was able to identify that there was a problem with the logic, and 
    fixed it. I verified these results by going to the line which it was going to change in this case line 38-41 on the app.py file and reviewed the logic
    myself. I too realized the logic was incorrect and that Claudes suggestions was correct.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    

    One example where Claude suggestion was incorrect or misleading was when I was fixing displayed attempts. The issues was that the number being shown previously was incorrect and misleading. It took Claude a while to figure out what the issue was, at first it tried to simply change the attempts the program displayed but after a couple prompts and verification by checking the code myself and playing around with the updated app, it was able to realize the logic error was somewhere else and fixed it.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    With continous testing using the code it produced after making a change, I was able to decide 
    whether a bug was really fixed only if it passed my testing.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
      One test I ran manually was the start new game button. It showed me that there was an issue 
      with the program not properly resetting the values and something needed to be changes.
- Did AI help you design or understand any tests? How?
      AI did in fact help me understand why the attempts were not being properly displayed. Initially 
      I thought that it was simply because something was wrong with the variables but turns out it was
      the way Streamlit was rendering the application. Meaning it was code rendering order issue not logic.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
    The secret number was cast to a string causing comparison issues which would affect the hints as well.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    Streamlit reruns just rerun your entire script again from top to bottom. It is important to have session states
    because those variables are the only ones that dont get refreshed/reset when a rerun happens.
- What change did you make that finally gave the game a stable secret number?
    Removed the if/else blocks and made sure to check the guess with the integer from secret directly.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
    Always testing the code multiple times. Running the program with different test cases really helped me understand what was wrong and what I needed to fix. Also, making a CLAUDE.md was super helpful, claude had all the background it needed inside that md file so it saved me a lot of time and the output of the AI was a lot better.

  - This could be a testing habit, a prompting strategy, or a way you used Git.


- What is one thing you would do differently next time you work with AI on a coding task?

    One thing I would do differently is spending a bit more time understanding the code itself. A lot of time could have been saved, if I just spent an extra 30 minutes examining the code and noting where issues could arise.


- In one or two sentences, describe how this project changed the way you think about AI generated code.

    AI generated code is only as powerful as the Prompt. AI works better with smaller task at a time. 
