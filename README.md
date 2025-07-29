# vitepress-fastapi-auth

一个将 Vitepress 前端与 FastAPI 后端认证相结合的安全文档解决方案。

## 特性
- **FastAPI认证**：基于JWT的认证系统，支持基于角色的访问控制
- **Vitepress集成**：受保护的文档路由，带有无缝的认证流程
- **安全访问控制**：文档页面的细粒度权限管理
- **现代UI**：简洁、响应式设计，内置深色模式支持

![特性展示图片](预留图片路径)

## 技术架构
- **前端**：Vitepress与Vue 3组件
- **后端**：FastAPI，使用Pydantic模型和Tortoise-ORM
- **认证**：基于JWT令牌的认证，使用安全的HTTP-only cookies
- **数据库**：SQLite，支持迁移

![系统架构图](预留图片路径)

## 安装指南

### 前提
- Python 3.10+
- Node.js 18+
- pnpm

### 后端
```bash
cd backend
pipenv --python 3
pipenv shell
pip install -r requirements.txt
uvicorn main:app --reload
```

### 前端
```bash
pnpm i
pnpm dev
```

![安装步骤截图](预留图片路径)