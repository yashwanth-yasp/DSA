bool isPalindrome(const string &s) {
    int left = 0;
    int right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int countPalindromes(const vector<string> &arr) {
    int count = 0;
    for (const auto &s : arr) {
        if (isPalindrome(s)) {
            count++;
        }
    }
    return count;
}

unordered_map<char, int> countFrequency(const string &s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    return freq;
}

int countPalindromes(vector<string> arr) {
    int n = arr.size();
    vector<int> nonPalindromicIndices;
    unordered_map<char, int> globalFreq;
    int initialPalindromes = 0;

    for (int i = 0; i < n; i++) {
        unordered_map<char, int> freq = countFrequency(arr[i]);
        for (const auto &entry : freq) {
            globalFreq[entry.first] += entry.second;
        }
        if (!isPalindrome(arr[i])) {
            nonPalindromicIndices.push_back(i);
        } else {
            initialPalindromes++;
        }
    }

    auto canFormPalindrome = [&](const unordered_map<char, int> &freq) {
        int oddCount = 0;
        for (const auto &entry : freq) {
            if (entry.second % 2 != 0) {
                oddCount++;
            }
        }
        return oddCount <= 1;
    };

    for (int x : nonPalindromicIndices) {
        unordered_map<char, int> freqX = countFrequency(arr[x]);
        if (canFormPalindrome(freqX)) {
            initialPalindromes++;
            continue;
        }

        for (int y : nonPalindromicIndices) {
            if (x == y) continue;
            unordered_map<char, int> freqY = countFrequency(arr[y]);

            for (int i = 0; i < arr[x].length(); i++) {
                for (int j = 0; j < arr[y].length(); j++) {
                    swap(arr[x][i], arr[y][j]);
                    unordered_map<char, int> newFreqX = countFrequency(arr[x]);
                    unordered_map<char, int> newFreqY = countFrequency(arr[y]);

                    if (canFormPalindrome(newFreqX) && canFormPalindrome(newFreqY)) {
                        initialPalindromes++;
                        goto nextString;
                    }

                    swap(arr[x][i], arr[y][j]);
                }
            }
        }
        nextString:;
    }

    return initialPalindromes;
}