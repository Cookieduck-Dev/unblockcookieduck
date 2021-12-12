# UnblockCookieduck

## Want to contribute to unblocking site cookieduck.com?

Well, now you could!

## How?

Running this script runs a server that will mirror the official cookieduduck.com, making it possible for Cookieduck to be accessible using your server's IP.
Later, your server's IP address can be forwarded to a domain and can be accessed from that domain.

## Don't have a server?
Quick setup to Heroku and Replit:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

[![Run on Repl.it](https://repl.it/badge/github/Cookieduck-Dev/unblockcookieduck)](https://repl.it/github/Cookieduck-Dev/unblockcookieduck)

> Note for Heroku: If you want to edit the main python file on Heroku, edit mainforheroku.py instead. Everything other platform should be using main.py

## Have a server?
> Ensure Python 3.8+ is installed (older versions not tested, but may work)

1. Clone repository
```
git clone https://github.com/Cookieduck-Dev/unblockcookieduck
```

2. Install dependencies
```
pip install git+https://github.com/Cookieduck-Dev/cdub
```
or
```
pip3 install git+https://github.com/Cookieduck-Dev/cdub
```

> Now, you can edit main.py to configure some settings before running it

3. Run main.py
```
python main.py
```
or
```
python3 main.py
```


## Setup a domain for your server
> Note: Server is running on port 80 by default (can be configured in main.py)
>These steps are not needed for Heroku and Replit because they come with domains

1. Buy a domain name
I recommend you buy a domain on Cloudflare because it is easy-to-use and can be easily connected with Cloudflare's DDoS Protection & Speed services.

1.5. (optional but highly recommended) Connect Cloudflare
I would definitely recommend connecting Cloudflare to your domain for free DDoS protection and to speed up your server. 
Without Cloudflare, your server can be open to DDoS attacks.
Cloudflare has instructions to setting up 

2. Point domain to server
Create an "A" record on your domain and point it to your server's IP address

## And that's it!
Your server should be up and running, displaying a page of Cookieduck's when accessed with the domain or IP.

Have any issues? Open a issue dirrectly on Github.
Know how to fix an issue? Make a pull request!

Have a great day!
-IsaacLK

