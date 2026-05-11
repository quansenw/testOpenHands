# 会话交接记录

创建时间：2026-04-08

## 1. 当前项目背景

项目是一个“本地分类信息平台”，当前工作方式是：

- 按模块逐个分析
- 每个模块独立出文档
- 先做业务/页面分析
- 再做数据库映射
- 再做 API 设计
- 再做测试/验收文档

## 2. 全局硬约束

- 已经存在数据库文档
- 所有分析与实现必须以现有数据库结构为准
- 不允许更改数据库文档中的表结构设计
- 如果页面需求与数据库结构不一致，优先做兼容方案，不直接改库
- 整站图片上传统一采用七牛上传
- 图片信息至少包含：
  - `path`
  - `size`
  - `width`
  - `height`
- 统计类能力当前只能较稳定记录登录用户点击
- 无法准确确认用户是否真实发起信息或拨打电话
- 因此统计数据与真实情况存在偏差属于正常现象
- 统计类模块相对独立，建议在前台主流程完成后再补充

## 3. 已完成模块

### 3.1 分类模块

文档已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/category/00-summary.md)
- [01-overview-and-global-settings.md](/Users/jiesen/project/xinxi2/docs/modules/category/01-overview-and-global-settings.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/category/02-db-mapping.md)
- [03-api-design.md](/Users/jiesen/project/xinxi2/docs/modules/category/03-api-design.md)
- [04-test-cases.md](/Users/jiesen/project/xinxi2/docs/modules/category/04-test-cases.md)

当前分类模块已确认的关键规则：

- 分类支持树形结构
- 最终发布落点必须是叶子分类
- 如果一级分类已有二级分类，则一级分类退化成容器分类
- 分类配置采用：
  - 分类模块公共配置
  - 单分类独立配置
- 字段模型 = 系统字段 + 自定义字段
- 硬规则：
  - 发布/编辑表单先按系统字段顺序渲染
  - 当遇到 `详细描述` 时，先插入全部自定义字段，再继续剩余系统字段
- 系统字段类型不可编辑
- 自定义字段类型不可编辑
- 平台至少并行支持：
  - 免费发布
  - 套餐发布
  - 普通单次付费发布
  - 付费刷新
  - 付费置顶
  - 热门推广

### 3.2 信息列表模块

文档已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/information/00-summary.md)
- [01-info-list.md](/Users/jiesen/project/xinxi2/docs/modules/information/01-info-list.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/information/02-db-mapping.md)
- [03-api-design.md](/Users/jiesen/project/xinxi2/docs/modules/information/03-api-design.md)
- [04-test-cases.md](/Users/jiesen/project/xinxi2/docs/modules/information/04-test-cases.md)

当前信息列表模块已确认的关键规则：

- 状态页签：
  - 全部
  - 通过
  - 待审
  - 拒绝
  - 待支付
  - 已失效
  - 已删除
- 待审审核弹窗支持：
  - 预设理由
  - 自定义理由
  - 通知作者
  - 在分类首页显示
  - 退款给作者
  - 退套餐给作者
- 通过态编辑后：
  - 不触发敏感词，状态不变
  - 触发敏感词，自动进入待审
- 待审态编辑后：
  - 状态保持待审
- 待支付下的信息通过后：
  - 只改变信息状态
  - 不改变各商户平台下的订单状态
- 当前阶段暂不深挖：
  - 更多
  - 加热
  - 转发
  - 添加客户至CRM

### 3.3 交易 / 套餐设置模块

文档已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/transaction/00-summary.md)
- [01-package-settings.md](/Users/jiesen/project/xinxi2/docs/modules/transaction/01-package-settings.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/transaction/02-db-mapping.md)
- [03-api-design.md](/Users/jiesen/project/xinxi2/docs/modules/transaction/03-api-design.md)
- [04-test-cases.md](/Users/jiesen/project/xinxi2/docs/modules/transaction/04-test-cases.md)

当前交易/套餐模块已确认的关键规则：

- 套餐是分类信息业务下的复合权益包
- 套餐可设置为：
  - 全分类适用
  - 指定分类适用
- 套餐支持：
  - 免费发布次数 + 有效天数
  - 刷新次数
  - 类别置顶天数
  - 分类首页 + 类别置顶天数
  - 查看简历库次数
  - 自定义内容
- 价格按端区分：
  - 安卓小程序 / APP / PC：现金
  - iOS 小程序：虚拟币
- 套餐支持：
  - 前端显示开关
  - 发布到前端购买页
  - 优先级排序
  - 新增 / 编辑 / 删除

### 3.4 审核操作理由模块

文档已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/audit-reasons/00-summary.md)
- [01-audit-reasons.md](/Users/jiesen/project/xinxi2/docs/modules/audit-reasons/01-audit-reasons.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/audit-reasons/02-db-mapping.md)
- [03-api-design.md](/Users/jiesen/project/xinxi2/docs/modules/audit-reasons/03-api-design.md)
- [04-test-cases.md](/Users/jiesen/project/xinxi2/docs/modules/audit-reasons/04-test-cases.md)

当前审核操作理由模块已确认的关键规则：

- 该模块维护信息审核弹窗里的预设理由库
- 支持：
  - 新增
  - 编辑
  - 删除
  - 拖拽排序
- 最终拒绝结果明确落到：
  - `s_fenlei_info.deny_reason`
- 理由库主表已锁定为 `s_fenlei_audit_reason`（经真实数据验证）

### 3.5 评论列表模块

文档已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/comments/00-summary.md)
- [01-comment-list.md](/Users/jiesen/project/xinxi2/docs/modules/comments/01-comment-list.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/comments/02-db-mapping.md)
- [03-api-design.md](/Users/jiesen/project/xinxi2/docs/modules/comments/03-api-design.md)
- [04-test-cases.md](/Users/jiesen/project/xinxi2/docs/modules/comments/04-test-cases.md)

当前评论列表模块已确认的关键规则：

- 状态页签：
  - 待审
  - 通过
  - 不通过
- 列表支持按：
  - 用户名
  - 信息ID
  - 评论关键词
筛选
- 单条评论支持：
  - 通过
  - 不通过
  - 详情
- `详情` 打开的不是评论详情，而是评论所属信息详情
- 信息详情弹窗底部支持对该信息下评论进行内联审核

### 3.6 发布信息模块

文档当前已完成：

- [00-summary.md](/Users/jiesen/project/xinxi2/docs/modules/publish/00-summary.md)
- [01-publish-flow.md](/Users/jiesen/project/xinxi2/docs/modules/publish/01-publish-flow.md)
- [02-db-mapping.md](/Users/jiesen/project/xinxi2/docs/modules/publish/02-db-mapping.md)

当前发布信息模块已确认的关键规则：

- 这是后台发布工作流，不是单一页面
- 当前流程为：
  - 选择分类
  - 填写信息
  - 完成发布
- 填写信息前必须先：
  - 选择发布人
  - 选择发布身份
- 发布身份至少包括：
  - 个人
  - 企业认证
- 表单是按分类模板和字段定义动态生成的
- 后台发布页额外具备：
  - 发布到期时间
  - 背景色
  - 视频号
  - 后台免费置顶
- 当前模块文档已全部完成：
  - `03-api-design.md`
  - `04-test-cases.md`

## 4. 已完成的全局记录

- [2026-04-07-local-classifieds-discovery.md](/Users/jiesen/project/xinxi2/docs/2026-04-07-local-classifieds-discovery.md)

## 5. 当前数据库映射关键结论

### 分类模块核心表

- `s_fenlei_category`
- `s_fenlei_theme`
- `s_fenlei_category_setting`
- `s_fenlei_field`
- `s_fenlei_category_perm`
- `s_fenlei_info`
- `s_fenlei_info_var`
- `s_fenlei_publish_log`
- `s_fenlei_package`
- `s_fenlei_package_log`
- `s_fenlei_package_user`

### 信息列表模块核心表

- `s_fenlei_info`
- `s_fenlei_info_var`
- `s_fenlei_user_log`
- `s_fenlei_publish_log`
- `s_fenlei_package_log`
- `s_fenlei_package_user`
- `s_fenlei_refresh_log`
- `s_fenlei_refresh_record`
- `s_fenlei_refresh_setting`
- `s_fenlei_operate_log`
- `s_user`
- `s_group`
- `s_group_user`

### 交易 / 套餐设置模块核心表

- `s_fenlei_package`
- `s_fenlei_package_user`
- `s_fenlei_package_log`
- `s_fenlei_publish_log`
- `s_fenlei_user_log`
- `s_fenlei_category`

### 评论列表模块核心表

- `s_fenlei_comment`
- `s_fenlei_info`
- `s_fenlei_info_var`
- `s_user`

### 发布信息模块核心表

- `s_fenlei_category`
- `s_fenlei_theme`
- `s_fenlei_field`
- `s_fenlei_category_setting`
- `s_user`
- `s_group`
- `s_group_user`
- `s_user_real_auth`
- `s_fenlei_info`
- `s_fenlei_info_var`
- `s_fenlei_publish_log`
- `s_fenlei_package_user`
- `s_fenlei_package_log`
- `s_fenlei_user_log`

## 6. 当前完成度判断

当前已经完整闭环的模块包括：

- 分类模块
- 信息列表模块
- 交易 / 套餐设置模块
- 审核操作理由模块
- 评论列表模块

这些模块当前都已经具备：

- 模块总结
- 页面/业务分析
- 数据库映射
- API 设计
- 测试/验收文档

因此当前已经足够：

- 继续分析时作为上下文依据
- 进入接口实现设计
- 进入联调准备

补充说明：

- 发布信息模块当前完成度低一层
- 已有总结、页面/业务分析、数据库映射
- 还未补 API 设计与测试文档

## 7. 下个会话建议从哪里继续

下一个推荐动作：

- 优先补完 `发布信息` 模块：
  - `03-api-design.md`
  - `04-test-cases.md`

如果暂不继续发布模块，下一个新模块可选：

- `用户操作日志`
- `平台 / 小程序设置`
- `平台 / PC设置`
- `运营 / 营销助手`

## 8. 下个会话建议工作方式

继续沿用当前节奏：

1. 先分析一个新模块
2. 为该模块建立独立目录
3. 先出：
   - `00-summary.md`
   - `01-*.md`
   - `02-db-mapping.md`
4. 再补：
   - `03-api-design.md`
   - `04-test-cases.md`

若某模块已做到 `00-02`，则优先先补齐到闭环，再开下一个模块。

## 9. 代码实现进度

### 9.1 service-api（后端）

已完成模块：

- **后台登录认证（admin-auth）**
  - `POST /api/admin/auth/login` — 账号登录，返回 token + user
  - `GET /api/admin/auth/me` — 获取当前用户信息
  - `POST /api/admin/auth/logout` — 退出登录
  - 分层实现：路由层 → 服务层 → 数据层
  - Token 方式：SHA256(manage_id:bearer_start:secret)
  - 密码校验当前为简化模式（只验证账号是否存在）

- **分类管理（category）**
  - `GET /api/admin/fenlei/category/tree` — 分类树（含子分类嵌套）
  - `GET /api/admin/fenlei/category/list` — 分类列表（支持 status 筛选）
  - `GET /api/admin/fenlei/category/themes` — 模板列表（8个模板）
  - `POST /api/admin/fenlei/category` — 新建分类
  - `PUT /api/admin/fenlei/category/{id}` — 编辑分类
  - `PATCH /api/admin/fenlei/category/{id}/status` — 切换分类状态
  - `GET/PUT /api/admin/fenlei/category/{id}/basic` — 单分类基础设置
  - `GET /api/admin/fenlei/category/{id}/fields` — 字段列表（含渲染规则、招聘模板锚点差异）
  - `POST /api/admin/fenlei/category/{id}/fields` — 新增自定义字段
  - `PUT /api/admin/fenlei/category/{id}/fields/{field_id}` — 编辑字段
  - `GET/PUT /api/admin/fenlei/category/{id}/perm` — 分类权限配置
  - ORM 模型：Category, Theme, CategorySetting, Field, CategoryPerm

- **发布信息（publish）**
  - `GET /api/admin/fenlei/publish/categories` — 发布分类树（只返回启用+标记 can_publish）
  - `GET /api/admin/fenlei/publish/users` — 搜索发布人（支持用户名/昵称/手机号）
  - `GET /api/admin/fenlei/publish/users/{id}/identities` — 用户可选发布身份
  - `GET /api/admin/fenlei/publish/form-schema` — 动态表单 Schema（含字段排序规则、招聘模板锚点）
  - `POST /api/admin/fenlei/publish/info` — 发布信息（写入 info + info_var + publish_log，title 自动同步）
  - `GET /api/admin/fenlei/publish/result/{id}` — 发布结果查询
  - ORM 模型：User, Group, GroupUser, Info, InfoVar, PublishLog
  - 已验证：发布后 title 从动态字段同步到 s_fenlei_info.title

- **信息列表与审核（information）**
  - `GET /api/admin/fenlei/info/list` — 信息列表（支持 7 个 tab 页签 + 多维筛选 + 排序）
  - `GET /api/admin/fenlei/info/{id}` — 信息详情（含动态字段回填）
  - `POST /api/admin/fenlei/info/{id}/approve` — 审核通过
  - `POST /api/admin/fenlei/info/{id}/reject` — 审核拒绝（含 deny_reason 写入）
  - `PUT /api/admin/fenlei/info/{id}` — 编辑信息（含 title 同步）
  - `DELETE /api/admin/fenlei/info/{id}` — 删除信息（status=5）
  - `POST /api/admin/fenlei/info/{id}/refresh` — 刷新信息
  - `POST /api/admin/fenlei/info/batch/approve|reject|delete` — 批量操作
  - 退款/退套餐逻辑待 Task 7 补充

- **评论管理（comments）**
  - `GET /api/admin/fenlei/comments` — 评论列表（支持 pending/passed/rejected 三个 tab）
  - `POST /api/admin/fenlei/comments/{id}/approve` — 评论通过
  - `POST /api/admin/fenlei/comments/{id}/reject` — 评论不通过
  - `GET /api/admin/fenlei/comments/info/{info_id}` — 按信息聚合评论
  - `GET /api/admin/fenlei/comments/info/{info_id}/detail-with-comments` — 信息详情+评论聚合
  - ORM 模型：Comment

- **审核理由（audit-reasons）**
  - `GET /api/admin/fenlei/audit-reasons` — 理由列表
  - `POST /api/admin/fenlei/audit-reasons` — 新增理由
  - `PUT /api/admin/fenlei/audit-reasons/{id}` — 编辑理由
  - `DELETE /api/admin/fenlei/audit-reasons/{id}` — 删除理由（逻辑删除 status=0）
  - `PATCH /api/admin/fenlei/audit-reasons/sort` — 批量排序
  - ORM 模型：AuditReason

### 9.2 admin-web（后台管理前端）

已完成模块：

- **项目脚手架**
  - Vite + React 18 + TypeScript
  - 依赖：antd, @ant-design/icons, axios, zustand, react-router-dom, dayjs
  - 开发端口：7002，API 代理到 7001

- **登录模块（admin-auth 前端）**
  - 登录页：账号 + 密码输入 → 调用 `/api/admin/auth/login` → 成功跳转首页
  - Auth Store：Zustand + persist，token 持久化到 localStorage
  - 请求工具：axios 封装，自动注入 Authorization，401 自动跳登录页
  - 路由守卫：RequireAuth 组件，未登录重定向到 /login
  - 主布局：侧边栏导航（统计概览/分类管理/信息管理/发布信息/评论管理）+ 顶栏用户信息 + 退出按钮
  - 占位页面：统计概览（StatsPage）

- **分类管理模块（category 前端）**（已按效果图对齐）
  - 分类列表页（`/category`）：树形表格展示全部分类，支持展开/折叠
    - 顶部 Tab 切换：全部 / 启用 / 禁用
    - 表格列：ID、图标（彩色 Avatar）、分类名称、分类数量、使用模板、排序、状态开关、编辑
    - 编辑列规则：
      - 有二级分类的一级分类：只显示「编辑分类 / 添加二级分类」
      - 叶子分类或无子分类的一级分类：显示「基础设置 / 字段设置 / 费用及权限」
    - 添加二级分类弹窗自动锁定父分类
  - 分类设置页（`/category/edit/:id`）：三个 Tab，支持 `?tab=` 参数直达
    - 基础设置：分类名称、标签颜色、排序、发布须知
    - 字段设置：系统字段+自定义字段列表，新增/编辑字段弹窗
    - 费用及权限：用户组列表，启用/置顶/跟随全局开关
  - API 层：`api/category.ts`
  - Mock 数据：4个一级分类 + 9个二级分类

- **发布信息模块（publish 前端）**
  - 四步向导：选择分类 → 选择发布人 → 填写信息 → 完成
  - StepCategory：分类树展示，只允许选择可发布的叶子分类
  - StepPublisher：搜索用户 → 选择发布身份（弹窗单选，显示不可用原因）
  - StepForm：根据 form-schema API 动态渲染表单字段 + 后台专属字段（到期时间、背景色、视频号、免费置顶）
  - StepResult：展示发布结果（状态、发布类型、是否需审核）
  - API 层：`api/publish.ts`（categories/searchUsers/getIdentities/getFormSchema/submitInfo/getResult）

- **信息管理模块（info 前端）**
  - 信息列表页（`/info`）：7个状态页签（全部/通过/待审/拒绝/待支付/已失效/已删除）
  - 支持关键词搜索、批量选择
  - 列表卡片：封面缩略图、标题+分类路径、发布人+身份标签、状态标签、浏览量、发布时间
  - 审核操作：单条/批量通过/拒绝弹窗，集成审核理由下拉（调用 auditReason options API）
  - 拒绝弹窗：预设理由、自定义理由、通知作者、退款给作者、退套餐开关
  - 刷新和删除操作
  - API 层：`api/info.ts`（list/detail/approve/reject/batchApprove/batchReject/batchDelete/refresh/delete）
  - API 层：`api/auditReason.ts`（list/options/create/update/delete/sort）

- **评论管理模块（comment 前端）**
  - 评论列表页（`/comment`）：3个状态页签（待审/通过/不通过）
  - 支持评论关键词搜索
  - 列表：评论内容、用户名、所属信息（ID+标题）、状态标签、时间
  - 单条通过/拒绝操作
  - API 层：`api/comment.ts`（list/approve/reject/getByInfo）

- **用户管理模块（user 前端）**
  - 用户列表页（`/user`）：用户名/手机号搜索
  - 表格列：ID、头像、用户名/昵称、手机号、用户组标签、资产（金币/虚拟币）、信息数、状态、注册时间
  - 操作列：详情、用户组、封禁/解封
  - 用户详情抽屉：基础信息、资产、用户组（可添加/移除）、封禁状态、封禁历史时间线
  - 封禁弹窗：天数 + 原因
  - 用户组弹窗：选择用户组 + 有效天数
  - API 层：`api/user.ts`（list/detail/getGroups/addGroup/removeGroup/getGroupList/forbid/unforbid/getForbidHistory）
  - Mock 数据：5个用户 + 5个用户组 + 封禁历史

### 9.3 admin-web 前端路由总览

| 路由 | 页面 | 状态 |
|------|------|------|
| `/login` | 登录页 | 已完成 |
| `/stats` | 统计概览 | 占位 |
| `/category` | 分类列表 | 已完成 |
| `/category/edit/:id` | 分类设置 | 已完成 |
| `/publish` | 发布信息 | 已完成 |
| `/info` | 信息管理 | 已完成 |
| `/comment` | 评论管理 | 已完成 |
| `/user` | 用户管理 | 已完成 |

## 10. 备注

- 第一阶段文档分析已全部完成
- 第二阶段代码实现已完成 admin-web 前端主业务闭环 + 用户管理
- 已完成前端模块：登录、分类管理、发布信息、信息管理（含审核理由联动）、评论管理、用户管理
- 后端目前仅完成 auth + category 模块，其余后端 API 尚需实现
- 下一步：按开发计划实现对应后端 API，或继续其他后台管理模块
