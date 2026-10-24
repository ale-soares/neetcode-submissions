class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let count = {}
        const sLen = s.length
        const tLen = t.length
    
        if (sLen != tLen) return false
        
        for (let i = 0; i < sLen; i++) {
            if (!count[s[i]]) {
                count[s[i]] = 1
            } else {
                count[s[i]]++
            }
        }
        
        for (let i = 0; i < tLen; i++) {
            if (!count[t[i]]) return false
            
            count[t[i]]--
        }
            
        return true
    }
}
