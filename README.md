# AGI Assistant
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#structure)
- [References](#references)

## Installation
The frontend is currently written in [Python 3.11](https://docs.python.org/3/) using the [Streamlit](https://docs.streamlit.io/library/cheatsheet) library.

### Requirements
Python >= 3.10 (Might also work on a lower version not sure) <br>
```pip install -r requirements.txt```

## Usage
Streamlit should handle everything for you so just navigate to the folder where the main is located <br>
and use ```streamlit run main.py``` to start the application. <br>

Don’t forget to set up the .env file! <br>

If you’re writing any code, please stick to [PEP 8](https://peps.python.org/pep-0008/) or otherwise this will become an even bigger mess…

## Structure
### AGI-Assistant-Backend
This repository handles the data traffic and connects all the different components. <br>
### AGI-Assistant-Frontend
This repository holds everything required to run the frontend of the application. <br>
### AGI-Assistant-Model
This repository holds everything required to run the machine learning model. <br>

## References
### Repositories
Backend:   https://github.com/Knaeckebrothero/AGI-Assistant-Backend <br>
Frontend:  https://github.com/Knaeckebrothero/AGI-Assistant-Frontend <br>
Model:     https://github.com/Knaeckebrothero/AGI-Assistant-Model <br>

### Lucidchart
https://lucid.app/documents#/documents?folder_id=336580960 <br>
