# LeetCode 158 – Read N Characters Given Read4 II

## Problem

Given an API `read4()` that reads up to 4 characters from a file, implement a function that reads **n characters**.

Unlike LeetCode 157, this version may call the `read()` function **multiple times**, so the characters read from `read4()` that are not immediately needed must be handled carefully.

---

## Approach

The basic idea is to repeatedly call `read4()` and copy only the required characters into `buf`.

For every call:

1. Create a temporary buffer of size 4.
2. Call `read4()`.
3. Check how many characters were actually read.
4. Copy only the required characters.
5. Stop when `n` characters are collected or the end of the file is reached.

The important part is that `read4()` may return **more characters than the current call needs**. Those extra characters would normally need to be saved for the next `read()` call.

---

## Example

Suppose the file contains:

```text
"abcdef"
```

First call:

```text
read(buf, 3)
```

The function reads:

```text
"abc"
```

and returns:

```text
3
```

A later call can continue reading from the remaining file contents.

---

## Key Difference from LeetCode 157

### Problem 157

The function is called only once.

### Problem 158

The function can be called multiple times.

Therefore, characters that are read but not used in the current call may need to be **stored and reused later**.

This is the main challenge of this problem.

---

## Key Concepts

* `read4()` API
* Buffer management
* Array manipulation
* String processing
* Handling multiple function calls
* Temporary storage
* End-of-file handling

---

## Complexity

### Time Complexity

**O(n)** for reading `n` characters.

### Space Complexity

**O(1)** extra space apart from the required buffer/storage.

---

## Important Points

* `read4()` reads at most 4 characters.
* The requested number `n` can be smaller or larger than 4.
* The file may contain fewer than `n` characters.
* Extra characters from `read4()` must not be lost between calls.
* The function should return the actual number of characters read.

---

## LeetCode Details

* **Problem Number:** 158
* **Problem Name:** Read N Characters Given Read4 II
* **Difficulty:** Hard
* **Language:** Python
* **Topic:** Array, String, Simulation

---

## What I Learned

This problem improves the understanding of **buffer management** and how data can be read in fixed-size chunks while the user may request a different number of characters.

The major difference from Problem 157 is handling repeated calls and making sure that unused characters are available for future calls.

---

# Author

T.Nandhini
