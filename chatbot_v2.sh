echo 'Welcome to ChatBot System!'
echo 'Which system would you like to start?'
echo 'Press 1 to start Reddit based system'
echo 'Press 2 to start Synopsis based system'
cd src/code_v2/
read vari
case $vari in
  1|Reddit) python fullsystem_reddit.pyc ;;
  2|Synopsis) cd ../code/; python system_synopsis.pyc ;;
  *) echo 'Incorrect input!';;
esac
cd ../../
