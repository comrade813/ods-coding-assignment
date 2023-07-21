# Solution

## Summary
I created a React/Typescript/Flask/PostgreSQL webapp running on a Ubuntu 22.04 server, hosted by Nginx. \
The server was created on AWS Lightsail, which also allowed me to give it a static public IP.

## Technical Decisions

### Why are some fields excluded?
Fields such as id, flight id number, and the last updated time are not useful for users to know.

### Why both to and from?
It seemed like the most intuitive for users -- most airline websites are built this way.

### Why use environment variables?
Environment variables mask sensitive information, such as passwords, usernames, and IP addresses. \
They can also be used to easily differentiate hardcoded values between development and production environments.

### Why is there another "airports" table?
The number of airports is much, much more static than the number of flights. \
It would be incredibly inefficient to parse the list of unique airports from the list of flights every single time a user entered the webpage. \
Therefore, I created a script backend/load_airports.py (that could be run as a daily Lambda function, or set on a database trigger) to calculate the list of unique airports. \
When the user first enters the page, this list is loaded from the airports table.

## Setup

### Local Machine (Macbook Pro)

#### Github
git clone https://github.com/comrade813/ods-coding-assignment.git

#### NPM, NodeJS, and React
// I already had this installed, but you can use the Node Version Manager (nvm). \
cd ods-coding-assignment \
npx create-react-app frontend --template typescript \
npm i --save react-select \
npm i --save axios \

#### Flask
I already had all the Flask packages installed locally.

#### PostgreSQL
Open pgAdmin \
Create database "ods" \
Create schema "flight_data" \
Create table "flights" with appropriate columns (see SQL script)

### AWS
// Website hosted on a cheap Linux server \
Create the most basic Ubuntu 22.04 server instance on AWS Lightsail. \
Cost: $3.50/month

#### Nginx
// Web server
sudo apt update \
sudo apt install nginx \
sudo ufw allow 22 \
sudo ufw allow 'Nginx HTTP' \
sudo ufw enable \
sudo mkdir /var/www/ods/html \
sudo chmod 777 /var/www/ods/html \

sudo nano /etc/nginx/sites-available/default \
// change line "root /var/www/html" to "root /var/www/ods/html" \
// add in a couple lines to reverse-proxy, allowing HTTP requests to reach the Flask endpoints \
sudo systemctl restart nginx

#### PostgreSQL
sudo apt install postgresql \
// allow PostgreSQL port in AWS Lightsail firewall \
On your local machine, back up the ods database as plaintext \
SCP it over to the AWS server with the script \
sudo psql -U postgres -h 127.0.0.1 -f ~/SQL/backup.sql \

#### Flask
sudo apt install python3-pip \
sudo apt install python3-flask \
pip install Flask \
pip install flask-cors \
pip install python-dotenv \
pip install psycopg2-binary \
// fill out the necessary fields in the environment dotenv files

## Run

### Flask
// make sure that the .flaskenv and .env files are filled out correctly \
cd backend \
nohup flask run & \

### Build React App and Deploy to Web Server
npm run build \
./scripts/push_react.sh

# Future Considerations

## Unit Testing
Use Jest for the frontend and Python's unittest for the backend.

## HTTPS Authentication
Given a domain name, I could use LetsEncrypt to get a free HTTPS certificate. \
For this project, I don't want to pay for a domain name.
