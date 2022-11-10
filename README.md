# yt2mp44web

YouTube to mp4 (on the web)

## Install requirements

```sh
sudo apt install wget ffmpeg firefox-esr -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
sudo tar xvzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/bin/
chmod +x /usr/bin/geckodriver
rm geckodriver-v0.30.0-linux64.tar.gz
pip3 install -r requirements.txt
```

## Run

```sh
python3 main.py
```

Sometimes it returns an error but if you try again it usually succeeds.
