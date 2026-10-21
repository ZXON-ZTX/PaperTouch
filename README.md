# PaperTouch

**英文论文轻修：只改命中规则的片段，其余原样保留。**

PaperTouch 是用于英文论文成稿清理的 AI 编程助手技能。它采用六条明确的编辑白名单，在保留科学含义和文章结构的前提下，清理指定的冗余表达。适用于摘要、正文、方法、讨论、综述及审稿回复。

English academic manuscript cleanup with an explicit six-rule whitelist, minimal span edits, and exact preservation of unmatched text and structure.

## 能做什么

| 规则 | 允许处理的问题 |
|---|---|
| E1 | 不承担必要强调或警示作用的空泛提示语 |
| E2 | 两组明确列出的冗长功能短语 |
| E3 | 三组研究动作中可等价简化的轻动词结构 |
| E4 | 同一位置紧邻叠加的添加连接词 |
| E5 | 同一数值前重复的近似词 |
| E6 | 功能已完整说明、且不承载独立信息的装饰性职业拟人 |

每次修改必须满足对应规则的触发条件和例外要求。不确定时保留原文；不为增加修改量而改写。完整规则见 [English whitelist](paper-touch-en/references/english-rules.md)。

例如，以下只是编辑示例，不是研究结果：

```text
Before: We conducted an evaluation of the encoder on the test split.
After:  We evaluated the encoder on the test split.
```

数字、单位、公式、术语、引用、限定条件、阴性结果和研究完成状态属于保护内容。正常被动语态、必要长句、真实对比及专业术语重复都不作为改写理由。

## 安装

适用于支持本地 `SKILL.md` 技能的 AI 助手。以 Codex 为例：

1. 下载 [paper-touch-en.zip](https://github.com/ZXON-ZTX/PaperTouch/releases/latest/download/paper-touch-en.zip)。
2. 解压后，将整个 `paper-touch-en` 文件夹放入技能目录，例如 Windows 的 `%USERPROFILE%\.agents\skills\`。
3. 确认路径为 `%USERPROFILE%\.agents\skills\paper-touch-en\SKILL.md`。如果尚未出现在技能列表中，重启 Codex 后再试。

也可以克隆本仓库，将其中的 `paper-touch-en` 文件夹复制到技能目录。调用标识为 `$paper-touch-en`，展示名称为 PaperTouch。

## 使用

清理已有英文原稿：

```text
使用 $paper-touch-en 清理下面英文论文段落。
只按白名单修改，保留未命中文字、数字、公式、引用和原有结构。
只输出修改后的全文。

[粘贴英文原稿]
```

仅审核，不修改：

```text
使用 $paper-touch-en，仅审核、不改写。
列出命中的 E1–E6、原文位置及最小修改建议。

[粘贴英文原稿]
```

作者样本或风格指南可以随任务提供。默认只输出完整修改稿；没有明确命中时原样返回。

## 补丁工具与测试

技能附带 Python 3.10+ 补丁工具，用于将已审阅的编辑计划应用到 UTF-8 文本、Markdown 和 LaTeX。无第三方 Python 依赖，工具本身不调用 API、检测器或网络服务。

```text
cd paper-touch-en
python scripts/apply_edits.py draft.md --plan edits.json -o draft.cleaned.md
python -B -m unittest discover -s tests -v
```

输出必须是新文件。工具检查字面锚点、重叠、未改区域、部分受保护结构、数值及常见单位、否定/模态标记和常见引文；它不能判定规则是否真正适用或科学语义是否等价。列表和表格等已识别结构继续整行保护。识别不到的专业单位、引文和其他结构需要显式保护范围及人工复核。

当前随包包含 **19 项自动测试**，覆盖原有补丁行为、六条规则示例和保护修复。完整格式与限制见 [patch-format.md](paper-touch-en/references/patch-format.md)，历史验证与本次修复记录见 [验证记录](paper-touch-en/验证记录.md)。

## 适用边界

PaperTouch 用于已有英文成稿，不负责从零起草、中文改写、翻译、全面语法校对或重组论文。Word/PDF 需要相应文档工具及独立排版验证，不能直接输入上述补丁脚本。

六条规则是编辑白名单，不是作者身份或 AI 检测模型。没有英文大规模实证或检测器降分保证；中文来源中的语料频率不作为英文效果证据。AI 助手实际运行所需的账号和服务由使用者所在环境提供。

## 来源与许可

本英文版本改编自用户提供的 `lieflat-less-ai-tone` 中文技能，保留白名单、最小改动和信息守恒方法；英文规则独立列明。原始 Copyright (c) 2026 shiujan 和 [MIT 许可证](LICENSE) 保留。

完整来源说明、中文原始快照及文件哈希随仓库提供：[source-notes.md](paper-touch-en/references/source-notes.md)、[source-zh.md](paper-touch-en/references/source-zh.md)、[source-provenance.json](paper-touch-en/references/source-provenance.json)。
