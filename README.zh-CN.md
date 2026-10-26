# b2b-growth-kit

给配合 AI agent 工作的小型 B2B 市场团队用的一套工作体系。playbook 讲每个阶段该做什么，workflow 排好多个步骤的先后，39 个 skill 各管一件具体的事，harness 负责检查产出。

[English](README.md)

## 四层怎么配合

```
playbook/        每个阶段做什么、为什么（给人读）
   |
skills/b2b-growth-kit/workflows/   多步骤任务：用哪些 skill、什么顺序、每步交出什么
   |
skills/<name>/   每个只做一件事：输入、做法、产出格式、关卡（给 agent 读）
   |
skills/b2b-growth-kit/policies/    只写一次的规则：审批、证据、指标口径、外联合规
skills/b2b-growth-kit/profile/     公司事实集中在一个 TOML 文件
   |
harness/         对草稿做确定性检查：证据、指标、归因、落地页、线索交接
```

依赖只往一个方向走。skill 里不写任何公司事实（从 profile 读），也不重复任何规则（直接链接 policy）。改一条规则只改一处，换一家公司只换一个文件。

## 快速开始

1. **安装 skill**，拷进 agent 的 skills 目录：

   ```bash
   git clone https://github.com/clairelily2020/b2b-growth-kit.git
   cp -R b2b-growth-kit/skills/* ~/.claude/skills/      # Claude Code
   cp -R b2b-growth-kit/skills/* ~/.codex/skills/       # Codex
   ```

   policies、workflows 和 profile 模板都放在 `skills/b2b-growth-kit/` 里面，跟着 skill 一起装，所有链接拷过去照样能用。

2. **建公司 profile。** 把 `skills/b2b-growth-kit/profile/example-company.toml` 复制到自己工作仓库的 `profiles/private/<公司名>/company.toml`（这个目录不进 git），或者直接让 agent 读你们官网帮你建一份。

3. **直接派活，别只问建议：** "检查一下我们 Google Ads 的转化追踪"、"用这份展商 CSV 做一份潜客名单"、"写一篇'{竞品} alternatives'对比页"、"跑一遍本周增长复盘"。

## Workflow

| 任务 | Workflow |
|---|---|
| 想清楚卖给谁、说什么 | [positioning-sprint](skills/b2b-growth-kit/workflows/positioning-sprint.md) |
| 从目标名单约到会议 | [account-based-outbound](skills/b2b-growth-kit/workflows/account-based-outbound.md) |
| 借展会或大会约客户 | [event-abm](skills/b2b-growth-kit/workflows/event-abm.md) |
| 在搜索和 AI 助手里赢下买家问题 | [content-to-citation](skills/b2b-growth-kit/workflows/content-to-citation.md) |
| 上线或修搜索广告 | [paid-search-launch](skills/b2b-growth-kit/workflows/paid-search-launch.md) |
| 创始人号和品牌号的社媒 | [founder-led-social](skills/b2b-growth-kit/workflows/founder-led-social.md) |
| 产品或功能发布 | [product-launch](skills/b2b-growth-kit/workflows/product-launch.md) |
| 每周的市场复盘 | [weekly-growth-review](skills/b2b-growth-kit/workflows/weekly-growth-review.md) |

## Skill 分组

| 方向 | Skill |
|---|---|
| 中枢 | [b2b-growth-kit](skills/b2b-growth-kit/SKILL.md)：加载 profile 和规则，把请求派给合适的 skill |
| 策略 | icp-and-positioning · offer-design · competitive-intel · market-signal-brief · voice-of-customer |
| 内容、SEO、GEO | seo · answer-engine-content · geo-citation-scout · article-writer · programmatic-pages · link-acquisition · landing-page · prepublish-qa · cms-draft-patcher |
| 付费投放 | google-ads · linkedin-ads · reddit-ads · ad-creative |
| 外联与销售 | prospect-list-builder · cold-email · linkedin-outbound · send-preflight · revenue-handoff |
| 社媒与社区 | founder-led-content · brand-social-content · social-engagement · content-calendar · creator-partnerships · reddit-community |
| 活动策划 | campaign-brief · campaign-review · launch-campaign |
| 数据与运营 | marketing-data-ops · marketing-reporting · performance-diagnosis · growth-plan · ops-brief · martech-scouting |

每个 skill 结构一样：适用场景、输入（含读哪些 profile 字段）、做法、产出格式、关卡、参考。skill 正文是英文，agent 会按你的提问语言回复。

## Playbook

[playbook/](playbook/README.md) 先问你卡在哪：需求验证、首批客户、重复获客、留存扩展、扩量。配有实践方法、15 张渠道卡、模板和实战笔记，每章结尾都链接到对应的 workflow 和 skill。

## Harness

```bash
cd harness && python3 -m b2b_harness ads --input examples/ads.json --as-of 2026-09-17
```

四个确定性检查（`signal`、`ads`、`landing`、`handoff`）加一个审批范围检查。离线运行，只用 Python 标准库。说明见 [harness/README.md](harness/README.md)。

## 几条原则

- **只出草稿，不擅自动手。** 调研、起草、分析随便做；发布、发送、花钱、改在投广告、写 CRM 都要有明确范围的审批（[approval-gates](skills/b2b-growth-kit/policies/approval-gates.md)）。
- **证据优先。** 不知道不等于零，没核实不等于不合格，不编客户、不编引语、不编数字（[evidence-and-claims](skills/b2b-growth-kit/policies/evidence-and-claims.md)）。
- **渠道上不耍花招。** 不用假账号、不做不披露的推广、不买评价、不绕平台规则（[outreach-compliance](skills/b2b-growth-kit/policies/outreach-compliance.md)）。
- **"完成"分三种：** 草稿好了，执行了且有回执，观察期结束后确实有效。

## 仓库检查

```bash
python3 tools/check_repo.py
```

检查链接（包括 skill 里的链接不能跳出 `skills/`，否则安装后会断）、skill 的 frontmatter 和必备章节、CSV 格式、隐私信息模式。在本地放一个不进 git 的 `.denylist.local`，写上绝不能出现的词（公司名、客户、人名），检查会自动拦截。CI 跑同样的检查和 harness 测试。

## 贡献与许可

新增 skill 的模板和规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。MIT 许可。作者 Claire。
