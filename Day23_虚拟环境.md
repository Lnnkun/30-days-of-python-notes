# Day 23 - 虚拟环境(Virtual Environment)

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'nodeSpacing': 8, 'rankSpacing': 40}}}%%
flowchart LR
  R(["Day 23 虚拟环境"])
  R --- b0["核心价值"]
  b0 --- n1["隔离不同项目的依赖"]
  b0 --- n2["避免版本冲突"]
  subgraph sn2[" "]
  n2 --- n3["同一个包，不同项目要不同版本"]
  n2 --- n4["共用环境会互相覆盖报错"]
  end
  style sn2 fill:none,stroke:none
  classDef c0 fill:none,stroke:#F5A623,stroke-width:2px,color:#F5A623,font-weight:bold
  class b0 c0
  R --- b1["virtualenv 工具"]
  b1 --- n5["不是项目依赖包"]
  b1 --- n6["是创建虚拟环境的专用工具"]
  b1 --- n7["pip install virtualenv 安装"]
  classDef c1 fill:none,stroke:#4A90E2,stroke-width:2px,color:#4A90E2,font-weight:bold
  class b1 c1
  R --- b2["创建虚拟环境"]
  b2 --- n8["virtualenv venv"]
  subgraph sn8[" "]
  n8 --- n9["在当前文件夹新建 venv 文件夹"]
  n8 --- n10["只是造好空间"]
  n8 --- n11["还没有进入使用"]
  end
  style sn8 fill:none,stroke:none
  classDef c2 fill:none,stroke:#2ECC71,stroke-width:2px,color:#2ECC71,font-weight:bold
  class b2 c2
  R --- b3["激活与退出"]
  b3 --- n12["activate"]
  subgraph sn12[" "]
  n12 --- n13["切换当前终端的 Python 环境"]
  n12 --- n14["切到独立隔离的 venv"]
  n12 --- n15["提示符前多出 (venv)"]
  end
  style sn12 fill:none,stroke:none
  b3 --- n16["deactivate"]
  subgraph sn16[" "]
  n16 --- n17["activate 的反向操作"]
  n16 --- n18["退出虚拟环境"]
  n16 --- n19["切回全局 Python 环境"]
  n16 --- n20["(venv) 标记消失"]
  end
  style sn16 fill:none,stroke:none
  classDef c3 fill:none,stroke:#A66CFF,stroke-width:2px,color:#A66CFF,font-weight:bold
  class b3 c3
  R --- b4["不上传 venv"]
  b4 --- n21["venv 体积大，内容可重新生成"]
  b4 --- n22["改为上传 requirements.txt"]
  subgraph sn22[" "]
  n22 --- n23["用 pip freeze 生成的依赖清单"]
  n22 --- n24["别人运行 pip install -r requirements.txt"]
  n22 --- n25["自动复刻一样的环境"]
  end
  style sn22 fill:none,stroke:none
  classDef c4 fill:none,stroke:#FF6B6B,stroke-width:2px,color:#FF6B6B,font-weight:bold
  class b4 c4
  classDef leaf fill:none,stroke:none,color:#9AA0A6
  classDef root fill:#5B5FC7,stroke:none,color:#fff,font-weight:bold
  class R root
  class n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25 leaf
  linkStyle 0 stroke:#F5A623,stroke-width:1.5px
  linkStyle 1 stroke:#F5A623,stroke-width:1.5px
  linkStyle 2 stroke:#F5A623,stroke-width:1.5px
  linkStyle 3 stroke:#F5A623,stroke-width:1.5px
  linkStyle 4 stroke:#F5A623,stroke-width:1.5px
  linkStyle 5 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 6 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 7 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 8 stroke:#4A90E2,stroke-width:1.5px
  linkStyle 9 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 10 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 11 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 12 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 13 stroke:#2ECC71,stroke-width:1.5px
  linkStyle 14 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 15 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 16 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 17 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 18 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 19 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 20 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 21 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 22 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 23 stroke:#A66CFF,stroke-width:1.5px
  linkStyle 24 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 25 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 26 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 27 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 28 stroke:#FF6B6B,stroke-width:1.5px
  linkStyle 29 stroke:#FF6B6B,stroke-width:1.5px
```

---

## 补充说明

### 1. 虚拟环境的核心价值
- 为每个项目创建**独立、隔离**的小环境
- 避免不同项目之间,因共用同一个Python环境而产生**版本冲突**(比如A项目要1.0版,B项目要2.0版,共用环境会互相覆盖)

### 2. virtualenv 工具
- `virtualenv` 本身**不是**某个项目要直接使用的功能包
- 它是一个专门用来"**创建虚拟环境**"的工具,通过 `pip install virtualenv` 安装

### 3. 创建虚拟环境
- `virtualenv venv`:在当前文件夹下,**新建**一个叫 `venv` 的文件夹
- 这一步只是"造好"独立环境的空间,人还**没有进入**使用

### 4. 激活(activate)与退出(deactivate)
| 命令 | 作用 |
|---|---|
| `source venv/bin/activate` | 把当前终端的Python环境,**切换**成这个独立隔离的虚拟环境;提示符前出现 `(venv)` |
| `deactivate` | `activate` 的反向操作,**退出**虚拟环境,切回电脑全局Python环境;`(venv)` 标记消失 |

### 5. 为什么不把 venv 上传到 GitHub
- `venv` 文件夹体积大,而且内容是"可以被重新生成"的
- 正确做法:上传一份轻量的 `requirements.txt`(用 `pip freeze` 生成的依赖清单)
- 别人拿到项目后,只需新建虚拟环境,运行 `pip install -r requirements.txt`,就能自动复刻出一模一样的环境,不用传输实际的包文件


---

[⬅️ 上一天：Day 22 网络爬虫](Day22_网络爬虫.md) · [📚 目录](README.md)
