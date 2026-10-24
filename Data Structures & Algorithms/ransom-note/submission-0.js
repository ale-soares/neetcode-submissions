class Solution {
    /**
     * @param {string} ransomNote
     * @param {string} magazine
     * @return {boolean}
     */
    canConstruct(ransomNote, magazine) {
        let mCount = {}

        for (const e of magazine) {
            if (mCount[e]) {
                mCount[e]++
            } else {
                mCount[e] = 1
            }
        }

        for (const e of ransomNote) {
            if (!mCount[e]) return false

            mCount[e]--
        }

        return true
    }
}
