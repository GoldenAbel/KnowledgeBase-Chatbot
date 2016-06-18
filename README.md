# Doha_Internship

Knowledge based chatbot for movies made using various deep-learning modules.

# Dependencies

This code is written in python. It uses the following dependencies: 

* Scikit-learn: pip install scikit-learn --user
* NumPy       :	$.pip install numpy --user
* H5Py        :	$.pip install h5py --user
* SciPy       :	$.sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
* Theano      :	$.pip install theano --user 
* NLTK v3     :	$.pip install nltk --user
* NLTK Data   :	As per written in at **http://www.nltk.org/data.html**

# System Requirements

This is a CPU-optimized version. If further required, GPU optimization functionality would be added.

[*Warning*] This consumes a lot of RAM space. RAM >= 32GB is recommended for running this system due to the large databases present.

[*warning*] This consumes high amount of disk space too. Please ensure you have atleast 50GB data space available on your hard-disk.

# Getting started

Step 1) 
1.1) Download the data from this google drive link:

1.2) Unzip the data to get the Data/ folder.

1.3) Place contents from Data/src/code/ to ./src/code

1.4) Place contents from Data/src/data/ to ./src/data

Step 2) Install the dependencies given before.

Voila! Chatbot is ready to kick-ass!

# Running the chatbot system

	$.bash chatbot.sh

Then follow instructions given in the bash script thereafter.

Please do kindly wait for 5-10 minutes for the libraries to initialize the engine. 

To stop the system simply exit from the bash terminal.

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
	
etc.
