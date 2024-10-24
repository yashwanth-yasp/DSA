def max_palindromes(arr):
  """
  Finds the maximum number of palindromic strings obtainable in an array through swaps.

  Args:
      arr: An array of strings containing lowercase English characters.

  Returns:
      The maximum number of palindromes achievable through swaps.
  """
  
  def swap_first_chars(s1, s2):
    """
    Checks if swapping first characters creates a palindrome.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        True if swapping creates a palindrome, False otherwise.
    """
    return s1[0] == s2[-1]

  def is_palindrome(s):
    """
    Checks if a string is a palindrome.

    Args:
        s: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1
    while left < right:
      if s[left] != s[right]:
        return False
      left += 1
      right -= 1
    return True
  pal_count = 0
  for s in arr:
    if is_palindrome(s):
      pal_count += 1

  swappable_pairs = []
  n = len(arr)
  for i in range(n):
    for j in range(i + 1, n):
      # Check swap at first character
      if swap_first_chars(arr[i], arr[j]):
        swappable_pairs.append((i, j))

      # Check swap at last character (reverse the check)
      if swap_first_chars(arr[j][::-1], arr[i]):
        swappable_pairs.append((i, j))

  

  # Sort swappable pairs based on heuristic
  swappable_pairs.sort(key=lambda pair: (arr[pair[0]][0] == arr[pair[1]][-1] or abs(len(arr[pair[0]]) - len(arr[pair[1]])) < 2), reverse=True)

  max_palindromes = pal_count
  for i, j in swappable_pairs:
    temp_s1, temp_s2 = arr[i], arr[j]
    arr[i], arr[j] = arr[j][::-1], arr[i][::-1]  # Swap characters for simulation
    if is_palindrome(arr[i]) and is_palindrome(arr[j]):
      max_palindromes += 2
    else:
      arr[i], arr[j] = temp_s1, temp_s2  # Undo swap if not successful

  return max_palindromes

# Example usage
arr = ["pass", "sas", "asps", "df"]
max_pals = max_palindromes(arr)
print(f"Maximum palindromes achievable: {max_pals}")
