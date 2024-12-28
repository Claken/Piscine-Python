import sys

def ft_tqdm(lst: range) -> None:
    """
    Mimics the tqdm progress bar using the yield operator.
	
    """
    total = len(lst)  # Total number of elements in the iterable

    for idx, item in enumerate(lst, start=1):
        barlen = 50
        progress = idx / total
        num_full_bar = int(progress * barlen)
        bar = f"{'█' * num_full_bar}{' ' * (barlen - num_full_bar)}"

        sys.stdout.write(f"\r{progress * 100:6.0f}%|{bar}| {idx}/{total}")
        sys.stdout.flush()

        yield item

    # Finalize the progress bar with a newline
    sys.stdout.write("\n")
