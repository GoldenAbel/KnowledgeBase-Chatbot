echo 'Welcome to ChatBot System!'
echo 'Movie selected is: Harry Potter and the Socerers Stone!'
echo 'Which system would you like to start?'
echo 'Press 1 to start Reddit based system'
echo 'Press 2 to start Synopsis based system'
cd src/code/
read vari
case $vari in
  1|Reddit) python system_reddit.pyc ;;
  2|Synopsis) python system_synopsis.pyc ;;
  *) echo 'Incorrect input!';;
esac
cd ../../
