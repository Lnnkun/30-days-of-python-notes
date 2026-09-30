"""把 Obsidian 里的 30 Days of Python 每日笔记导出到这个仓库。

用法：python sync.py
- 读取：笔记库 📂 Projects/3. 30 Days of Python/
  - DayNN_主题.md 单独文件
  - description.md 里 "### Day NN · ..." 小节
- 转换：[[双链]] → 纯文字，![[图片]] → ![](images/图片)，去掉 YAML 属性
- 输出：DayNN_主题.md、images/、README.md 目录
"""
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent
VAULT = REPO.parent / "Lnnk的第二大脑" / "Lnnk的第二大脑"
SRC = VAULT / "📂 Projects" / "3. 30 Days of Python"
ATTACH = VAULT / "Attachments"
IMAGES = REPO / "images"
COURSE = "https://github.com/Asabeneh/30-Days-Of-Python"


def link(name: str) -> str:
    return name.replace(" ", "%20")


def nav_line(days, n) -> str:
    """底部翻页：⬅️ 上一天 · 📚 目录 · 下一天 ➡️"""
    order = sorted(days)
    i = order.index(n)
    parts = []
    if i > 0:
        p = order[i - 1]
        parts.append(f"[⬅️ 上一天：Day {p} {days[p][0][len(f'Day{p:02d}_'):-3]}]({link(days[p][0])})")
    parts.append("[📚 目录](README.md)")
    if i < len(order) - 1:
        q = order[i + 1]
        parts.append(f"[下一天：Day {q} {days[q][0][len(f'Day{q:02d}_'):-3]} ➡️]({link(days[q][0])})")
    return " · ".join(parts)


def convert(text: str, nav: str = "") -> str:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)  # YAML 属性
    text = re.sub(r"^相关：.*\n?", "", text, flags=re.M)         # 换成自动生成的翻页

    def image(m):
        name = m.group(1).split("|")[0]
        src = ATTACH / name
        if src.exists():
            IMAGES.mkdir(exist_ok=True)
            shutil.copy2(src, IMAGES / name)
        return f"![{name}](images/{name.replace(' ', '%20')})"

    text = re.sub(r"!\[\[([^\]]+)\]\]", image, text)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)  # [[a|b]] → b
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)             # [[a]] → a
    text = re.sub(r"^所属：.*\n?", "", text, flags=re.M)         # 笔记库内部导航
    text = re.sub(r"^> 返回 .*\n?", "", text, flags=re.M)
    text = re.sub(r"(\n---\s*)+\Z", "", text.strip())             # 去掉末尾空分隔线
    if nav:
        text += f"\n\n---\n\n{nav}"
    return text.strip() + "\n"


def day_files():
    """返回 {天数: (文件名, 内容)}"""
    days = {}
    # 1) description.md 里的 "### Day NN · 标题" 小节
    desc = (SRC / "description.md").read_text(encoding="utf-8")
    pattern = r"^### Day (\d+) · (.+?)\n(.*?)(?=^### |^---\s*$|\Z)"
    for m in re.finditer(pattern, desc, flags=re.M | re.S):
        n, title, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        topic = re.sub(r"[（(].*", "", title).strip()
        body = re.sub(r"^#### ", "## ", body, flags=re.M)  # 小节升一级
        days[n] = (f"Day{n:02d}_{topic}.md", f"# Day {n} · {title}\n\n{body}")
    # 2) 单独的 DayNN_*.md 文件（优先）
    for f in SRC.glob("Day*.md"):
        m = re.match(r"Day\s*(\d+)[_ ]?(.*)", f.stem)
        if m:
            n = int(m.group(1))
            days[n] = (f"Day{n:02d}_{m.group(2) or 'notes'}.md", f.read_text(encoding="utf-8"))
    return days


def main():
    days = day_files()
    for old in REPO.glob("Day*.md"):
        old.unlink()
    rows = []
    for n in sorted(days):
        name, text = days[n]
        (REPO / name).write_text(convert(text, nav_line(days, n)), encoding="utf-8")
        topic = name[len(f"Day{n:02d}_"):-3]
        rows.append(f"| {n} | [{topic}]({link(name)}) |")
    readme = f"""# 🐍 30 Days of Python · 学习笔记

跟着 [Asabeneh / 30-Days-Of-Python]({COURSE}) 学 Python，每天分享一篇我自己的简要总结，希望对你有帮助。

**进度**：已完成 {max(days) if days else 0} / 30 天（从 Day {min(days) if days else '-'} 开始记录）

| Day | 主题 |
|---|---|
{chr(10).join(rows)}
"""
    (REPO / "README.md").write_text(readme, encoding="utf-8")
    print(f"导出 {len(days)} 天：", ", ".join(days[n][0] for n in sorted(days)))


if __name__ == "__main__":
    main()
