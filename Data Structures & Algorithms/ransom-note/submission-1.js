class Solution {
    /**
     * @param {string} ransomNote
     * @param {string} magazine
     * @return {boolean}
     */
    canConstruct(ransomNote, magazine) {
        if (ransomNote.length > magazine.length) return false;

        const count = new Int32Array(26);
        const aCode = 97; // ASCII code for 'a'

        for (let i = 0; i < magazine.length; i++) {
            count[magazine.charCodeAt(i) - aCode]++;
        }

        for (let i = 0; i < ransomNote.length; i++) {
            const idx = ransomNote.charCodeAt(i) - aCode;
            count[idx]--;
            if (count[idx] < 0) return false;
        }

        return true;
    }
}
