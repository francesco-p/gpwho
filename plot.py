import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


def main():
    plt.xkcd()
    df = pd.read_csv("./detailed_usage.csv", sep=',', header=None)
    df.columns = ['user', 'usage', 'total', 'max', 'timestamp']
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 13) )
    sns.lineplot(x='timestamp', y='usage', hue='user', data=df, ax=ax)
    ax.xaxis.set_major_locator(mdates.HourLocator(interval = 1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d-%H:%M'))
    ax.set_title("Main GPU Usage", fontsize=35)
    ax.set_xlabel("Timestamp", fontsize=35)
    ax.set_ylabel("Memory Usage (MB)", fontsize=35)
    ax.set_ylim(0, df.iloc[0]['max'])
    ax.tick_params(axis='x', rotation=40)
    plt.grid()
    plt.savefig("status.png")
    plt.close('all')


if __name__ == "__main__":
    main()