# No AI slop

[English](README.md) · 简体中文 · [日本語](README.ja.md)

这个 Skill 可从你的文本中去除 20 多种 AI 腔模式，也能帮助你检测这类问题。

## 它能发现什么

它能检测的模式包括：

| 模式 | 常见表现 |
|---------|-------------|
| 二元对比 | “不是 X，而是 Y。” |
| 铺垫式开场 | “事情是这样的……” |
| 伪洞见铺垫 | “没人告诉你的是……” |
| 冒号揭示 | “最棒的是：它会学习。” |
| 浮于表面的分析 | “……凸显了团队的投入” |
| 夸大重要性 | “标志着一个关键时刻” |
| 含糊归因 | “专家一致认为”，“研究表明” |
| 假强势动词 | “充当一个集中式枢纽” |
| 同义词轮换 | 先称为 agent，再称为 assistant，接着又称为 tool |
| 否定式列举 | “不是 X。不是 Y。而是 Z。” |
| 戏剧化碎句 | “就这样。事情就是这么简单。” |

它还会落实优质写作的基本原则：在适合时开门见山、使用主动语态、理清难以理解的句子，并优先使用具体数字而非抽象表述。

## 安装

将以下内容粘贴到 Claude Code、Codex 或你常用的 AI 工具中：

“全局安装这个 Skill：[https://github.com/petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)”

## 使用

**1. 编辑草稿。** 粘贴草稿并调用该 Skill：

```
/no-ai-slop

[your draft]
```

你会收到编辑后的草稿，以及一个简短的 What changed（改了什么）部分。该 Skill 会进行最少但有效的修改，然后根据 [eval.md](eval.md) 检查自己的工作。

**2. 检测 AI 腔。** 询问一段文本读起来是否像 AI 所写：

```
/no-ai-slop is this AI slop?

[the text]
```

它会列出发现的每一种模式，并为每项附上对应原句。

## 文件

1. `SKILL.md`：编辑规则和工作流。
2. `eval.md`：该 Skill 用于检查自身编辑结果的通过/失败项目。

## 作者

这是我个人 AI 操作系统中的一个 Skill。包括我的课程和工作流在内的完整库位于 [Behind the Craft](https://behindthecraft.com)。

## 许可证

MIT
