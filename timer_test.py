from inputimeout import inputimeout,TimeoutOccurred

try:
    answer = inputimeout(
        prompt="Type something within 10 seconds: ",
        timeout=10
    )
    print("You typed:", answer)

except TimeoutOccurred:
    print("Time is up!")

    
      

