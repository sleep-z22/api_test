import requests
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import BASE_URL, TIMEOUT
from utils.logger import logger


class APIClient:
    def __init__(self):
        #初始化客户端
        self.base_url = BASE_URL.strip()
        self.session = requests.Session()
        logger.info(f"API客户端初始化完成，地址: {self.base_url}")
    def _request(self,method:str,endpoint:str,data = None,params = None):
        #拼接完整URL
        base = self.base_url.rstrip('/')
        endpoint_clean = endpoint.lstrip('/')
        url = f"{base}/{endpoint_clean}"
        url = url.replace(' ','')
        #记录请求日志
        logger.info(f"{method}请求:{url}")
        if params:
            logger.info(f"请求参数:{params}")
        if data:
            logger.info(f"请求数据:{data}")
        #根据方法类型发送请求
        if method == 'GET':
            response = self.session.get(url,params=params,timeout=TIMEOUT)
        elif method == 'POST':
            response = self.session.post(url,json=data,timeout=TIMEOUT)
        elif method == 'PUT':
            response = self.session.put(url,json=data,timeout=TIMEOUT)
        elif method == 'DELETE':
            response = self.session.delete(url,timeout = TIMEOUT)
        else:
            raise ValueError(f"不支持的请求方法:{method}")
        logger.info(f"响应状态码:{response.status_code}")
        return response
    def get(self,endpoint:str,params=None):
        """
                发送PUT请求（更新数据）
                :param endpoint: API端点，如 "/posts/1"
                :param data: 要更新的数据，字典格式
                :return: 响应对象
        """
        return self._request("GET",endpoint,params=params)
    def post(self,endpoint:str,data=None):
        return self._request("POST",endpoint,data=data)
    def put(self,endpoint:str,data=None):
        return self._request("PUT",endpoint,data=data)
    def delete(self,endpoint:str):
        return self._request("DELETE",endpoint)

    def close(self):
        #关闭对话，释放连接
        self.session.close()
        logger.info("API客户端已关闭")

# 创建全局客户端
client = APIClient()