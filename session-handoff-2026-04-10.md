# Session Handoff — 2026-04-10

## 当前阶段：APP 前台开发 — 全部功能开发完成

## 已确认决策

- 登录方式：手机号 + 短信验证码，登录即注册
- 开发策略：前后端并行开发，sub-agent 模式
- 开发优先级：先搭框架 → 消费链路 → 发布链路

## 模块开发进度

| 模块 | 效果图 | 后端 API | 前端页面 | 状态 |
|------|--------|----------|---------|------|
| 基础设施（项目初始化） | - | ✅ 完成 | ✅ 完成 | ✅ 完成 |
| 七牛云上传 | - | ✅ client/upload/token | ✅ utils/upload.js | ✅ 完成 |
| 搜索功能 | - | ✅ 复用 info/list | ✅ 搜索页 | ✅ 完成 |
| 用户中心-我的发布 | - | ✅ user/my-posts | ✅ 发布列表页 | ✅ 完成 |
| 用户中心-我的评论 | - | ✅ user/my-comments | ✅ 评论列表页 | ✅ 完成 |
| app-login（登录） | 无 | ✅ 4个接口 | ✅ 登录页 | ✅ 完成 |
| app-home（首页） | 2张 | ✅ 首页聚合接口 | ✅ 首页（搜索+分类+商家+信息流） | ✅ 完成 |
| app-local-recommend（本地推荐） | 无 | ✅ 复用info/list | ✅ 推荐列表页 | ✅ 完成 |
| app-category-list（分类列表） | 2张 | ✅ 分类树+子分类+信息列表 | ✅ 分类列表+信息列表 | ✅ 完成 |
| app-user-center（用户中心） | 无 | ✅ /auth/me | ✅ 用户中心页 | ✅ 完成 |
| app-info-detail（信息详情） | 2张 | ✅ 详情+评论接口 | ✅ 完整实现 | ✅ 完成 |
| app-merchant-detail（商家详情） | 1张 | ✅ 3个接口 | ✅ 完整实现 | ✅ 完成 |
| app-publish（发布） | 7张 | ✅ 5个接口 | ✅ 6个页面 | ✅ 完成 |
| app-merchant-auth（商家认证） | 3张 | ✅ 4个接口 | ✅ 2个页面 | ✅ 完成 |

## 第一批完成情况

### 后端 (service-api) — 已完成

新增文件 20+，创建 11 个 Client API 端点：

**认证模块 (/api/client/auth)**
- POST /sms/send — 发送短信验证码（60s 频率限制，6位验证码）
- POST /login — 验证码登录（自动注册新用户，生成 uuid4 token）
- GET /me — 获取当前用户信息
- POST /logout — 退出登录

**分类模块 (/api/client/fenlei/category)**
- GET /tree — 前台分类树（status=1）
- GET /{id}/children — 子分类列表（带信息数量）

**信息模块 (/api/client/fenlei/info)**
- GET /list — 信息列表（分类/关键词/排序/分页，置顶优先）
- GET /latest — 最新发布
- GET /{id} — 信息详情（含自定义字段，+1浏览量）
- GET /{id}/comments — 评论列表（仅已通过）

**首页模块 (/api/client/home)**
- GET /data — 首页聚合数据

**新增 ORM 模型**：SmsLog (s_sms_logs)、UserLogin (s_user_login)
**补充字段**：User 模型增加 login_token、current_device、is_secrecy
**新增 Service**：ClientAuthService、ClientCategoryService、ClientInfoService、ClientHomeService
**新增 Repository**：SmsLogRepository、UserLoginRepository、ClientInfoRepository

### 前端 (app) — 已完成

新增文件 33 个，完整的 uni-app + Vue 3 项目：

**项目配置**：package.json、vite.config.js、pages.json（10页面+5Tab）、manifest.json

**Tab 页面**（5个）：
- 首页 — 搜索栏+分类网格+公告+推荐商家+最新发布（分类Tab筛选）
- 本地推荐 — 信息流+下拉刷新+触底加载
- 发布 — 占位页面+登录拦截
- 出售房屋 — 固定分类信息列表
- 用户中心 — 登录/未登录态+用户信息+功能菜单+退出

**功能页面**（5个）：
- 登录页 — 手机号+验证码+60s倒计时+redirect回流
- 分类列表 — 图标+名称+数量+箭头（匹配效果图）
- 分类信息列表 — 子分类Tab+筛选+InfoCard列表+分页
- 信息详情 — 骨架页面
- 全部评论 — 骨架页面

**通用组件**：InfoCard（左图右文卡片）、MerchantCard（商家卡片）、Empty（空态）
**基础设施**：request.js（请求封装+token+401处理）、Pinia store、useLogin composable、formatTime工具

## 开发批次规划

### ✅ 第一批（框架 + 核心浏览）— 已完成
- 项目初始化（前后端基础设施）
- app-login（全局登录能力）
- app-home（首页）
- app-category-list（分类列表 + 信息列表）
- app-local-recommend（本地推荐）
- app-user-center（用户中心）

### ✅ 第二批（详情消费）— 已完成
- app-info-detail（信息详情 + 评论）— 前端完整实现（图片swiper、价格、标签、内容、联系人、评论摘要、猜你喜欢、底部咨询/打电话）
- app-info-detail/comments — 评论页完整实现（警告横幅、评论列表、输入框、底部操作栏）
- app-merchant-detail — 后端 Store/StoreType 模型 + 3个API + 前端完整实现（头图、名称、简介、地址、标签、发布信息列表）

**后端新增：**
- Store ORM 模型 (s_stores) + StoreType 模型 (s_stores_types)
- GET /api/client/store/recommended — 推荐商家列表
- GET /api/client/store/{id} — 商家详情
- GET /api/client/store/{id}/info — 商家发布的信息
- 首页聚合接口新增 recommended_merchants 字段

**前端新增/重写：**
- pages/info/detail.vue — 完全重写，匹配效果图
- pages/info/comments.vue — 完全重写，匹配效果图
- pages/merchant/detail.vue — 新建
- api/store.js — 新建
- MerchantCard 组件更新（跳转商家详情）
- pages.json 新增商家详情路由

### ✅ 第三批（发布链路）— 已完成
- app-publish — 完整发布流程（分类选择→二级分类→身份选择→动态表单→支付→成功页）
- app-merchant-auth — 商家认证（分类选择→认证表单+须知弹窗+驳回态重认证）

**后端新增：**
- GET /api/client/publish/categories — 发布分类树
- GET /api/client/publish/identities — 用户可选发布身份
- GET /api/client/publish/form-schema — 动态表单字段
- POST /api/client/publish/submit — 发布提交（source=1 APP端，默认365天）
- GET /api/client/publish/result/{id} — 发布结果
- GET /api/client/merchant-auth/status — 认证状态
- GET /api/client/merchant-auth/categories — 商家分类
- GET /api/client/merchant-auth/detail — 认证资料回显
- POST /api/client/merchant-auth/submit — 提交/重新认证

**前端新增：**
- pages/publish/category.vue — 3列图标网格分类选择
- pages/publish/subcategory.vue — 二级分类列表
- pages/publish/identity.vue — 个人/推荐商家双卡片
- pages/publish/form.vue — 动态字段表单+图片上传+置顶选项+套餐
- pages/publish/payment.vue — 支付页（微信支付占位）
- pages/publish/success.vue — 成功页+再发一条/关闭
- pages/merchant-auth/category.vue — 商家分类选择
- pages/merchant-auth/form.vue — 认证表单（Logo/标签/地址+须知弹窗+驳回态）
- api/publish.js、api/merchantAuth.js

## 文档完成情况

所有 APP 模块文档已完整（00-04 文档包）：
- app-front-map ✅
- app-login ✅（本次新建）
- app-home ✅
- app-local-recommend ✅（本次补齐）
- app-category-list ✅
- app-info-detail ✅
- app-publish ✅
- app-user-center ✅
- app-merchant-auth ✅
- app-merchant-detail ✅
- app-merchant-results ✅（轻量说明文档）
