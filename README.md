# Python RTI Example

[![codecov](https://codecov.io/gh/codecov/impact-analysis-example-python/branch/main/graph/badge.svg)](https://codecov.io/gh/codecov/impact-analysis-example-python)

This repository demonstrating how to use Codecov's [Impact Analysis](https://about.codecov.io/product/feature/impact-analysis/) feature with python. It runs with the [Flask](https://flask.palletsprojects.com/en/2.1.x/) framework and leverages the [codecov/opentelem-python](https://github.com/codecov/opentelem-python) package to send information to Codecov's Runtime Insights API.

This repository is set up to do to be used as
1. a working sandbox to explore Impact Analysis
1. a reference for adding Impact Analysis to your own repositories

## Getting Started

The following section details how to get started with Impact Analysis. Before getting started, you will need
1. `python` version 3+
2. An account on [Codecov](https://about.codecov.com)

<br />

**Step 1: Fork and clone this repository**
-------------

[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) this repository from GitHub. It is strongly recommended that you fork the repository to your personal GitHub account.
Clone your new repository to your local machine.

<br />

**Step 2: Set the `profiling token`**
-------------

Go to [Codecov](https://app.codecov.io/gh) and find the fork in the list of repositories. Note that it may be under `Not yet setup` in the right-hand section.

In the `settings` page, grab the `Impact analysis token`, and set the token locally in a terminal.
```
export CODECOV_OPENTELEMETRY_TOKEN='***'
```

<br />

**Step 3: Install the dependencies**
-------------

Install all dependencies for this project. It is highly recommended to do this in a virtual environment.
```
pip install -r requirements.txt
```

<br />

**Step 4: Run the server locally and generate profiling data**
-------------

Run the server from your machine using the command
```
python example-app/app.py
```
If the token has been set properly, you should see the server running with the following logs
```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.1.184:8080 (Press CTRL+C to quit)
```

You can view the app by going to `http://127.0.0.1:8080`.
The app has two pages, the main page that has a button to `Get the time`, while the other page displays the time.

<br />

**Step 5: Overloading the `/time` endpoint**
-------------

In order for us to see what happens when we change a critical (frequently hit) line, we will need to hit the `/time` endpoint. In a python shell, run the following with the server running
```
import requests
import time

for i in range(100):
    print(i)
    requests.get('http://127.0.0.1:8080/time')
    time.sleep(0.1)
```
This should hit our `/time` endpoint 100 times and upload the telemetry data to Codecov.

<br />

**Step 6: Making a change to critical code**
-------------

Let's now make a change in our code to see if what we are changing is critical.

In `example-app/utils/time.py`, update line 4 from
```
    return datetime.strftime(time, '%Y-%m-%d %H:%M:%S')
```
to
```
    return datetime.strftime(time, '%Y-%m-%d:%H:%M:%S')
```


You will also need to update the tests. Change line 7 of `example-app/utils/tests/test_time.py`
```
    assert(format_time(current_time) == datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S'))
```
to
```
    assert(format_time(current_time) == datetime.strftime(current_time, '%Y-%m-%d:%H:%M:%S'))
```

Save the changes, create a new branch, and push to GitHub.
```
git checkout -b 'test-codecov'
git add example-app/
git commit -m 'fix: update time display with colon'
git push origin test-codecov
```
Open a new pull request. Be sure to set the base branch to your fork.

<br />

**Step 7: Seeing Impact Analysis in the UI**
-------------

After CI/CD has completed, you should see a comment from Codecov similar to this [PR](https://github.com/codecov/impact-analysis-example-python/pull/14). The comment will now show 2 new elements

1. Under `impacted files`, you should see a `Critical` label next to `example-app/utils/time.py`. This means that the PR has a change in that file that is frequently hit in production.
2. Under `related entrypoints`, you should see `/time`. This means that the PR has a change that touches that endpoint.

You should now be able to see how Impact Analysis can give crucial information on how a code change can affect critical code in your system.

### Using your own repositories
To get started with Impact Analysis on your own repositories, check out our getting started [guide](https://docs.codecov.com/docs/impact-analysis-python).
