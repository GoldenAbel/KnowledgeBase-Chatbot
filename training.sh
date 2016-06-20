cd src/training/
echo 'Which system would you like to start?'
echo 'Press 1 to start Reddit based system'
echo 'Press 2 to start Synopsis based system'

read vari
case $vari in
  1|Reddit) python train_reddit.pyc ;;
  2|Synopsis) python train_synopsis.pyc ;;
  *) echo 'Incorrect input!';;
esac
cd ../../