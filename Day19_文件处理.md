# Day 19 - 文件处理(File Handling)

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 8, 'rankSpacing': 40}}}%%
flowchart LR
  R(["Day 19 文件处理"])
  R --- b0["open() 打开文件"]
  classDef c0 fill:none,stroke:#F5A623,stroke-width:2px,color:#F5A623,font-weight:bold
  class b0 c0
  b0 --- n1["open 返回文件对象"]
  n1 --- n2["像遥控器，用来操作文件"]
  n1 --- n3["print(f) 只显示文件信息"]
  n3 --- n4["不是文件内容本身"]
  R --- b1["三种读取方式"]
  classDef c1 fill:none,stroke:#4A90E2,stroke-width:2px,color:#4A90E2,font-weight:bold
  class b1 c1
  b1 --- n5["read() 全部内容"]
  n5 --- n6["返回一整个字符串"]
  b1 --- n7["readline() 只读一行"]
  n7 --- n8["只读第一行"]
  n7 --- n9["返回字符串"]
  b1 --- n10["readlines() 所有行"]
  n10 --- n11["按行拆开"]
  n10 --- n12["返回列表"]
  R --- b2["with 语句"]
  classDef c2 fill:none,stroke:#2ECC71,stroke-width:2px,color:#2ECC71,font-weight:bold
  class b2 c2
  b2 --- n13["自动关闭文件"]
  n13 --- n14["代码块结束自动 close"]
  n13 --- n15["不用手动写 close"]
  n13 --- n16["更安全，不容易忘记"]
  R --- b3["写入模式对比"]
  classDef c3 fill:none,stroke:#A66CFF,stroke-width:2px,color:#A66CFF,font-weight:bold
  class b3 c3
  b3 --- n17["'a' 追加模式"]
  n17 --- n18["保留原内容"]
  n17 --- n19["新增写到末尾"]
  n17 --- n20["像排队排到最后"]
  b3 --- n21["'w' 写入模式"]
  n21 --- n22["清空原内容"]
  n21 --- n23["覆盖重写"]
  n21 --- n24["像解散重排队伍"]
  R --- b4["删除文件"]
  classDef c4 fill:none,stroke:#FF6B6B,stroke-width:2px,color:#FF6B6B,font-weight:bold
  class b4 c4
  b4 --- n25["os 模块"]
  n25 --- n26["操作系统层面管理文件"]
  n25 --- n27["区别于 open 处理内容"]
  b4 --- n28["os.remove() 删除"]
  b4 --- n29["os.path.exists() 先检查"]
  n29 --- n30["避免删除不存在的文件报错"]
  R --- b5["JSON 处理"]
  classDef c5 fill:none,stroke:#1ABC9C,stroke-width:2px,color:#1ABC9C,font-weight:bold
  class b5 c5
  b5 --- n31["JSON 本质"]
  n31 --- n32["字符串格式"]
  n31 --- n33["跨语言、跨程序通用"]
  b5 --- n34["json.loads()"]
  n34 --- n35["字符串 → 字典"]
  n34 --- n36["load 进来解析"]
  b5 --- n37["json.dumps()"]
  n37 --- n38["字典 → 字符串"]
  n37 --- n39["返回类型是 str"]
  b5 --- n40["json.dump() 不带 s"]
  n40 --- n41["直接写入文件"]
  n40 --- n42["不返回字符串"]
  n40 --- n43["转换 + 写入一步完成"]
  classDef leaf fill:none,stroke:none,color:#9AA0A6
  classDef root fill:#5B5FC7,stroke:none,color:#fff,font-weight:bold
  class R root
  class n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30,n31,n32,n33,n34,n35,n36,n37,n38,n39,n40,n41,n42,n43 leaf
  linkStyle 0 stroke:#F5A623,stroke-width:1.5px
  linkStyle 1 stroke:#F5A623,stroke-width:1.5px
  linkStyle 2 stroke:#F5A623,stroke-width:1.5px
  linkStyle 3 stroke:#F5A623,stroke-width:1.5px
  linkStyle 4 stroke:#F5A623,stroke-width:1.5px
  linkStyle 5 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 6 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 7 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 8 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 9 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 10 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 11 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 12 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 13 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 14 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 15 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 16 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 17 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 18 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 19 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 20 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 21 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 22 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 23 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 24 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 25 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 26 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 27 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 28 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 29 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 30 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 31 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 32 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 33 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 34 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 35 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 36 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 37 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 38 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 39 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 40 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 41 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 42 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 43 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 44 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 45 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 46 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 47 stroke:#1ABC9C,stroke-width:1.5px
  linkStyle 48 stroke:#1ABC9C,stroke-width:1.5px
```

---

## 文字版补充说明

### 1. open() 打开文件
- `open()` 返回的是一个**文件对象**(不是文件内容),相当于"操作文件的遥控器"
- `print(f)` 只会显示这个对象的元信息(路径、模式、编码),不是文件文字

### 2. 三种读取方式
| 方法 | 读取范围 | 返回类型 |
|---|---|---|
| `read()` | 全部内容 | 字符串 |
| `readline()` | 只有第一行 | 字符串 |
| `readlines()` | 所有行 | 列表(按行拆分) |

### 3. with 语句
- 离开缩进代码块后,自动关闭文件,不需要手动写 `f.close()`

### 4. 'a' vs 'w'
- **`'a'`(追加)**:保留原内容,新增写到文件末尾
- **`'w'`(写入)**:清空原内容,覆盖重写

### 5. 删除文件
- 用 `os` 模块(操作系统层面的文件管理),不是 `open()`
- 先用 `os.path.exists()` 检查文件是否存在,再决定要不要 `os.remove()`,避免报错

### 6. JSON 的本质
- JSON 是**字符串格式**,不属于任何具体语言,用于不同程序/语言间传递数据

### 7. loads / dumps / dump
| 函数 | 方向 | 结果 |
|---|---|---|
| `json.loads()` | 字符串 → 字典 | 返回字典 |
| `json.dumps()` | 字典 → 字符串 | 返回字符串 |
| `json.dump()` | 字典 → 文件 | 直接写入文件,不返回字符串 |
