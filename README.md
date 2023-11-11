# Connect-A-Ton

Connect-A-Ton ( CAT ) was a fun game platform created as part of [Make-A-Ton](https://makeaton.in) one of south India's largest yearly hackathon. I then decided to release CAT as an independent product after the huge popularity it received during the hackathon. So for all you guys who wanted to use CAT for your own events, here you go.

## Installation

CAT is created entirely using Django and it comes as a batteries included package. In essence, you need only this repo to get setup and running. CAT uses Postgres as it's primary database, but don't  worry you don't have to install and configure postgres as there is a docker-compose included that will take care of setting up the DB with required users and other configs.

### Steps

1) Clone this repo
    ```bash
    git clone https://github.com/rohittp0/connect_a_ton.git
    ```
2) Create a venv and activate it
    - Linux / MacOs
    ```bash
   python3 -m venv venv
   ./venv/bin/activate
   ```
   - Windows
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```
3) Install dependencies
    ```bash
   pip install -r requirements.txt
    ```
4) Rename the .env.example to .env and edit the values in it
5) Set up the database
    ```bash
   docker-compose up -d
    ```
6) Apply migrations
    ```bash
   python manage.py migrate
   ```
7) Enable sign in with Google ( currently only Google auth is supported 
    ```bash
    python manage.py createsocial
    ```
8) Create an admin user account
    ```bash
   python manage.py createsuperuser
   ```
   
That's it, now you should be able to start CAT by running,
```bash
python manage.py runserver
```

Open http://localhost:8000 in your browser

## Configuration

CAT is fully customisable and at the same time starts working right out the box. The main settings you would want to play around with is,

### Preregistration

If you are using CAT as part of some event ( e.g. Hackathon ) you might want to limit CAT to be accessible to a set of registered users only. In this case you can enable checkin feature of CAT by changing `PRE_REGISTRATION=True` in `connect_a_ton/settings.py`. Enabling this will restrict CAT access to preregistered users only. 

When enabled you should provide a JSON file containing preregistration data. Create a `registration_data.json` file in the root folder. The structure of this JSON should be:

```json
{
  "email": {
    "name": "User's name",
    "course": "Course currently attending if applicable",
    "college": "College if applicable",
    "github": "github id/url",
    "tshirt": "xs | s | m | l | xl | xxl",
    "year_of_study": "4",
    "phone": "123456789",
    "food": "veg|non-veg",
    "linkedin": "linkedin url",
    "gender": "male|female",
    "email": "same as above",
    "team": "team name if applicable"
  }
}
```

### Swags

CAT can be used to distribute swags/prices if you decide. There is inbuilt support for adding swags with corresponding points so that when ever any of the users accumulate the given points the swag gets automatically unlocked. You can use the Django Admin to add swags and also keep track of who unlocked what their delivery status. Swags can also be manually awarded irrespective of the points using the adin panel as well.

To enable this feature change `SWAGS = True` in `connect_a_ton/settings.py`. Once enabled you should apply migrations once again to create the required DB tables.

### Questions

CAT doesn't include any questions by default. You have to add questions you like to be asked using the admin panel. In the admin panel questions can be added by going to questions tab and entering the question and corresponding options.

When adding question you can use `%USER%` special syntax to refer to current user. That is,
```text
According to %USER% what is the best FOSS project?
```

will be rendered as,

```text
According to Rohit what is the best FOSS project 

or

According to you what is the best FOSS project
```

> Note: The options for a specific question should be entered as a string of comma seperated values.

## Questions and Feedback
If you are facing any problem feel free to open an issue or mail me a stack overflow question with connect-a-ton as the tag. All pull requests are always welcome.

## Contact Me

**Mail me @**  [tprohit9@gmail.com](mailto:tprohit9@gmail.com)

**Catch me on**  [Stackoverflow](https://stackoverflow.com/users/10182024/rohi)

**Check out my YouTube**  [Channel](https://www.youtube.com/channel/UCVRdZwluF8jYXSIaHBqK73w)

**Follow me on**  [Instagram](https://www.instagram.com/rohit_pnr/)