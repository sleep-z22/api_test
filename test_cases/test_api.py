import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.api_client import client
from utils.logger import logger

def test_get_post():
    logger.info("========== 开始测试获取帖子 ==========")
    response = client.get("/posts/1")

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1

    logger.info(f"✅ 测试通过！帖子标题: {data['title']}")


def test_get_nonexistent_post():
    """测试：获取不存在的帖子"""
    logger.info("========== 开始测试不存在的帖子 ==========")
    response = client.get("/posts/99999")

    assert response.status_code == 404
    logger.info(f"✅ 正确返回404")


def test_get_all_posts():
    """测试：获取所有帖子"""
    logger.info("========== 开始测试获取所有帖子 ==========")
    response = client.get("/posts")

    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

    logger.info(f"✅ 获取到 {len(data)} 条帖子")


# ========== 新增测试用例 ==========

def test_create_post():
    """测试：创建新帖子（POST请求）"""
    logger.info("========== 开始测试创建帖子 ==========")

    new_post = {
        "title": "新帖子",
        "body": "这是测试内容",
        "userId": 1
    }

    response = client.post("/posts", data=new_post)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "新帖子"
    assert data["userId"] == 1

    logger.info(f"✅ 创建成功！新帖子ID: {data['id']}")


def test_update_post():
    """测试：更新帖子（PUT请求）"""
    logger.info("========== 开始测试更新帖子 ==========")

    update_data = {
        "id": 1,
        "title": "更新后的标题",
        "body": "更新后的内容",
        "userId": 1
    }

    response = client.put("/posts/1", data=update_data)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "更新后的标题"

    logger.info("✅ 更新成功！")


def test_delete_post():
    """测试：删除帖子（DELETE请求）"""
    logger.info("========== 开始测试删除帖子 ==========")

    response = client.delete("/posts/1")

    assert response.status_code == 200

    logger.info("✅ 删除成功！")


# ========== 参数化测试 ==========

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_multiple_posts(post_id):
    """参数化测试：批量获取多个帖子"""
    logger.info(f"========== 测试获取帖子 ID={post_id} ==========")

    response = client.get(f"/posts/{post_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id

    logger.info(f"✅ 帖子 {post_id} 获取成功，标题: {data['title'][:30]}...")


# 也可以测试不同的错误场景
@pytest.mark.parametrize("post_id,expected_status", [
    (1, 200),  # 存在的帖子 → 200
    (2, 200),  # 存在的帖子 → 200
    (999, 404),  # 不存在的帖子 → 404
    (0, 404),  # 无效ID → 404
    (-1, 404), # 负数ID → 404
])
def test_posts_with_expected_status(post_id, expected_status):
    """参数化测试：测试不同ID的预期状态码"""
    logger.info(f"测试帖子ID={post_id}，预期状态码={expected_status}")

    response = client.get(f"/posts/{post_id}")

    assert response.status_code == expected_status
    logger.info(f"✅ 状态码正确: {expected_status}")