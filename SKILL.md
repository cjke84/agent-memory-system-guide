---
name: agent-memory-system-guide
description: OpenClaw 和 Codex 可用的 Agent 长期记忆搭建指南。用于 MEMORY.md 三层架构、每日笔记、记忆蒸馏、Obsidian 备份与向量检索的规划和落地。
---

# Agent Memory System Guide

> 🧠 从零搭建 Agent 长期记忆系统。基于 OpenClaw 实战，覆盖 `MEMORY.md` 架构、每日笔记、记忆维护、Obsidian 备份全流程。

## 触发词

`记忆系统`、`memory-setup`、`搭建记忆`、`记忆架构`

## 5 分钟快速上手

**如果你赶时间，只做三步：**

### 第一步：创建 `MEMORY.md`

```markdown
# MEMORY.md

> 长期记忆。只保留会持续影响协作的事实、偏好和决策。

## User

- Preferred name: K
- Timezone: Asia/Shanghai

## 当前任务

- [ ] 正在做的事

## 决策记录

- YYYY-MM-DD: 决策内容 + 原因

## 踩坑记录

- 问题 → 解决方案
```

### 第二步：创建每日笔记

```markdown
# memory/2026-03-20.md

## 完成
- 分析了网宿科技

## 决策
- 暂不加仓

## 踩坑
- （无）

## 待办
- [ ] 明天要做什么
```

### 第三步：每次对话开始时

```text
memory_search(query="相关关键词")
```

## 核心架构（三层模型）

- `MEMORY.md`：长期记忆，精炼保存
- `memory/YYYY-MM-DD.md`：每日原始记录
- Obsidian：长期归档与备份

## 维护原则

- 下次对话会用到的 → 保留在本地记忆
- 可能永远用不到但值得保留的 → 归档到 Obsidian
- 记忆膨胀时，先蒸馏再保留

## 兼容性

- OpenClaw-compatible skill
- Codex-compatible skill
- Obsidian vault workflows
