import os
from langchain_community.document_loaders import WebBaseLoader


def get_job_description(job_description, job_post_url):
    if job_description != "":
        return job_description
    else:
        job_post_url_data=WebBaseLoader(job_post_url).load()
        return job_post_url_data
    