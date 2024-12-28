import sys

def ft_tqdm(lst: range) -> None:
    """
    Mimics the tqdm progress bar using the yield operator.
    :param lst: The list to iterate over.
    :return: None
    """
    total = len(lst)

    for idx, item in enumerate(lst, start=1):
        barlen = 50
        progress = idx / total
        num_full_bars = int(progress * barlen)
        bar = f"{'█' * num_full_bars}{' ' * (barlen - num_full_bars)}"

        sys.stdout.write(f"\r{progress * 100:6.0f}%|{bar}| {idx}/{total}")
        sys.stdout.flush()

        yield item
        
    sys.stdout.write("\n")
