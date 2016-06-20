echo 'Welcome to ChatBot System!'
echo 'Which system would you like to start?'
echo 'Press 1 to start Reddit based system'
echo 'Press 2 to start Synopsis based system'

read vari
case $vari in
  1|Reddit) cd src/reddit/; python file2.pyc ;;
  2|Synopsis) cd src/synopsis/; python file2.pyc ;;
  *) echo 'Incorrect input!';;
esac
cd ../../
