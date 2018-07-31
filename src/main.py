from load_data import time_series
import outgoing
import json


def load_config() -> dict:
    with open("/data/config.json", "rb") as f:
        config = json.load(f)
    return config


def main():
    df = time_series()
    config = load_config()
    outgoing.send_request({"foo": 100}, config)
    return df


if __name__ == '__main__':
    print(main())
