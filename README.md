# WhereToShieldsBadges
[![Endpoint](https://img.shields.io/website?down_message=offline&label=endpoint&up_message=online&url=https%3A%2F%2Fo3x72k5hu9.execute-api.us-west-1.amazonaws.com%2Fapi)](https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api)

This repository contains source code for custom endpoints used by the [shields.io](https://shields.io/) badges on the [WhereTo](https://github.com/park-junha/WhereTo) README.

## Running the App

This app was developed with Python 3.8.5.

```
# Install dependencies
pip3 install -r requirements.txt

# Run the app
python3 app.py
```

Optionally, you can create / use a virtual environment to segregate your installed dependencies from your main work environment:

```
# To create virtual environment (one time only)
mkdir ~/.virtualenv
cd ~/.virtualenv
python3 -m venv WhereToShieldsBadges

# To activate virtual environment (must run every time)
source ~/.virtualenv/WhereToShieldsBadges/bin/activate

# To install dependencies to your environment (one time only, run above command first)
cd /path/to/WhereToShieldsBadges
pip3 install -r requirements.txt
```

## Badges

The following badges use the custom endpoints:

- [![Chrome](https://img.shields.io/endpoint?url=https%3A%2F%2Fo3x72k5hu9.execute-api.us-west-1.amazonaws.com%2Fapi%2Fchrome)](https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/chrome) - https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/chrome
- [![Firefox](https://img.shields.io/endpoint?url=https%3A%2F%2Fo3x72k5hu9.execute-api.us-west-1.amazonaws.com%2Fapi%2Ffirefox)](https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/firefox) - https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/firefox
- [![Safari](https://img.shields.io/endpoint?url=https%3A%2F%2Fo3x72k5hu9.execute-api.us-west-1.amazonaws.com%2Fapi%2Fsafari)](https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/safari) - https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/safari
- [![Edge](https://img.shields.io/endpoint?url=https%3A%2F%2Fo3x72k5hu9.execute-api.us-west-1.amazonaws.com%2Fapi%2Fedge)](https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/edge) - https://o3x72k5hu9.execute-api.us-west-1.amazonaws.com/api/edge
