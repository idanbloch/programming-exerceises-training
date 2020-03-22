import multiprocessing
from typing import Callable, Tuple
import numpy as np
import json
import time
import os

INPUTS_PATH = f'{os.getcwd()}\\inputs'


def get_input(problem_name: str, idx: int) -> Tuple:
    path = f'{INPUTS_PATH}\\{problem_name}\\test_{idx}.json'
    if f'test_{idx}.json' not in os.listdir(f'{INPUTS_PATH}\\{problem_name}'):
        raise FileNotFoundError('Test index does not exist')
    with open(path, 'r') as f:
        arguments = json.load(f)
    if not arguments['visible']:
        raise PermissionError('The requested test is not visible')
    return arguments['arguments']


def wrapper(func, desired_output, idx, *args, **kwargs):
    initial_time = time.time()
    output = func(*args, **kwargs)
    if desired_output == output:
        print(f'Well done! test #{idx} had been passed sucessfully.')
        print(f'Time required: {np.round(time.time() - initial_time, 2)} seconds.')
    else:
        print('Solution is incorrect.')


def test(problem_name: str, idx: int, solution: Callable) -> None:
    # Start bar as knapsack process
    try:
        path = f'{INPUTS_PATH}\\{problem_name}\\test_{idx}.json'
        with open(path, 'r') as f:
            data = json.load(f)
            arguments = data['arguments'].values()
            time_limit = data['time_limit']
            desired_output = data['desired_output']
    except:
        raise FileNotFoundError('Test index does not exist')
    p = multiprocessing.Process(target=wrapper, args=(solution, desired_output, idx, *arguments))
    print('Starting')
    p.start()

    # give the solution the given time to run
    p.join(time_limit)

    # If thread is still active
    if p.is_alive():
        print('Time limit exceeded. You can do better than that!')

        # Terminate
        p.terminate()
        p.join()
