# polis-loadtesting
A single, simple Locust test to meaningfully load-test Pol.is instances

Server-specific configuration is done through .env files - copy .env.template to .env, make the necessary changes for your system, and run `source ./.env` from the project directory to set these.

To run the tests, `pip install locustio`, then `locust -f locustfile.py --host=$LOCUST_TARGET`. You can then send creatures at your server through the web interface at http://localhost:8089
