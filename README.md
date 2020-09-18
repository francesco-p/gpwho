![icon](https://i.imgur.com/ubOuPe3.png)

If you're a hardcore GPU user, and if you are competing with your collegues for the usage of lab's GPU, this tool is for you.

**gpwho???!!** is a GPU usage logger, with optional Telegram bot integration. It logs *who* is using the GPU and *when*.


# 1. Prerequisites

- GPU
- `python3.7+` - Not tested with other versions
- `sudo apt install gpustat` - Consult [gpustat](https://github.com/wookayin/gpustat) for other methods of installation.


# 2. Install

1. `git clone https://github.com/francesco-p/gpwho && cd gpwho`
2. `pip install -r requirements.txt`


# 3. Run

1. `python gpwho.py` - This script starts logging into `detailed_usage.csv` file. It measures the GPU usage every 20 seconds. You can alter this parameter directly inside the script.


# 4. Visualize

1. If you want a Telegram bot: 
    1. Ask a token to [@BotFather](https://telegram.me/BotFather) and put it inside `tgram.py`. 
    2. While `gpwho.py` is running open another terminal and run `python tgram.py`. 
    3. Start the newly created bot and visualize the status through the command `/status`.

2. If you do not want the bot:
    1. While `gpwho.py` is running open another terminal and run `python plot.py`. 
    2. Visualize the newly created `status.png` image.


# 5. Example

![bad_situation](https://i.imgur.com/CQuVCyA.png)
![bad_situation_tg](https://i.imgur.com/EvObjq1.png)


# Q/A

- Q. I have more than one gpu and I want to control let's say only the second one. How can I do it?
- A. You have to alter `main_regex` in `gpwho.py` file. In particular you can change the GPU id `r"\[1\] GeForce blabla...`. This tool has been developed for one GPU only but if you want to extend it to handle more than one GPUs make a pr!

- Q. You are awesome, how can I help you getting more GPUs?
- A. Thanks, if you feel that I'm particularly cool to you, just: 
<a href="https://www.buymeacoffee.com/lakj" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>