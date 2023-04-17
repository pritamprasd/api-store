
import yaml

with open("data.yml", "r") as stream:
    print("start")
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)