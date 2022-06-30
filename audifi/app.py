import os
import dotenv


if __name__ == '__main__':
    if dotenv.load_dotenv():

        for key in os.environ.keys():
            print(f"{key} == {os.environ[key]}")
