# Learning gpt-2-simple

The gpt-2-simple repository was extremely useful in helping me get hands on experience with GPT-2.

After forking the repository I wanted to build out and capture how I learned and some examples of using GPT-2. 
That's what this document captures.

I've focused on the language generation features of GPT-2. 
This works by feeding in some starter text (e.g. a sentence or two) into the model, and it will then produce more sentences based on that start. 

There's a lot more you can do with GPT-2, but that's not covered here (yet).

Lastly, before jumping in, I'll make it clear that I don't go into a lot of detail explaining virtual environments here.
Checkout my `roywilds/howto` repository for help there, or search for the many many online tutorials that walk through using Python virtual environments.


# Getting gpt-2-simple
I was experimenting with gpt-2-simple in the summer of 2020.

Turns out that the approach they take with gpt-2 requires old Tensorflow (1.15) which only works with at most Python3.6
My Ubuntu 20.04 only has Python3.8 by default. Here's the steps I followed:

```bash
# Start by adding required repo and updating so we can install Python3.6
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update

# Install python 3.6 and venv
$ sudo apt-get install python3.6
$ sudo apt-get install python3.6-venv

# Create a venv. I store mine in ~/.virtualenvs/
$ python3.6 -m venv ~/.virtualenvs/gpt2

# Activate it and upgrade pip
$ source ~/.virtualenvs/gpt2/bin/activate
$ pip install --upgrade pip

# Install the gpt-2-simple dependencies. If using my fork, then you'll get additional packages we'll need later on
$ cd gpt-2-simple
$ pip install -r requirements.txt 

# Install gpt-2-simple
$ pip install gpt-2-simple

# Verify
$ python
> import gpt_2_simple as gpt2
```
You should see `Python 3.6.X` (`X` may vary) for the Python version, and then the import step will likely spit out a WARNING about tensorflow.
You're now set to proceed.

Note: For those not familiar with virtualenvs, just type in `deactivate` in your shell and you'll be back to your default Python installation, with none of these packages installed.
You must be in this virtualenv (via `source ~/.virtualenvs/gpt2/bin/activate`) to use gpt-2-simple.

# Data
Now that we have `gpt-2-simple` installed, let's talk about data to fine tune our models.

What is fine tuning? 

The GPT-2 model is itself a complete language model. You don't need to fine tune it. 
However, fine tuning is a great way to produce specific language that you want. 

For example, with the `shakespeare` corpus included in `gpt-2-simple`, once you fine tune the model then when you feed in a starter sentence, you'll get language generated that makes sense in the context of the `shakespeare` corpus.

The `shakespeare` corpus included with gpt-2-simple was handy, but did not fine tune the base models in a way that I wanted. 
I was looking to use more contemporary content. 

## Medium
Medium has ample amounts of content, and fortunately a lot of folks have spent time either collecting and curating it, or providing code and tools to do just that.
Web scraping isn't my forte, but fortunately I came across https://www.kaggle.com/hsankesara/medium-articles, which suited my initial purposes.
Check out the link to grab the dataset.

## Podcast Transcripts
A really great resource for text to fine tune are readily available transcripts. 

# Generating Content
See the various notebooks in `notebooks/` to see how you can use 

Steps
1. Launch Jupyter Notebook via `jupyter notebook` (you'll need your virtualenv active)
2. It should automatically redirect you to your browser, but if needed, open a new tab and go to `localhost:8888/tree`
3. Navigate into `notebooks/` and select a notebook. Try `Demo.ipynb` to get started.

## Introduction
Start with `notebooks/Demo.ipynb`

This uses the "small" 124 million parameter GPT-2 model as a starting point. 
We train it on a small document that consists of sentences describing GPT-2 and GPT-3.

From this trained model, we get it to generate a few sentences given the starting sentence

```
What can we do with our GPT-2 model now?
```

Here's one example that was produced

> The GPT-2 language model was first announced in February 2019, with only limited demonstrative versions initially released to the public. The full version of GPT-2 was not immediately released out of concern over potential misuse, including applications for writing fake news. Some experts expressed skepticism that GPT-2 posed a significant threat. The Allen Institute for Artificial Intelligence responded to GPT-2 with a tool to detect "neural fake news".

The quality of the generated text can vary a lot. And this Demo uses a very minimal training period, intended to show functionality, not performance.

## TBD