import time

def log_time(func):
    """A decorator to log the time taken by a method"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Translation took {end_time - start_time:.2f} seconds.")
        return result
    return wrapper

