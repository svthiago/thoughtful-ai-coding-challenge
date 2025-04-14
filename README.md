# thoughtful-ai-coding-challenge
ThoughtfulAI conding challenge

## Running the script
Just execute the script as you normally would:

`python script.py`

## Implementation Rules

In order to make the labeling easier I assumed the labels as integers:

    dimensions = 1 -> not bulky
    dimensions = 2 -> bulky

    weight = 1 -> not heavy
    weight = 2 -> heavy

    dimensions + weight = 2 -> STANDARD
    dimensions + weight = 3 -> SPECIAL
    dimensions + weight > 3 -> REJECTED

I also assumed the following rules:

    if any dimension is negative or zero the package is REJECTED
    if any dimension is not int the package is REJECTED
