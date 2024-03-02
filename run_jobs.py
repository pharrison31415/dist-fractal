import requests
import pickle
from job import Job
import env


def get_job():
    resp = requests.get(f"http://{env.SERVER_IP}:{env.SERVER_PORT}/job")
    new_job = pickle.loads(resp.content)
    return new_job


def main():
    new_job = None

    # try:
    new_job = get_job()
    # print(new_job)
    new_job.exec()
    # except:
    # print("A job was not correctly recieved")


if __name__ == "__main__":
    main()
