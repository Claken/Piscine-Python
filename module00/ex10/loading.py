from tqdm import tqdm
from time import sleep

def ft_progress(listeuh):
    for i in tqdm(listeuh, desc="ETA: ", ascii=' >=', ncols=90, bar_format="{desc}{remaining_s:.2f}s [{percentage:3.0f}%][{bar}] {n_fmt}/{total_fmt} | elapsed time {elapsed_s:.2f}s"):
        yield i
        pass

if __name__ == "__main__":
    listeuh = range(1000)
    ret = 0
    for elem in ft_progress(listeuh):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)