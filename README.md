# GAI News Curator

## Dev Installation

Create a virtual environment as desired, and then:

```commandline
git clone git@github.com:GAI-News/news-curator.git as goodnews && cd goodnews
pip install -r requirements.xt
```

## Samples

You should be able to run the newscollector sample with:

```commandline
python curator/samples/newscollector_simple.py
```

Running the GPT sample requires you place an OpenAI key in your [config.ini](curator/config/config.ini) file. And then:

```commandline
python curator/samples/gpt_simple.py
```

Running the Bart sample requires you place a Huggingface key in you [config.ini](curator/config/config.ini) file, 
as well as install all the local dependencies:

```commandline
pip install -r local_requirements.txt
python curator/samples/bart_simple.py
```
