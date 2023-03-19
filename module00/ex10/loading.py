from tqdm import tqdm
from time import sleep

def ft_progress(listeuh):
    for i in tqdm(listeuh, desc="ETA: ", ascii=' >=', ncols=100):
        yield i
        pass

if __name__ == "__main__":
    listeuh = range(1000)
    ret = 0
    for elem in ft_progress(listeuh):
        ret += (elem + 3) % 5
        sleep(0.001)
    print()
    print(ret)