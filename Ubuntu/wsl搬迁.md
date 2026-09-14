### 第一阶段：先安装到 C 盘

**1.通过浏览器手动下载官方 Ubuntu 20.04 安装包:**避开网络报错.

在 Windows 浏览器（Edge 或 Chrome）中直接打开以下微软官方下载链接：

👉 [https://aka.ms/wslubuntu2004](https://aka.ms/wslubuntu2004)

浏览器会自动下载一个名为 `Ubuntu_2004.2021.825.0_x64.appx`（或类似命名的 `.appx` 文件，约 500MB）。

**2.双击安装并初始化用户名:**安装到 C 盘.

1. 下载完成后，在 Windows 文件资源管理器中找到该文件，**直接双击运行**，点击弹窗中的“安装”（它会默认安装到 C 盘的应用目录下）。
    
2. 安装完毕后会自动弹出一个黑色的终端窗口，提示：
    

Plaintext

```
Installing, this may take a few minutes...
Enter new UNIX username: 
```

3. 按提示输入你想要的普通用户名和密码（输入密码时光标不会动，输完直接回车）。
    
4. 看到命令提示符出现后，输入 `exit` 退出该窗口。
    

> **验证此步**：在 PowerShell 中输入 `wsl -l -v`，能看到列表中多了一项 `Ubuntu-20.04`，状态为 `Stopped`。



---

针对目标路径 **`F:\wsl-ubantu20.04`** 和用户 **`xyx`**，请在 Windows **PowerShell** 中按顺序依次执行以下命令：

### 搬迁到 `F:\wsl-ubantu20.04` 的完整命令

**1.退出 Ubuntu 并关闭 WSL 服务:**避免文件占用.

如果你还在 Ubuntu 终端里，先输入 `exit` 退出。然后在 **PowerShell** 中执行：

PowerShell

```
wsl --shutdown
```

**2.在 F 盘建立指定文件夹:**创建目标路径.

PowerShell

```
New-Item -ItemType Directory -Path "F:\wsl-ubantu20.04" -Force
```

**3.将当前实例导出到 F 盘临时文件:**数据打包.

PowerShell

```
wsl --export Ubuntu "F:\wsl-ubantu20.04\ubuntu_temp.tar"
```

_(光标会闪烁数十秒，等待下一行命令提示符出现即可)_

**4.注销 C 盘原实例:**释放 C 盘.

PowerShell

```
wsl --unregister Ubuntu
```

**5.将系统重新导入到目标文件夹:**落地 F 盘.

PowerShell

```
wsl --import Ubuntu-20.04 "F:\wsl-ubantu20.04" "F:\wsl-ubantu20.04\ubuntu_temp.tar" --version 2
```

导入成功后，清理临时打包文件：

PowerShell

```
Remove-Item "F:\wsl-ubantu20.04\ubuntu_temp.tar"
```

**6.将默认登录身份恢复为 xyx:**用户恢复.

PowerShell

```
wsl -d Ubuntu-20.04 -u root bash -c "echo -e '[user]\ndefault=xyx' >> /etc/wsl.conf"
wsl --shutdown
```

### 验证搬迁是否成功

在 PowerShell 中直接启动系统：

PowerShell

```
wsl -d Ubuntu-20.04
```

**验证判断**：

1. 提示符开头应为 **`xyx@...`**。
    
2. 打开 Windows 文件资源管理器进入 **`F:\wsl-ubantu20.04`**，能看到生成的虚拟磁盘文件 **`ext4.vhdx`**。
    

进入系统后，即可直接运行 ROS 1 安装脚本。