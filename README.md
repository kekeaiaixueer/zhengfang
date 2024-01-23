正方教务系统成绩获取
## 使用方法

### 1. [Fork](https://github.com/kekeaiaixueer/zhengfang/fork "Fork") 本仓库

`Fork` → `Create fork`

### 2. [开启](https://github.com/kekeaiaixueer/zhengfang/settings/actions "开启")工作流读写权限

`Settings` → `Actions` → `General` → `Workflow permissions` →`Read and write permissions` →`Save`

### 3. [添加](https://github.com/kekeaiaixueer/zhengfang/settings/secrets/actions "添加") Secrets

`Settings` → `Secrets and variables` → `Actions` → `Secrets` → `Repository secrets` → `New repository secret`

> Name = Name，Secret = 例子

| Name     | 例子                       | 说明                                                                                                                 |
| -------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| URL      | https://www.nianbroken.top | 教务系统地址                                                                                                          |
| USERNAME | 2971802058                 | 教务系统用户名                                                                                                        |
| PASSWORD | Y3xhaCkb5PZ4               | 教务系统密码                                                                                                          |
|   YEAR   | 2023-2024                  | 学年                                                                                                                 |
|   TERM   | 1                          | 学期                                                                                                                 |
|   TOKEN  | J65KWMBfyDh3YPLpcvm8       | [Pushplus 的 token](https://www.pushplus.plus/doc/guide/openApi.html#_1-%E8%8E%B7%E5%8F%96token "Pushplus 的 token") |

### 4. [开启](https://github.com/kekeaiaixueer/zhengfang/actions "开启") Actions

`Actions` → `I understand my workflows, go ahead and enable them` → `CheckScores` → `Enable workflow`

### 5. [运行](https://github.com/kekeaiaixueer/zhengfang/actions/workflows/main.yml "运行")程序

`Actions` → `CheckScores` → `Run workflow`

_若你的程序正常运行且未报错，那么在此之后，程序将会每隔 30 分钟自动运行一次_

