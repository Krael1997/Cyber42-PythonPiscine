import time

def ft_progress(lst):
    length = len(lst)
    start_time = time.time()
    for i, item in enumerate(lst):
        yield item
        elapsed_time = time.time() - start_time
        progress = i / length
        eta = int(elapsed_time / progress - elapsed_time) if progress > 0 else 0
        bar = '=' * int(30 * progress) + '>' + '-' * (30 - int(30 * progress))
        print(f"ETA: {eta}s [{int(progress * 100):>3}%][{bar}] {i+1}/{length} | elapsed time {elapsed_time:.2f}s", end='\r')

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
