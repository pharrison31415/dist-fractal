import requests
import pickle
from job import Job
import env


def get_job():
    resp = requests.get(f"http://{env.SERVER_IP}:{env.SERVER_PORT}/job")
    new_job = pickle.loads(resp.content)
    return new_job


def post_job(job):
    resp = requests.post(
        f"http://{env.SERVER_IP}:{env.SERVER_PORT}/job",
        data=pickle.dumps(job))
    return resp.status_code == requests.codes.ok


def main():
    new_job = None

    # try:
    new_job = get_job()
    # print(new_job)
    new_job.exec()
    new_job.real_start = 1
    post_job(new_job)

    # except:
    # print("A job was not correctly recieved")


if __name__ == "__main__":
    main()
