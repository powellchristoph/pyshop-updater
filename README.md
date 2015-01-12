PyShop Updater
===================

This will go through all of the packages on your PyShop server and force them to validate their cache.
We use this to ensure that new packages are mirrored on the server to reduce installation time for our users.

Instructions
==================

Enter your PyShop information into the sites.ini file. You can have muliple sites, each in its own block.

    [your-site-goes-here]
    url = http://your-site-url/simple
    user = user-for-your-site
    pass = password-for-user

Ensure you have installed the requirements.

    pip install -r requirements.txt

Usage Instructions:

execution format:

    python pyshop-updater.py sites.ini

Schedule
==================

Create a crontab entry to run the script at scheduled intervals.

    mkdir ~/bin && cd ~/bin
    git clone https://github.com/powellchristoph/pyshop-updater.git
    pip install -r requirements.txt

Edit the sites.ini with your information

Edit /etc/crontab

    @daily root /path/to/bin/pyshop-updater.py /path/to/bin/sites.ini > /dev/null

