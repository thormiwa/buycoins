# Buycoins Engineering Project
This is the solution for the Buycoins engineering challenge
## Pure Levenshtein Distance algorithm vs Damerau–Levenshtein Distance algorithm
The Pure Levenshtein computes the distance taking three possible ways into account, insertions, deletions or substitutions, of single characters.
For example it calculates the distance between two strings "moth" and "mother", The distance between those strings is 2, the Pure Levenshtein allows us to add "th" to make those strings equal and i understand it helps us solve the problem of when users accidentally miss a letter or two due to human error.

Damerau–Levenshtein Distance algorithm does the same thing but it goes further to add a fourth way, the ability to account for transposition of two adjacent characters, as a possible step. for example the edit distance between two strings "a cat" and "an abct" is 4, using the Damerau–Levenshtein we can add and transpose/swap some characters in those strings to make them equal.

Getting started
---------------

First you'll need to get the source of the project. Do this by cloning the
whole buycoins repository:

```bash
# Get the example project code
git clone https://github.com/thormiwa/buycoins.git
cd buycoins
```

It is good (but not required) to create a virtual environment
for this project. We'll do this using
[virtualenv] to keep things simple.

```bash
# Create a virtualenv in which we can install the dependencies
virtualenv env
source env/bin/activate
```

Now we can install the dependencies:

```bash
pip3 install -r requirements.txt
```

Now setup our database:

```bash
# Setup the database
python3 manage.py migrate

# Create an admin user (useful for logging into the admin UI
# at http://127.0.0.1:8000/admin)
python3 manage.py createsuperuser
```

Now you should be ready to start the server:

```bash
python3 manage.py runserver
```

Now go to 
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql) on your browser
and run some queries!
