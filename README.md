# Doha_Internship

Knowledge based chatbot for movies made using various deep-learning modules.

# Dependencies

This code is written in python. It uses the following dependencies: 

* Scikit-learn
* NumPy
* H5Py 
* SciPy
* Theano
* NLTK v3 
* NLTK Data 

NLTK data can be installed as per written in at **http://www.nltk.org/data.html**

	$.pip install scikit-learn --user
	$.pip install numpy --user
	$.pip install h5py --user
	$.sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
	$.pip install theano --user 
	$.pip install nltk --user


# Getting started

Step 1
------ 

1.1) Download the data from this google drive link:

1.2) Unzip the data to get the Data/ folder.

1.3) Place contents from Data/src/data/ to ./src/data/

1.4) Place contents from Data/src/synopsis/ to ./src/synopsis/

1.5) Place contents from Data/src/reddit/ to ./src/reddit/

Step 2
------

Install the dependencies given before.

Voila! Chatbot is ready to kick-ass!

# Integrating the chatbot system with anything

Working of the chatbot system
------------------------------

The main chatbot script starts the chatbot. The chatbot reads the sentence from the file input-*moviename*-*reddit/synopsis*.txt and stores the nouns present in the file into nouns-query-*moviename*-*reddit/synopsis*.txt and output is written in output-*moviename*-*reddit/synopsis*.txt .

Integration with any existing system
------------------------------------

We use the interfacing script - run-*reddit/synopsis*.py stored in the src/(reddit or synopsis)/ sections. Further, we explain the workings of the script. We first import the wrapper:

	$.import wrapper-reddit as w

It contains 2 commands :- 

1) Getmovie - It is to write be given the movie name as the input. The movie name should be case-sensitive according to what is written in the list file.

2) Query - To give it a query, we type in the string of the query to this module.  Put a time wait of 2 seconds and then read the output from the output-*moviename*-*reddit/synopsis*.txt file. 

	$.import wrapper-reddit as w
	$.
	$.w.getmovie('hobbit')
	$.w.query('peter parker was a bullied a lot in the start.')


To start the system for any movie,

Step 1:

	$. bash chatbot.sh

Then you are ready for I/O!

Then follow instructions given in the bash script thereafter.

Please do kindly wait for 5-10 minutes for the libraries to initialize the engine. 

To stop the system simply exit from the bash terminal.

To run the script given by kr run this once, 

	$. g++ -std=c++11 filter.cpp

This generates the ./a.out file. 
Then, to rerank the outputs, run

	$. ./a.out nouns-query-*moviename*-*synopsis/reddit*.txt output-*moviename*-*synopsis/reddit*.txt *filecontainingcharacters*.txt input-*moviename*-*synopsis/reddit*.txt

This gives the re-ranked outputs!

# Training
# Input formats

Reddit input files should have Message<tab>Reply format and should be named out_*moviename*.tsv
Synopsis should have 1 sentence per line and should be named synout_*moviename*.txt

# Training the files

To train the system, simply go to

	$. bash train.sh

## Tested System Configurations & Constraints

This code has been throughly tested and anny benchmarks provided are from the following configuration:

* CPU: Intel i7 4790 - (8 hyperthreaded cores)
* RAM: 32 GB Kingston HyperX Fury RAM
* SSD: 128 GB SSD 
* GPU: Nvidia GeForce 970 GTX
* Vcc: CUDA v7.5
* Vcf: CuDNN v5005

This is a CPU-optimized version. In further releases, GPU optimization functionality would be added.

[*Warnings*] 

1). High Space Consumption: Please ensure you have atleast 50GB data space available on your hard-disk.

2). High RAM Consumption: RAM >= 32GB is required for running this system(Large databases are present).

# Sample testrun

	$.bash chatbot.sh 
	Welcome to ChatBot System!
	Movie selected is: Harry Potter and the Socerers Stone!
	Which system would you like to start?
	Press 1 to start Reddit based system
	Press 2 to start Synopsis based system
	$.2
	Initializing ChatBot Release1- Movie: Harry Potter Version: Synopsis
	Initializing... (Optimization might take some time, please wait)
	Enter the query:$. voldemort came back       
	Question: voldemort came back
	Reply rank #1: Dumbledore adds that Voldemort’s power apparently began to wane after his failed attempt to kill Harry and that he retreated.
	Reply rank #2: He got back in the nick of time, to save Harry from Quirrell – although at first he worried that Harry had died.
	Reply rank #3: Another centaur, Bane, comes in.
	Reply rank #4: When he comes back, he explains that Malfoy played a joke on Neville, who panicked.
	Reply rank #5: Malfoy snatches it away, but McGonagall comes by and makes him give it back.
	Reply rank #6: Although Voldemort was not destroyed, Harry’s actions have kept him from regaining power for now.
	Reply rank #7: Harry’s only interaction with his peers in Little Whinging was running away from Dudley’s gang; the school children were too afraid of Dudley to be Harry’s friend.
	Reply rank #8: Snape did hate his dad, but it was because Harry's dad saved him from death once.
	Reply rank #9: He admits he brought the troll in, and was foiled by Harry and Snape – he didn't get past Fluffy then.
	Reply rank #10: Then, Ron and Hermione fill Harry in on what happened with them: Hermione was helping Ron out to go for help and they passed by Dumbledore as he went in.
	 
	 
	Enter the query: $. 

Some more ones for fun!

	$.bash chatbot.sh 
	Welcome to ChatBot System!
	Which system would you like to start?
	Press 1 to start Reddit based system
	Press 2 to start Synopsis based system
	2
	Initializing ChatBot Release1- Movie: Harry Potter Version: Synopsis
	Initializing... (Optimization might take some time, please wait)
	
	Question: the plot of deathly hallows was flawed
	Reply rank #1: This knowledge of Voldemort and the curse that killed his parents will become a crucial aspect of Harry’s character and a large part of his determination to face Voldemort later in the book.
	Reply rank #2: Although Rowling does not describe the Dursleys in truly malevolent terms – as she will later with Voldemort – their closed-mindedness and insistence on appearing “normal” are all expressed as negative characteristics.
	Reply rank #3: There is no question of the evil of the mysterious hooded figure since only the most depraved dark wizard would be willing to murder a pure unicorn for the sake of its blood.
	Reply rank #4: In classic literary tradition, the hero of such a narrative would have remarkable powers and skills.
	Reply rank #5: Dumbledore explains that the Mirror of Erised reveals the deepest desires of a person’s heart but cannot give truth or knowledge.
	Reply rank #6: Because of Harry’s fame in the wizarding world for removing Voldemort from power, there was the possibility that he would become egocentric and arrogant as a wizard and as a man.
	Reply rank #7: This one fulfilled desire serves as the catalyst to the events that unfold during the rest of the book.
	Reply rank #8: Their neglect and cruelty toward him was not simply personal hatred for him, but rather hatred for his parents and what their life represented.
	Reply rank #9: Nicolas Flamel and Dumbledore had decided to destroy the Stone to ensure that it could never be used by a dark wizard.
	Reply rank #10: The caricatured aspect of the characters thus helps us read the story as a myth.

	Question: harry can speak parseltongue. why is it
	Reply rank #1: Maybe its because Im a fan but I believe deep down hes a good guy Throughout his life Lily brought the good out in him If it werent for her if it werent for her death I think he certainly would have stayed a Death Eater.
	Reply rank #2: Mcgonaggal says that aurors have to complete at least three more years of training and Im sure other.
	Reply rank #3: I was sort of surprised too Then I remembered that Bill is supposed to be smokin hot and can pull Fleur so it sort of made sense then.
	Reply rank #4: 29 POINTS TO GRYFFINDOR.
	Reply rank #5: Krister Henriksson the guy who reads Harry Potter for audio books in Swedish is apeshit nuts I tell you I sometimes fell asleep but after seconds I woke up to his hysterical shouting and exaggeration for effect all the time.
	Reply rank #6: Ships which are.
	Reply rank #7: No it wasnt that is why there is a malformed voldemort in purgatoryhe killed his soul when he attacked harry.
	Reply rank #8: and of course check out the rest of rHPfanfiction .
	Reply rank #9: Yes So much power in that quote.
	Reply rank #10: Oh man hed be awesome too.