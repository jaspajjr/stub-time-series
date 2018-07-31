import time
import json
from load_data import time_series
import outgoing


def load_config() -> dict:
    with open("/data/config.json", "rb") as f:
        config = json.load(f)
    return config


def main():
    df = time_series()
    config = load_config()

    for row in df.iterrows():
        outgoing.send_request(row[1]['Open'], config)
        time.sleep(int(config['interval']))


if __name__ == '__main__':
    print(main())
