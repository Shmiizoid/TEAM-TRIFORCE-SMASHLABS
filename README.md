# SmashLabs 
The Ultimate Super Smash Bros. Companion. Our app optimizes the SQL database for efficient storage of fighter details. Extensive testing guarantees accessibility and visual appeal. Enjoy an intuitive interface that offers seamless exploration of fighters, emphasizing usability and readability with elegant formatting and typography. Unleash your creativity with the ability to create, edit, and delete custom fighters and stages. SmashLabs fosters a collaborative environment for players to share their content and ideas, with potential inclusion in future game updates. Elevate your Super Smash Bros. experience with SmashLabs today!

**Screenshot of app**
![sitecapture](./main_app/static/images/smashlabs.png)

# Technologies Used
The following technologies were utilized in the development of SmashLabs:

- NeonDB: Our app's backbone is built on NeonDB, a robust SQL database that efficiently stores and manages all fighter details, ensuring lightning-fast performance.
- Django: The flexible and minimalistic web application framework for Node.js, Django, empowers SmashLabs with the ability to create a highly customizable and responsive user interface.
- Python3: The server-side code execution is handled by Python3, enabling dynamic and efficient handling of various operations within the app.
- Icons8: To enhance the application's visual appeal, we've integrated the Icons8 library, providing a wide array of stunning icons for a more engaging user experience.
- Visual Studio Code: Our developers rely on the powerful Integrated Development Environment (IDE), Visual Studio Code, to craft clean and efficient code, ensuring the app runs smoothly.
- Heroku: For seamless deployment and hosting of the app, SmashLabs leverages Heroku, a trusted cloud platform, guaranteeing that users can access the app anytime, anywhere.

 ## PIP installs: 
- asgiref==3.7.2
- certifi==2023.5.7
- charset-normalizer==3.2.0
- dj-database-url==2.0.0
- Django==4.2.3
- django-on-heroku==1.1.2
- gunicorn==21.2.0
- idna==3.4
- packaging==23.1
- psycopg2-binary==2.9.6
- requests==2.31.0
- sqlparse==0.4.4
- typing_extensions==4.7.1
- urllib3==2.0.4
- whitenoise==6.5.0



# Installation Instructions

**Setting up a virtual environment called .env:**
```bash
python3 -m venv .env
```

**Activating a virtual environment called .env:**
```bash
source .env/bin/activate
```

**Deactivating a virtual environment:**
```bash
deactivate
```

<ol>
<li>Clone the repository by running:
<pre><code>git clone https://github.com/Shmiizoid/TEAM-TRIFORCE-SMASHLABS.git</code></pre>
</li>
<li>Navigate to the project directory:
<pre><code>cd TEAM-TRIFORCE-SMASHLABS </code></pre>
</li>
<li>Install all dependencies:
<pre><code>pip install -r requirements.txt
</code></pre>
</li>
<li>Activate environment:
<pre><code>source .env/bin/activate</code></pre>
</li>
<li>Start the application by running:
<pre><code>python3 manage.py runserver</code></pre>
</li>
<li>Open your browser and visit `http://localhost:8000` to access the application locally.</li>
<li>Visit <a href="https://smashlabs-69ccb3a7e5a4.herokuapp.com/"> Live Site</a> Instead !</li>
</ol>

# User Stories

- **New/Intermediate Player:** Access detailed character guides for informed character selection.

- **Pro Player:** Research opponents' playstyles, strengths, and weaknesses for strategic improvement.

- **Tournament Moderator:** Look at compatible stages for each character to ensure fair gameplay.

- **Commentator:** Familiarize myself with move lists for enhanced commentary and viewer experience.





# Major Hurdles:

1. Implementing APIs and loading images on our site proved to be a significant challenge.

2. Attempting to incorporate a CSS framework resulted in conflicting CSS codes, making it unachievable.

3. Django Forms didn't offer the level of customization we initially anticipated.

4. App responsiveness was not our strong point, requiring further improvement.

5. Setting up the card display was challenging, involving numerous container divs and classes.


# Unsolved Problems



1. The API is not 100% functional with images not being able to load when the cache is cleared. Images do load 1-5 mins after.

2. The responsiveness is not 100% but we still got most of it working.



# Wireframes/ERD/Route Table

https://miro.com/app/board/uXjVM2jNhaY=/

