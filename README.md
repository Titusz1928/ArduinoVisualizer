To run this project you need:
  -an arduino board
  -Arduino IDE
  -Python IDE ( I used pycharm)

1. First upload the arduino script to the arduino
2. Create the python enviroment with the help of the requirements.txt
3. Start the server with: flask --app server run --host=0.0.0.0 --debugger --port 4000
4. Go to the url

Help:
The operations with the arduino will take a considerable amount of time (you can probably speed it up, I just wanted to make sure it works), every operation ending will be signaled with a led blink, if you dont have a led you can disable the function.
If you want to delete/rename a file make sure to do that with all 3 files:
  /static/images/drawings/example.pmg
  /static/binfiles/example.txt
  /static/decfiles/example.txt
If the message "An error occurred: [Errno 2] No such file or directory: '../binfiles/drawing.txt'" appears when starting the server dont worry, it is not an issue but i dont know why it appears
