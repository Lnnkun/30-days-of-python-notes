# Day 22 - 网络爬虫(Web Scraping)

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 8, 'rankSpacing': 40}}}%%
flowchart LR
  R(["Day 22 网络爬虫"])
  R --- b0["获取网页"]
  b0 --- n1["requests.get(url)"]
  n1 --- n2["访问网址"]
  b0 --- n3["response.content"]
  subgraph sn3[" "]
  n3 --- n4["拿到原始 HTML 文字"]
  n3 --- n5["标签套标签的结构"]
  end
  style sn3 fill:none,stroke:none
  classDef c0 fill:none,stroke:#F5A623,stroke-width:2px,color:#F5A623,font-weight:bold
  class b0 c0
  R --- b1["BeautifulSoup 解析"]
  b1 --- n6["BeautifulSoup(content, 'html.parser')"]
  subgraph sn6[" "]
  n6 --- n7["把杂乱 HTML 解析成有结构的对象"]
  n6 --- n8["之后能按标签、属性精准查找"]
  n6 --- n9["区别于正则的纯文字匹配"]
  end
  style sn6 fill:none,stroke:none
  classDef c1 fill:none,stroke:#4A90E2,stroke-width:2px,color:#4A90E2,font-weight:bold
  class b1 c1
  R --- b2["读取标签内容"]
  b2 --- n10["soup.title"]
  subgraph sn10[" "]
  n10 --- n11["整个标签本身"]
  n10 --- n12["带着尖括号的标签符号"]
  end
  style sn10 fill:none,stroke:none
  b2 --- n13["soup.title.get_text()"]
  subgraph sn13[" "]
  n13 --- n14["只要标签里的纯文字"]
  n13 --- n15["去掉标签外壳"]
  end
  style sn13 fill:none,stroke:none
  classDef c2 fill:none,stroke:#2ECC71,stroke-width:2px,color:#2ECC71,font-weight:bold
  class b2 c2
  R --- b3["find_all() 查找"]
  b3 --- n16["第 1 个参数：标签名"]
  subgraph sn16[" "]
  n16 --- n17["指定要找哪种 HTML 标签"]
  n16 --- n18["例如 table、div、a"]
  end
  style sn16 fill:none,stroke:none
  b3 --- n19["第 2 个参数：字典（可选）"]
  subgraph sn19[" "]
  n19 --- n20["进一步筛选"]
  n19 --- n21["某个属性等于指定值"]
  n19 --- n22["例如 cellpadding = 3"]
  end
  style sn19 fill:none,stroke:none
  classDef c3 fill:none,stroke:#A66CFF,stroke-width:2px,color:#A66CFF,font-weight:bold
  class b3 c3
  R --- b4["find() vs find_all()"]
  b4 --- n23["find() 单数"]
  n23 --- n24["只返回第一个匹配"]
  b4 --- n25["find_all() 复数"]
  n25 --- n26["返回所有匹配，打包成列表"]
  b4 --- n27["类似 re.search() 和 re.findall()"]
  classDef c4 fill:none,stroke:#FF6B6B,stroke-width:2px,color:#FF6B6B,font-weight:bold
  class b4 c4
  R --- b5["链式调用"]
  b5 --- n28["先缩小范围再继续查找"]
  b5 --- n29["table.find('tr').find_all('td')"]
  subgraph sn29[" "]
  n29 --- n30["先找表格第一行"]
  n29 --- n31["再找这一行里的每个格子"]
  end
  style sn29 fill:none,stroke:none
  b5 --- n32["逐步精确定位目标内容"]
  classDef c5 fill:none,stroke:#1ABC9C,stroke-width:2px,color:#1ABC9C,font-weight:bold
  class b5 c5
  classDef leaf fill:none,stroke:none,color:#9AA0A6
  classDef root fill:#5B5FC7,stroke:none,color:#fff,font-weight:bold
  class R root
  class n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32 leaf
  linkStyle 0 stroke:#F5A623,stroke-width:1.5px
  linkStyle 1 stroke:#F5A623,stroke-width:1.5px
  linkStyle 2 stroke:#F5A623,stroke-width:1.5px
  linkStyle 3 stroke:#F5A623,stroke-width:1.5px
  linkStyle 4 stroke:#F5A623,stroke-width:1.5px
  linkStyle 5 stroke:#F5A623,stroke-width:1.5px
  linkStyle 6 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 7 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 8 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 9 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 10 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 11 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 12 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 13 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 14 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 15 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 16 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 17 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 18 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 19 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 20 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 21 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 22 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 23 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 24 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 25 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 26 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 27 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 28 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 29 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 30 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 31 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 32 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 33 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 34 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 35 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 36 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 37 stroke:#1ABC9C,stroke-width:1.5px
```

---

## 补充说明

### 1. 获取网页原始内容
- `requests.get(url)`:访问网址,拿到服务器返回的数据
- `response.content`:网页的原始HTML文字(标签套标签的结构)

### 2. BeautifulSoup 解析
- `BeautifulSoup(content, 'html.parser')`:把杂乱的HTML文字,解析成一个有"层级结构"的对象
- 之后可以按标签名、属性,精准定位内容,而不是像正则表达式那样对纯文字做模式匹配

### 3. 标签 vs 纯文字
- `soup.title`:拿到整个标签(包含 `<title>` 和 `</title>` 符号本身)
- `soup.title.get_text()`:只拿标签里面包裹的纯文字内容

### 4. find_all() 的两个参数
| 参数 | 作用 |
|---|---|
| 第一个(字符串) | 指定要找哪种HTML标签(如 `table`、`div`、`a`) |
| 第二个(字典,可选) | 进一步筛选,要求该标签的某个属性等于指定值(如 `{'cellpadding': '3'}`) |

### 5. find() vs find_all()
- `find()`(单数):只返回**第一个**匹配的标签
- `find_all()`(复数):返回**所有**匹配的标签,打包成列表
- 与 Day18 的 `re.search()`(只返回第一个)和 `re.findall()`(返回所有)是同一种设计思路

### 6. 链式调用,逐步缩小范围
- 例:`table.find('tr').find_all('td')`
  1. 先用 `find('tr')` 找到表格的**第一行**
  2. 再用 `find_all('td')` 找出这一行里的**每一个格子**
- 这种"先定位大范围,再在范围内继续查找"的写法,是 BeautifulSoup 常见的用法


---

[⬅️ 上一天：Day 21 类和对象](Day21_类和对象.md) · [📚 目录](README.md)
