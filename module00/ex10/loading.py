from tqdm import tqdm
from time import sleep


def ft_progress(listeuh):
    for i in tqdm(listeuh, desc="ETA: ", ascii=' >=',
                  ncols=90, bar_format="\
{desc}{remaining_s:.2f}s [{percentage:3.0f}%][{bar}] \
{n_fmt}/{total_fmt} | elapsed time {elapsed_s:.2f}s"):
        yield i
        pass


if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
