# Headers
## Overview
Headers is a full-stack web application that collects and displays information about a visitor’s IP address, geolocation, and device. It is hosted on a Raspberry Pi and exposed securely to the internet via a Cloudflare Tunnel, accessible at headers.pettifor.tech

The system captures and processes request headers from users, enriches them with geolocation data (using the free ipinfo.io api (while it is available)), abstracts user agent details into categories (device, OS, browser), and displays this information back to the user through a simple web interface.

Further plans are to store simple user information (country, browser, and visit time) as well as a small dashboard displaying this information (users by country / browser in the last 90 days). User data will stay in the database for only 90 days.

