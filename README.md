# Headers
## Overview
Headers is a full-stack web application that collects and displays information about a visitor’s IP address, geolocation, and device. It is hosted on a Raspberry Pi and exposed securely to the internet via a Cloudflare Tunnel, accessible at headers.pettifor.tech 

The system captures and processes request headers from users, enriches them with geolocation data (using the free ipinfo.io api (while it is available)), abstracts user agent details into categories (device, OS, browser), and displays this information back to the user through a simple web interface.

Further plans are to store simple user information (country, browser, and visit time) as well as a small dashboard displaying this information (users by country / browser in the last 90 days). User data will stay in the database for only 90 days.

## Architecture
The application is composed of several services in Docker containers

### Collector
**Flask** app that receives incoming requests, extracting the raw request headers and forwarding them to the processor service, displaying the response (future plans are to pass this information to the front-end)

### Processor
Another **Flask** app that enriches the IP data with the ipinfo.io API, gets more country information using *pycountry* and (will eventually) abstract user agents with *user-agents*. This app will also communicate with an externally hosted **PostgreSQL** database to store non-identifiable user data for use in the planned dashboard microservice

### Frontend (planned)
Lightweight web UI that will display information handled by the other apps, details on what information is publicly visible to any website the user visits.

#### Dashboard (planned)
Display a simple graph using data from the **PostgreSQL** database

### Infrastructure
Deployed on a Raspberry Pi using Docker & Docker Compose
Exposed securely via a Cloudflare Tunnel to avoid direct access