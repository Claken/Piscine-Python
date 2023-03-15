from tqdm import tqdm

def ft_progress(listeuh):
    for i in tqdm(listeuh, desc="ETA: ", ascii=' >=', ncols=100):
        #yield i
        pass

if __name__ == "__main__":
    listeuh = range(int(9e6))
    ft_progress(listeuh)