import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import BASE_URL, TIMEOUT
from utils.logger import logger


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL.strip()
        self.session = requests.Session()
        logger.info(f"API客户端初始化完成，地址: {self.base_url}")

    def get(self, endpoint, params=None):
        base = self.base_url.rstrip('/')
        endpoint = endpoint.lstrip('/')
        url = f"{base}/{endpoint}"
        url = url.replace(' ', '')

        logger.info(f"GET请求:{url}")

        response = self.session.get(url, params=params, timeout=TIMEOUT)
        logger.info(f"相应状态码:{response.status_code}")

        return response

    def post(self, endpoint, data=None):
        """发送POST请求"""
        base = self.base_url.rstrip('/')
        endpoint = endpoint.lstrip('/')
        url = f"{base}/{endpoint}"
        url = url.replace(' ', '')

        logger.info(f"POST请求: {url}")
        response = self.session.post(url, json=data, timeout=TIMEOUT)
        logger.info(f"响应状态码: {response.status_code}")
        return response

    def put(self, endpoint, data=None):
        """发送PUT请求"""
        base = self.base_url.rstrip('/')
        endpoint = endpoint.lstrip('/')
        url = f"{base}/{endpoint}"
        url = url.replace(' ', '')

        logger.info(f"PUT请求: {url}")
        response = self.session.put(url, json=data, timeout=TIMEOUT)
        logger.info(f"响应状态码: {response.status_code}")
        return response

    def delete(self, endpoint):
        """发送DELETE请求"""
        base = self.base_url.rstrip('/')
        endpoint = endpoint.lstrip('/')
        url = f"{base}/{endpoint}"
        url = url.replace(' ', '')

        logger.info(f"DELETE请求: {url}")
        response = self.session.delete(url, timeout=TIMEOUT)
        logger.info(f"响应状态码: {response.status_code}")
        return response

    def close(self):
        self.session.close()


# 创建全局客户端
client = APIClient()