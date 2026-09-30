# Day 20 - PIP Python包管理器

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 8, 'rankSpacing': 40}}}%%
flowchart LR
  R(["Day 20 PIP 包管理器"])
  R --- b0["包与模块"]
  classDef c0 fill:none,stroke:#F5A623,stroke-width:2px,color:#F5A623,font-weight:bold
  class b0 c0
  b0 --- n1["模块 module"]
  n1 --- n2["一个 Python 文件"]
  b0 --- n3["包 package"]
  n3 --- n4["一个文件夹"]
  n3 --- n5["可装多个模块"]
  n3 --- n6["层级比模块更高"]
  R --- b1["pip 基础操作"]
  classDef c1 fill:none,stroke:#4A90E2,stroke-width:2px,color:#4A90E2,font-weight:bold
  class b1 c1
  b1 --- n7["pip install"]
  n7 --- n8["下载安装到电脑"]
  n7 --- n9["只需装一次"]
  b1 --- n10["import"]
  n10 --- n11["每份要用的代码里都要写"]
  n10 --- n12["install 和 import 是两步"]
  b1 --- n13["pip uninstall"]
  n13 --- n14["卸载已安装的包"]
  b1 --- n15["pip list"]
  n15 --- n16["列出所有已安装的包"]
  n15 --- n17["给人看，方便自查"]
  b1 --- n18["pip show"]
  n18 --- n19["展示某个包的详细信息"]
  R --- b2["pip freeze"]
  classDef c2 fill:none,stroke:#2ECC71,stroke-width:2px,color:#2ECC71,font-weight:bold
  class b2 c2
  b2 --- n20["生成 包名==版本号 清单"]
  b2 --- n21["配合 requirements.txt"]
  b2 --- n22["复现一样的运行环境"]
  b2 --- n23["别人一次装好所有依赖"]
  R --- b3["requests 模块"]
  classDef c3 fill:none,stroke:#A66CFF,stroke-width:2px,color:#A66CFF,font-weight:bold
  class b3 c3
  b3 --- n24["requests.get(url)"]
  n24 --- n25["像网络版的 open()"]
  n24 --- n26["访问网址抓取数据"]
  b3 --- n27["response 对象"]
  n27 --- n28["status_code 状态码"]
  n28 --- n29["200 表示成功"]
  n28 --- n30["其他数字表示问题"]
  n27 --- n31[".text"]
  n31 --- n32["原始字符串"]
  n31 --- n33["要自己 json.loads() 解析"]
  n27 --- n34[".json()"]
  n34 --- n35["自动把字符串转成字典"]
  n34 --- n36["比 .text 多一步转换"]
  R --- b4["创建自己的包"]
  classDef c4 fill:none,stroke:#FF6B6B,stroke-width:2px,color:#FF6B6B,font-weight:bold
  class b4 c4
  b4 --- n37["文件夹 + __init__.py"]
  b4 --- n38["__init__.py 的作用"]
  n38 --- n39["给 Python 的信号标签"]
  n38 --- n40["空文件也算数"]
  n38 --- n41["让文件夹被识别为包"]
  n38 --- n42["之后才能 import"]
  classDef leaf fill:none,stroke:none,color:#9AA0A6
  classDef root fill:#5B5FC7,stroke:none,color:#fff,font-weight:bold
  class R root
  class n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,n41,n42 leaf
  linkStyle 0 stroke:#F5A623,stroke-width:1.5px
  linkStyle 1 stroke:#F5A623,stroke-width:1.5px
  linkStyle 2 stroke:#F5A623,stroke-width:1.5px
  linkStyle 3 stroke:#F5A623,stroke-width:1.5px
  linkStyle 4 stroke:#F5A623,stroke-width:1.5px
  linkStyle 5 stroke:#F5A623,stroke-width:1.5px
  linkStyle 6 stroke:#F5A623,stroke-width:1.5px
  linkStyle 7 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 8 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 9 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 10 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 11 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 12 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 13 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 14 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 15 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 16 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 17 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 18 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 19 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 20 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 21 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 22 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 23 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 24 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 25 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 26 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 27 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 28 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 29 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 30 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 31 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 32 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 33 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 34 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 35 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 36 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 37 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 38 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 39 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 40 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 41 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 42 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 43 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 44 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 45 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 46 stroke:#FF6B6B,stroke-width:1.5px
```

---

## 补充说明

### 1. 包(package) vs 模块(module)
- **模块**:一个Python文件
- **包**:一个文件夹,可以装一个或多个模块,层级比模块更高

### 2. pip install 与 import 的关系
- `pip install` 把包下载安装到电脑上(装一次即可)
- `import` 在每一份需要用到它的代码文件里引入(每次都要写)

### 3. pip 管理命令
| 命令 | 作用 |
|---|---|
| `pip uninstall` | 卸载已安装的包 |
| `pip list` | 列出所有已安装的包 |
| `pip show` | 展示某个特定包的详细信息 |

### 4. pip freeze
- 生成"包名==版本号"格式的清单
- 配合 `requirements.txt` 使用,方便别人一次性复现相同的运行环境

### 5. requests 模块
- `requests.get(url)`:像"网络版的 `open()`",访问网址并抓取数据
- `response.status_code`:状态码(200 = 成功,其他数字通常代表问题)
- `response.text`:返回原始字符串,需要自己手动用 `json.loads()` 解析
- `response.json()`:自动完成"字符串转字典"这一步,比 `.text` 多做了一步转换

### 6. 创建自己的包
- 新建一个文件夹 + 里面放一个空的 `__init__.py`
- `__init__.py` 的存在本身,就是给 Python 的"信号标签",让这个文件夹被识别为一个正式的包,之后才能用 `import` 来使用

---
相关：30 Days of Python · 上一天：Day19_文件处理 · 下一天：Day21_类和对象
