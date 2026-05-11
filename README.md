# Product Manager Skill

> 资深产品经理 AI Skill，通过结构化对话引导一线业务人员梳理需求，输出标准 PRD 文档。

## 它能做什么

- 扮演资深PM角色，通过引导式对话从业务人员口中挖出真实需求
- 主动挑战不合理需求（功能太多、逻辑矛盾、优先级缺失等）
- 支持多种素材输入（Word/Excel/PPT/PDF/图片/URL/录音/录屏）
- 最终输出标准化的产品需求文档（PRD）

## 兼容平台

| 平台 | 支持 | 安装方式 |
|------|------|----------|
| Claude Code | ✅ | `npx skills add NicZhang/product-manager-skill` |
| Codex (OpenAI CLI) | ✅ | `codex install NicZhang/product-manager-skill` |

## 安装

### Claude Code

```bash
npx skills add NicZhang/product-manager-skill
```

或手动克隆：

```bash
git clone https://github.com/NicZhang/product-manager-skill.git ~/.claude/skills/product-manager-skill
```

### Codex

```bash
codex install NicZhang/product-manager-skill
```

或手动克隆：

```bash
git clone https://github.com/NicZhang/product-manager-skill.git ~/.codex/plugins/product-manager-skill
```

### 依赖安装

音视频转录功能需要安装 Python 依赖：

```bash
pip install -r scripts/requirements.txt
```

同时需要系统安装 [ffmpeg](https://ffmpeg.org/)（音视频转录需要）。

## 使用

在 Claude Code 或 Codex 中直接说：

```
帮我梳理一个需求
我想做一个XX功能
帮我写个PRD
```

或者发送文件：

```
[发送 Word/Excel/PPT/PDF/录音/录屏文件]
帮我从这个文件里提取需求
```

## 三种工作模式

| 模式 | 适用场景 |
|------|---------|
| **引导模式** | 想法还模糊，需要从零梳理 |
| **倾倒模式** | 已有大量信息，先倾倒再整理 |
| **审查模式** | 已有初版文档，需要PM审查挑战 |

## 工作流程

```
Phase 0: 选择模式
    ↓
Phase 1: 问题与背景（WHY） → Checkpoint 确认
    ↓
Phase 2: 用户与场景（WHO） → Checkpoint 确认
    ↓
Phase 3: 方案与功能（WHAT） → Checkpoint 确认
    ↓
Phase 4: 生成PRD → 质量自检 → 交付
```

每个阶段结束有检查点确认，确保理解正确再继续。

## 支持的输入格式

| 类型 | 格式 |
|------|------|
| 文档 | .docx, .xlsx, .pptx, .pdf |
| 图片 | .png, .jpg, .jpeg |
| 音频 | .mp3, .wav, .m4a, .flac, .ogg |
| 视频 | .mp4, .mov, .webm, .avi, .mkv |
| 链接 | 任意 URL |

## 项目结构

```
product-manager-skill/
├── .claude-plugin/           # Claude Code 插件入口
│   ├── plugin.json
│   └── marketplace.json
├── .codex-plugin/            # Codex 插件入口
│   └── plugin.json
├── commands/
│   └── product-manager.md    # 命令入口（引用 SKILL.md）
├── SKILL.md                  # 主逻辑：引导协议 + 工作流 + PM判断逻辑
├── references/
│   ├── question-bank.md      # 各阶段问题库（含追问策略）
│   └── prd-template.md       # PRD输出模板
├── scripts/
│   ├── parse_document.py     # 文档解析（docx/xlsx/pptx → 结构化文本）
│   ├── transcribe_media.py   # 音视频转录（mp3/mp4等 → 带时间戳文本）
│   └── requirements.txt      # Python 依赖
├── README.md
└── LICENSE
```

## 许可证

[MIT](LICENSE)
