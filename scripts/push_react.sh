ssh -i $1 ubuntu@54.144.233.30 "cd /var/www/ods/html; sudo rm -rf *"
scp -i $1 -r ./frontend/build/* ubuntu@54.144.233.30:/var/www/ods/html
