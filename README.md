# DSA @ Boot.dev

A hands-on Data Structures and Algorithms repository, structured as coursework for the [Boot.dev](https://boot.dev) platform. All problems are themed around **LockedIn**, a fictional influencer marketing platform.

> **Status:** In progress. Red-Black Tree insert and rotation are partially implemented.

## Tech Stack

- **Python 3.13**
- **uv** (package manager)
- No external dependencies — pure stdlib only

## Getting Started

```bash
# Clone the repo
git clone <repo-url>
cd dsa@boot/algorithms

# Create and activate the virtual environment
uv venv
source .venv/bin/activate

# Run any test file directly
python algorithm-intro/find_min_test.py
python Sorting-Algorithms/bubble_sort_test.py
python Binary-Trees/insert_nodes_test.py
```

Each module has a corresponding `*_test.py` file. Run it as a script to see test results. Many tests print input, expected, and actual values with pass/fail status.

Some tests include **performance checks** with timeout thresholds to verify time complexity requirements.

## Project Structure

```
algorithms/
├── algorithm-intro/        # Linear scan, summation
├── Data-Structures-Intro/  # Intro to lists and counting
├── Math/                   # Factorials, exponents, logarithms, mean/median
├── Big-O-Analysis/         # O(1), O(n), O(log n), O(n²), O(n·m)
├── Exponential-Time/       # O(2ⁿ), O(kⁿ), Fibonacci optimization
├── Stacks/                 # Stack class, balanced parentheses
├── Queues/                 # Queue class, matchmaking simulation
├── Linked-list/            # Node, LinkedList, LLQueue
├── Sorting-Algorithms/     # Bubble, selection, insertion, merge, quick sort
├── Binary-Trees/           # BST: insert, delete, traversals, min/max, height
├── Redblack-Trees/         # RBTree: insert, rotate_left (in progress)
├── images/                 # Test output screenshots
├── main.py                 # Scratch file
└── pyproject.toml
```

## Topics Covered

### Data Structures
| Structure | File | Operations |
|---|---|---|
| Stack | `Stacks/` | push, pop, peek, size |
| Queue | `Queues/` | push, pop, peek, size, search_and_remove |
| Linked List | `Linked-list/` | Node, iteration, O(1) add to head/tail |
| Linked List Queue | `Linked-list/queue_by_LinkedList.py` | remove_from_head, add_to_tail |
| Binary Search Tree | `Binary-Trees/` | insert, delete, traversals (pre/in/post), min, max, exists, height |
| Red-Black Tree | `Redblack-Trees/` | insert, rotate_left *(rotate_right pending)* |

### Algorithms
| Algorithm | File | Complexity |
|---|---|---|
| Find Minimum | `algorithm-intro/find_min.py` | O(n) |
| Sum List | `algorithm-intro/sum_nums.py` | O(n) |
| Binary Search | `Big-O-Analysis/order_logn.py` | O(log n) |
| Bubble Sort | `Sorting-Algorithms/bubble_sort.py` | O(n²) |
| Selection Sort | `Sorting-Algorithms/selection_sort.py` | O(n²) |
| Insertion Sort | `Sorting-Algorithms/insertion_sort.py` | O(n²) |
| Merge Sort | `Sorting-Algorithms/merge_sort.py` | O(n log n) |
| Quick Sort | `Sorting-Algorithms/quick_sort.py` | O(n log n) avg |
| Balanced Parentheses | `Stacks/using_stack.py` | O(n) |
| Fibonacci (optimized) | `Exponential-Time/reduction_toP.py` | O(n) |
| Phone Combinations | `Exponential-Time/order_kton.py` | O(kⁿ) |

### Math
- Factorials, exponents, exponential growth & decay
- Logarithms, logarithmic scaling
- Mean calculation

## Complexity Classes

| Class | Example | Where |
|---|---|---|
| O(1) | Dictionary lookup | `Big-O-Analysis/order_one.py` |
| O(n) | Linear scan | `algorithm-intro/` |
| O(log n) | Binary search | `Big-O-Analysis/order_logn.py` |
| O(n²) | Nested loops, simple sorts | `Big-O-Analysis/ordern_squared.py` |
| O(n·m) | Two independent collections | `Big-O-Analysis/order_nm.py` |
| O(kⁿ) | Exponential combinations | `Exponential-Time/order_kton.py` |
| O(n log n) | Merge/Quick sort | `Sorting-Algorithms/` |

## Testing

Tests are hand-rolled (no pytest/unittest). Each `*_test.py` file contains:

- **`run_cases`** — quick subset for local feedback
- **`submit_cases`** — full suite with edge cases
- A `test()` function comparing expected vs actual
- Some tests enforce **timing thresholds** to validate algorithmic complexity

Run any test directly:

```bash
python <topic>/<module>_test.py
```
