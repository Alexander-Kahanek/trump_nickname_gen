# Trump Nickname AI generator

This will be a project to generate and nicknames based on a given real name, using a model trained on Trump's used nicknames.

data: https://en.wikipedia.org/wiki/List_of_nicknames_used_by_Donald_Trump

# Python Notebooks

These notebooks were created as a walkthrough of the whole process taken from the inital data analysis, to the end product of a working model.

+ 1_intial_analysis.ipynb
  - This notebook contains the original analysis that was done on the dataset before it was used to train the LSTM Neural Network.

+ 2_character.nn.gen.ipynb
  - This notebook was the first attempt at training the model, using a character based approach.
  - This character based approach did not have goo results, and thus a word based model was created.

+ 3_word.nn.gen.ipynb
  - This notebook is the creation of the word based approach to nickname generation.
  - This model had much better results, especially when utilizing the affix information of the nicknames.


# PROJECT UNDER DEVELOPMENT

Working on displaying the Phoenix / Elixir Web Application that was created to implement the model displayed in the 3_word.nn.gen.ipynb analysis
