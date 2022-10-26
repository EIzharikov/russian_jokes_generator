# Russian Jokes Generator

## Description
This project is part of the compulsory course Programming for Linguists in 
National Research University Higher School of Economics. It is a joke generator, that is a special case of text generation.
```
Input: a collection of jokes.  
Output: generated text based on the input collection.
```
The program is trained on two models, which are based on the same architecture — RuGPT3. 
Before starting generation it is possible to select a model, a topic of jokes (if it is a ‘Наша’ model) 
and the length of the generated text. Besides, you need to enter a prompt for a joke 
and the program will continue the text.

### Creators

**Team-lead / NLP-engineer**: Polina Savinova  
**Logic and Interface developer**: Egor Zharikov  
**QA / Tech Writer**: Vita Zaytseva  
**Developer**: Evgenia Pareshina

___

## Installing

To install the program you need to open Git on your computer and write the command:
```
git clone https://github.com/posavinova/russian_jokes_generator.git
```
___

## Focal points
### Contents
The generator consists of the following folders:
1. `models_config`  
   

   Two models are stored here. Both are based on the same architecture — RuGPT3. 
   The difference between them is fine-tuning on different datasets.
   Our model was fine-tuned on a collection of texts from [humornet.ru](https://humornet.ru).
   As for the other model, we are giving credits to [Neural Shit](https://t.me/NeuralShit).
   

2. `spider`
   

   Here you can find scraper for collecting dataset from the site [humornet.ru](https://humornet.ru)


3. `src`
   

   It is the folder where the GUI, the model request and the saving the history of jokes are stored.
   

4. `tests` 
   

   Here you can find unit tests on models.

### Technical solutions

| Module                                                       | Description                                        | Component |
|:-------------------------------------------------------------|:---------------------------------------------------|:----------|
| [`pathlib`](https://pypi.org/project/pathlib/)               | module for working with file paths                 |           |
| [`pylint`](https://pypi.org/project/pylint/)                 | module for code analyser                           |           |
| [`gdown`](https://pypi.org/project/gdown/)                   | module for downloading big files from Google Drive | models    |
| [`torch`](https://pypi.org/project/torch/)                   | module for machine learning                        | models    |
| [`transformers`](https://pypi.org/project/transformers/)     | module for downloading and training models         | models    |
| [`BeautifulSoup4`](https://pypi.org/project/beautifulsoup4/) | module for finding information on web pages        | scraper   |
| [`pandas`](https://pypi.org/project/pandas/)                 | module for working with tabular data               | scraper   |
| [`requests`](https://pypi.org/project/requests/)             | module for downloading web pages                   | scraper   |
| [`tqdm`](https://pypi.org/project/tqdm/)                     | module for tracking progress                       | scraper   |

___

## Running
### Program launch
To run the generator you need to open the file `main.py` in the folder `src` and run the method.
```python
if __name__ == '__main__':
    app = Application()
    app.run
```

### Interface
When you start the generator, the Joke Generator front-end application will open. 
At the bottom you can see drop-down lists where you can choose `model`, `length` and `tag` (if it is a "Наша" model). 
To get the generated joke, you need to enter a prompt for a joke in the field, select all categories and 
click on Submit or press Enter. Then your prompt and the generated joke will appear.


### Saving
Our program has an automatic function of saving jokes locally. 
When you run the generator for the first time, the file `jokes_history.txt` is created, 
where you can see all the generated jokes.
