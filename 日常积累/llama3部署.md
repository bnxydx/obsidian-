# llama3部署



- 在docker中创建一个ubuntu
- **记得设置内网穿透，不然外边访问不了**
- 更新系统软件包列表

~~~
apt-get update
~~~

- 下载wget

~~~
apt-get install wget
~~~

- 下载git

~~~
apt-get install git
~~~

- 安装一个轻量级的conda

~~~
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh
~~~

- 这里可能输回车，也可能yes

- 输入环境变量

~~~
vim .bashrc
# Add Miniconda to PATH (for bash)
export PATH="/root/miniconda3/bin:$PATH"
~~~

~~~
vim .profile
# Add Miniconda to PATH (for non-bash shells)
export PATH="/root/miniconda3/bin:$PATH"
~~~

# 激活

~~~
source ~/.bashrc   # For bash users
source ~/.profile # For non-bash users
~~~



# 初始化 激活

~~~
conda init
~~~

~~~
conda create --name llama_factory python=3.11
~~~

~~~
conda activate llama_factory
~~~

# 克隆

~~~
cd ai-text
git clone https://gitee.com/bnxydx/LLaMA-Factory.git
cd ~/ai-test/LLaMA-Factory
~~~

# 升级pip

~~~
python -m pip install --upgrade pip
~~~

~~~
pip install -r requirements.txt --index-url https://mirrors.huaweicloud.com/repository/pypi/simple
~~~

# 要是一直下载不下来，得删一下缓存

~~~
pip cache info
pip cache list
pip cache remove 包名
pip cache purge #清空缓存
~~~

- 受不了了，一直下载不下来

# 下载模型

~~~
mkdir model 存放模型文件
cd model
git clone https://www.modelscope.cn/LLM-Research/Meta-Llama-3-8B-Instruct.git
~~~

# 准备启动

~~~
cd ~/ai-test/LLaMA-Factory
~~~

~~~
CUDA_VISIBLE_DEVICES=0  python src/webui.py \
    --model_name_or_path /root/ai-text/model/Meta-Llama-3-8B-Instruct\
    --template llama3 \
    --infer_backend vllm \
    --vllm_enforce_eager
~~~







# 本地端部署

- 主要是使用ollama

https://www.ddhigh.com/2024/04/20/%E8%B6%85%E8%B6%8Agpt-3.5llama3%E4%B8%AA%E4%BA%BA%E7%94%B5%E8%84%91%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2%E6%95%99%E7%A8%8B/

- 第二次启动

- ~~~
	cd Windows/System33
	cmd
	ollama run llama3
	~~~



# 本地端可视化

https://www.bilibili.com/video/BV1nt421g79T/?spm_id_from=333.880.my_history.page.click&vd_source=088c1e78206ad2b55500662df5f6652f

https://github.com/CrazyBoyM/llama3-Chinese-chat