#!/usr/bin/env python3
"""
Audio/Video transcription for Product Manager Skill.
Extracts speech-to-text from mp3, mp4, wav, m4a, mov, webm files.

Usage:
    python transcribe_media.py <file_path> [--model small]

Models: tiny, base, small (default), medium, large-v3
Smaller models are faster; larger models are more accurate for Chinese.

Output:
    Timestamped transcript in markdown format to stdout.

Requirements:
    - faster-whisper (pip install faster-whisper)
    - ffmpeg (system install)
"""

import sys
import os
from pathlib import Path


SUPPORTED_EXTENSIONS = {".mp3", ".mp4", ".wav", ".m4a", ".mov", ".webm", ".flac", ".ogg", ".avi", ".mkv"}
DEFAULT_MODEL = "small"


def transcribe(file_path: str, model_size: str = DEFAULT_MODEL) -> str:
    from faster_whisper import WhisperModel

    path = Path(file_path)
    if not path.exists():
        return f"错误：文件不存在 - {file_path}"

    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        return f"错误：不支持的格式 - {ext}\n支持格式：{', '.join(sorted(SUPPORTED_EXTENSIONS))}"

    try:
        model = WhisperModel(model_size, device="cpu", compute_type="int8")
        segments, info = model.transcribe(str(path), beam_size=5, language=None)

        lines = []
        lines.append(f"## 转录结果")
        lines.append(f"")
        lines.append(f"- 文件：{path.name}")
        lines.append(f"- 时长：{info.duration:.1f} 秒")
        lines.append(f"- 检测语言：{info.language}（置信度 {info.language_probability:.0%}）")
        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")

        full_text_parts = []
        for segment in segments:
            start_min = int(segment.start // 60)
            start_sec = int(segment.start % 60)
            timestamp = f"[{start_min:02d}:{start_sec:02d}]"
            text = segment.text.strip()
            lines.append(f"{timestamp} {text}")
            full_text_parts.append(text)

        lines.append(f"")
        lines.append(f"---")
        lines.append(f"")
        lines.append(f"## 全文（无时间戳）")
        lines.append(f"")
        lines.append(" ".join(full_text_parts))

        return "\n".join(lines)

    except Exception as e:
        return f"错误：转录失败 - {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python transcribe_media.py <文件路径> [--model small]")
        print(f"支持格式: {', '.join(sorted(SUPPORTED_EXTENSIONS))}")
        print("模型选择: tiny(最快), base, small(默认), medium, large-v3(最准)")
        sys.exit(1)

    file_path = sys.argv[1]
    model_size = DEFAULT_MODEL

    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model_size = sys.argv[idx + 1]

    result = transcribe(file_path, model_size)
    print(result)
