# Information
* This document is written for bash terminal.

* This project is planned to work on a Raspberry Pi. 

* This Raspberry Pi system designed for receiving and displaying messages on its screen. Messages can be sent from any device that can connect to the website.

* PHP website will be hosted by a Raspberry Pi.

* Python program is designed for being displayed on a Raspberry Pi screen.

# Configuring Server Side
* Before everything,
    ```
    $ sudo apt update
    ```

* You should install these on your device where you will host website. For my case this is a Raspberry Pi.
    ```
    $ sudo apt install php-common php-cli php-fpm
    $ sudo apt install nginx
    ```

* Now you should enable PHP for nginx. Go for this file:
    ```
    $ sudo nano /etc/nginx/sites-available/default
    ```

* Check where your root file is and add index.php next to ```index```, right below your root file declaration. You should have something like this:
    ```
    root   /var/www/html;
    index  index.php index.html index.htm;
    ```
* Root path may be different on your file. That line shows where you need to put your source code. Edit or leave as you wish.

* Edit your location function as this (you can edit the port as you wish):
    ```
    location ~ \.php$ {
       fastcgi_pass 127.0.0.1:7777;
       fastcgi_index  index.php;
       fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
       fastcgi_buffers 256 128k;
       fastcgi_connect_timeout 300s;
       fastcgi_send_timeout 300s;
       fastcgi_read_timeout 300s;
       include fastcgi_params;
    }
    ```

* Now you need to make sure PHP-fpm is listening to right port. Go to:
    ```
    sudo nano /etc/php/7.4/fpm/pool.d/www.conf
    ```

* Be carefull here, the file ```7.4``` may be different according to installed PHP version. Use ```$ php --version``` to learn your PHP version. If this doesn't work, you may have forgotten to install ```php-cli```, or there may be a problem with its operation. Also this path may change in the future. If you are having problems related to finding ```www.conf``` file, I recommend you to go directory by directory for finding the file.

* Now in this file, you need to find the line which contains ```listen```. Edit the line as you have written in your nginx configuration file.
    ```
    listen 127.0.0.1:7777;
    ```

* For not experiencing any kind of problems, restart the services:
    ```
    $ sudo service nginx restart
    $ sudo service php7.4-fpm restart
    ```

* You should put the ```index.php``` and ```depo.txt``` in the root directory. (Which was /var/www/html for my case.)

* In addition, you need to matk ```depo.txt``` as readable and writable. So the web service can write messages into this text file.
    ```
    $ chmode 777 depo.txt
    ```

### Tor Implementation
* If you don't want to use tor network to host your web service, you can skip this part.
* For downloading ```Tor``` on your Linux machine:
    ```
    $ sudo apt install tor
    ```

* For editing the configuration file of ```Tor```:
    ```
    $ sudo nano /etc/tor/torrc
    ```

* Search for these two lines, and uncomment them:
    ```
    HiddenServiceDir /var/lib/tor/hidden_service/
    HiddenServicePort 80 127.0.0.1:80
    ```

* Restart the Tor service:
    ```
    $ sudo service tor restart
    ```

* Now you are all set! For getting your .onion URL, go for:
    ```
    sudo cat /var/lib/tor/hidden_service/hostname
    ```
* If the ```HiddenServiceDir``` path is different on your config file, you should use the path written on your config file instead.

# Extra Required Stuff
* For testing your PHP file on a test server, 
    ```
    $ php -S localhost:8000
    ```
* Then, go to ```localhost:8000/main.php``` on any web browser.

* For installing Python3:
    ```
    $ sudo apt install python3
    ```

* For installing pip:
    ```
    $ sudo apt install pip
    ```

* Tkinter used for GUI. For installing it:
    ```
    $ sudo pip install tkinter
    ```
